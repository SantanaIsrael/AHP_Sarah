from flask import Flask, render_template, jsonify, request
import importlib.util
import pathlib
import ahpy

app = Flask(__name__)

PASTA_TABELAS = pathlib.Path("Tabelas")


@app.route("/")
def index():
    return render_template("index.html")


def carregar_modulo(arquivo):
    spec = importlib.util.spec_from_file_location(
        arquivo.stem,
        arquivo
    )

    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)

    return modulo


@app.get("/api/Tabelas")
def listar_tabelas():

    arquivos = sorted(PASTA_TABELAS.glob("*.py"))

    return jsonify([
        arquivo.stem
        for arquivo in arquivos
    ])


@app.get("/api/Tabelas/<nome>")
def obter_tabela(nome):

    arquivo = PASTA_TABELAS / f"{nome}.py"

    modulo = carregar_modulo(arquivo)

    comparacoes = None

    for atributo in dir(modulo):

        if atributo.endswith("_comparisons"):

            comparacoes = getattr(modulo, atributo)
            break

    if comparacoes is None:
        return jsonify({"erro": "comparações não encontradas"}), 404

    elementos = []

    for par in comparacoes.keys():
        for item in par:
            if item not in elementos:
                elementos.append(item)

    compare = ahpy.Compare(
        name=nome,
        comparisons=comparacoes,
        precision=3,
        random_index="saaty"
    )

    return jsonify({
        "nome": nome,
        "elementos": elementos,
        "comparacoes": [
            {
                "row": k[0],
                "col": k[1],
                "value": v
            }
            for k, v in comparacoes.items()
        ],
        "weights": compare.target_weights,
        "cr": compare.consistency_ratio
    })


@app.post("/api/calcular")
def calcular():

    dados = request.get_json()

    comparacoes = {
        (item["row"], item["col"]): item["value"]
        for item in dados["comparacoes"]
    }

    compare = ahpy.Compare(
        name=dados["nome"],
        comparisons=comparacoes,
        precision=3,
        random_index="saaty"
    )

    return jsonify({
        "weights": compare.target_weights,
        "cr": compare.consistency_ratio
    })

if __name__ == "__main__":
    app.run(debug=True)
