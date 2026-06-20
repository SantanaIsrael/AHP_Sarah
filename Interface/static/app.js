
const VALORES_SAATY = [
  ["1/9", 1 / 9], ["1/8", 1 / 8], ["1/7", 1 / 7], ["1/6", 1 / 6],
  ["1/5", 1 / 5], ["1/4", 1 / 4], ["1/3", 1 / 3], ["1/2", 1 / 2],
  ["1", 1], ["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6],
  ["7", 7], ["8", 8], ["9", 9]
];

//armazenar informações da aplicação
const estado = {
  currentName: "",   //nome atual
  changedCells: new Set()  //celulas alteradas
};

//referências dos componentes
const elementos = {
  tableSelect: document.querySelector("#tableSelect"),
  rowSelect: document.querySelector("#rowSelect"),
  colSelect: document.querySelector("#colSelect"),
  weightSelect: document.querySelector("#weightSelect"),
  applyButton: document.querySelector("#applyButton"),
  downloadButton: document.querySelector("#downloadButton"),
  fileInput: document.querySelector("#fileInput"),
  loadStatus: document.querySelector("#loadStatus"),
  tableInfo: document.querySelector("#tableInfo"),
  matrixWrap: document.querySelector("#matrixWrap"),
  crValue: document.querySelector("#crValue"),
  weightsList: document.querySelector("#weightsList")
};

//identificar a comparação que ta sendo feita
function comparisonKey(row, col) {
  return `${row}\u0000${col}`;
}

//inverso da matriz
function splitComparisonKey(key) {
  return key.split("\u0000");
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

//conversão string p numero
function parseNumericExpression(text) {
  const clean = text.trim();
  if (/^nan$/i.test(clean)) return null;
  if (/^-?\d+(\.\d+)?$/.test(clean)) return Number(clean);

  const fraction = clean.match(/^(-?\d+(?:\.\d+)?)\s*\/\s*(-?\d+(?:\.\d+)?)$/);
  if (fraction) {
    return Number(fraction[1]) / Number(fraction[2]);
  }

  return null;
}

function normalizeReciprocalComparisons(table) {
  const { comparisons, elements } = table;

  for (let rowIndex = 0; rowIndex < elements.length; rowIndex += 1) {
    const row = elements[rowIndex];
    comparisons.set(comparisonKey(row, row), 1);

    for (let colIndex = rowIndex + 1; colIndex < elements.length; colIndex += 1) {
      const col = elements[colIndex];
      const key = comparisonKey(row, col);
      const reverseKey = comparisonKey(col, row);
      const forward = comparisons.get(key);
      const reverse = comparisons.get(reverseKey);

      if (forward !== undefined) {
        comparisons.set(reverseKey, 1 / forward);
      } else if (reverse !== undefined) {
        comparisons.set(key, 1 / reverse);
      } else {
        comparisons.set(key, 1);
        comparisons.set(reverseKey, 1);
      }
    }
  }

  return table;
}

function addTables(tables) {
  for (const table of tables) {
    estado.tables[table.name] = table;
  }

  const names = Object.keys(estado.tables).sort((a, b) => a.localeCompare(b, "pt-BR", { numeric: true }));
  elementos.tableSelect.innerHTML = names
    .map((name) => `<option value="${escapeHtml(name)}">${escapeHtml(name)}</option>`)
    .join("");

  if (names.length > 0 && !estado.currentName) {
    estado.currentName = names[0];
    elementos.tableSelect.value = estado.currentName;
  }

  elementos.loadStatus.textContent = `${names.length} tabelas carregadas`;
  renderCurrentTable();
}

function fillSelect(select, values) {
  select.innerHTML = values
    .map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`)
    .join("");
}

document.getElementById("weightSelect").addEventListener("input", function() {
  const item = VALORES_SAATY[this.value];
  document.getElementById("weightDisplay").textContent = item.display;
});

// Para obter o valor numérico ao aplicar:
function getSelectedWeight() {
  return VALORES_SAATY[document.getElementById("weightSelect").value].numeric;
}
function currentTable() {
  return estado.tables[estado.currentName];
}

function formatWeight(value) {
  const close = (target) => Math.abs(value - target) < 1e-9;

  for (const [label, saatValue] of VALORES_SAATY) {
    if (close(saatValue)) return label;
  }

  return value.toFixed(3);
}

function sourceWeight(value) {
  const close = (target) => Math.abs(value - target) < 1e-9;

  for (const [label, saatValue] of VALORES_SAATY) {
    if (!close(saatValue)) continue;
    if (label.includes("/")) return label;
    return label === "1" ? "1" : `${label}/1`;
  }

  return Number(value.toFixed(6)).toString();
}

function comparisonValue(table, row, col) {
  return table.comparisons.get(comparisonKey(row, col)) ?? 1;
}

function renderCurrentTable() {
  const table = currentTable();
  if (!table) {
    elementos.matrixWrap.innerHTML = "";
    elementos.weightsList.innerHTML = "";
    elementos.crValue.textContent = "CR: -";
    elementos.tableInfo.textContent = "";
    return;
  }

  fillSelect(elementos.rowSelect, table.elements);
  fillSelect(elementos.colSelect, table.elements);
  if (table.elements.length > 1) {
    elementos.rowSelect.value = table.elements[0];
    elementos.colSelect.value = table.elements[1];
  }

  elementos.tableInfo.textContent = `${table.fileName} - ${table.elements.length} itens`;
  renderMatrix(table);
  renderResults(table.weights, table.cr, table.elements);
}

async function applySelectedWeight() {

  const row = elementos.rowSelect.value;
  const col = elementos.colSelect.value;

  if (row === col) {
    alert("A diagonal da matriz sempre deve ser 1.");
    return;
  }

  const idx = parseInt(elementos.weightSelect.value);
  const selected = VALORES_SAATY[idx];

  if (!selected) return;

  const value = selected[1];

  const comparacoes =
    estado.currentTable.comparacoes;

  const direta = comparacoes.find(
    item =>
      item.row === row &&
      item.col === col
  );

  const inversa = comparacoes.find(
    item =>
      item.row === col &&
      item.col === row
  );

  if (direta) {
    direta.value = value;
  }

  if (inversa) {
    inversa.value = 1 / value;
  }

  estado.changedCells.add(`${row}|||${col}`);
estado.changedCells.add(`${col}|||${row}`);

  const response = await fetch(
    "/api/calcular",
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json"
      },
      body: JSON.stringify({
        nome:
          estado.currentTable.nome,
        comparacoes:
          comparacoes
      })
    }
  );

  const resultado =
    await response.json();

  renderMatrix(
    estado.currentTable
  );

  renderResults(
    resultado.weights,
    resultado.cr,
    estado.currentTable.elementos
  );
}


async function loadManualFiles(files) {
  const tables = [];

  for (const file of files) {
    const source = await file.text();
    const table = parseComparisonFile(file.name, source);
    if (table) tables.push(normalizeReciprocalComparisons(table));
  }

  addTables(tables);
}

function bindEvents() {

  elementos.tableSelect.addEventListener(
    "change",
    async () => {

      estado.changedCells.clear();
      const nome =
        elementos.tableSelect.value;

      console.log("Carregando:", nome);

      await loadTable(nome);

    }
  );

  elementos.applyButton.addEventListener(
    "click",
    applySelectedWeight
  );

}

function fillSelect(select, values) {

    select.innerHTML =
        values.map(value =>
            `<option value="${value}">${value}</option>`
        ).join("");
}
function renderMatrix(data) {

    const elementosLista =
        data.elementos;

    const comparacoes =
        data.comparacoes;

    const mapa = {};

    comparacoes.forEach(item => {

        mapa[
            `${item.row}|||${item.col}`
        ] = item.value;

    });

    const header = elementosLista
        .map(item => `<th>${escapeHtml(item)}</th>`)
        .join("");

    const rows = elementosLista.map(row => {

        const cells = elementosLista.map(col => {

            const chave =
                `${row}|||${col}`;

            const valor =
                mapa[chave] ?? 1;

            const classe = [
                row === col ? "diagonal" : "",
                estado.changedCells.has(chave)
                    ? "changed"
                    : ""
            ]
            .filter(Boolean)
            .join(" ");

            return `
                <td class="${classe}">
                    ${formatWeight(valor)}
                </td>
            `;

        }).join("");

        return `
            <tr>
                <td>${escapeHtml(row)}</td>
                ${cells}
            </tr>
        `;

    }).join("");

    elementos.matrixWrap.innerHTML = `
        <table>
            <thead>
                <tr>
                    <th></th>
                    ${header}
                </tr>
            </thead>
            <tbody>
                ${rows}
            </tbody>
        </table>
    `;
}
function renderResults(weights, cr, order) {

    elementos.crValue.textContent =
        `CR: ${cr}`;

    const entries = (order ?? Object.keys(weights))
        .filter(nome => weights[nome] !== undefined)
        .map(nome => [nome, weights[nome]]);

    elementos.weightsList.innerHTML =
        entries
        .map(([nome, peso]) => `

            <div class="weight-row">

                <div>
                    <div class="weight-name">
                        ${nome}
                    </div>

                    <div class="bar">
                        <span style="
                            width:${peso * 100}%
                        "></span>
                    </div>
                </div>

                <div class="weight-value">
                    ${peso}
                </div>

            </div>

        `).join("");
}

async function loadTable(nome) {

    const response =
        await fetch(`/api/Tabelas/${nome}`);

    const data =
        await response.json();

    console.log(data);

    estado.currentTable = data;

    fillSelect(
        elementos.rowSelect,
        data.elementos
    );

    fillSelect(
        elementos.colSelect,
        data.elementos
    );

    renderMatrix(data);

    renderResults(
        data.weights,
        data.cr,
        data.elementos
    );
}

function fillWeightSelect() {
  const slider = elementos.weightSelect;
  slider.min = 0;
  slider.max = VALORES_SAATY.length - 1;
  slider.value = Math.floor(VALORES_SAATY.length / 2); // índice do "1"
  updateWeightDisplay();
}

function updateWeightDisplay() {
  const idx = parseInt(elementos.weightSelect.value);
  const [label] = VALORES_SAATY[idx];
  document.getElementById("weightDisplay").textContent = label;
  // feedback visual: lado esquerdo = frações, direito = inteiros
  const isFraction = label.includes("/");
  document.getElementById("weightSide").textContent  = isFraction ? label : "←";
  document.getElementById("weightSide2").textContent = isFraction ? "→" : label;
}

elementos.weightSelect.addEventListener("input", updateWeightDisplay);
async function start() {

    fillWeightSelect();

    bindEvents();

    const response =
        await fetch("/api/Tabelas");

    const tabelas =
        await response.json();

    elementos.tableSelect.innerHTML =
        tabelas.map(nome =>
            `<option value="${nome}">${nome}</option>`
        ).join("");

    if (tabelas.length > 0) {

        await loadTable(
            tabelas[0]
        );
    }
}

function downloadAhpyScript() {
  const table = estado.currentTable;
  if (!table) {
    alert("Nenhuma tabela carregada.");
    return;
  }

  const nome = table.nome.replace(/[^a-zA-Z0-9_]/g, "_");
  const elementos = table.elementos;
  const mapa = {};
  table.comparacoes.forEach(item => {
    mapa[`${item.row}|||${item.col}`] = item.value;
  });

  const linhasComparacoes = [];
  for (const row of elementos) {
    for (const col of elementos) {
      const chave = `${row}|||${col}`;
      const valor = mapa[chave] ?? 1;
      const valorFormatado = formatarFracao(valor);
      linhasComparacoes.push(`    ('${row}', '${col}'): ${valorFormatado},`);
    }
  }

  const script = `import ahpy


${nome}_comparisons = {
${linhasComparacoes.join("\n")}
}

${nome} = ahpy.Compare(name='${nome}', comparisons=${nome}_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(${nome}.target_weights)

print('\\nCONSISTENCY RATIO')
print(${nome}.consistency_ratio)

report = ${nome}.report(show=True)
`;

  const blob = new Blob([script], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${nome}_ahpy.py`;
  a.click();
  URL.revokeObjectURL(url);
}

function formatarFracao(valor) {
  for (const [label, num] of VALORES_SAATY) {
    if (Math.abs(valor - num) < 1e-9) {
      if (label.includes("/")) return label;
      return label;
    }
  }
  return valor.toFixed(6);
}

start();
