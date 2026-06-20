import ahpy


B1_comparisons = {

    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 1,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Tipo das Edificações:'): 5,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Porte das Edificações:'): 1/3,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Condições das Vias:'): 5,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Histórico de Ocorrências:'): 1/3,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Abastecimento de Água:'): 5,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Sistema de Esgotamento:'): 3,
    ('Número de Residentes / Densidade habitacional (D= hab/ha )', 'Depósito Antrópico:'): 1/3,

    ('Tipo das Edificações:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 1/5,
    ('Tipo das Edificações:', 'Tipo das Edificações:'): 1,
    ('Tipo das Edificações:', 'Porte das Edificações:'): 1/7,
    ('Tipo das Edificações:', 'Condições das Vias:'): 1,
    ('Tipo das Edificações:', 'Histórico de Ocorrências:'): 1/3,
    ('Tipo das Edificações:', 'Abastecimento de Água:'): 1,
    ('Tipo das Edificações:', 'Sistema de Esgotamento:'): 1/2,
    ('Tipo das Edificações:', 'Depósito Antrópico:'): 1/7,

    ('Porte das Edificações:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 3,
    ('Porte das Edificações:', 'Tipo das Edificações:'): 7,
    ('Porte das Edificações:', 'Porte das Edificações:'): 1,
    ('Porte das Edificações:', 'Condições das Vias:'): 9,
    ('Porte das Edificações:', 'Histórico de Ocorrências:'): 1/3,
    ('Porte das Edificações:', 'Abastecimento de Água:'): 5,
    ('Porte das Edificações:', 'Sistema de Esgotamento:'): 5,
    ('Porte das Edificações:', 'Depósito Antrópico:'): 1/5,

    ('Condições das Vias:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 1/5,
    ('Condições das Vias:', 'Tipo das Edificações:'): 1,
    ('Condições das Vias:', 'Porte das Edificações:'): 1/9,
    ('Condições das Vias:', 'Condições das Vias:'): 1,
    ('Condições das Vias:', 'Histórico de Ocorrências:'): 1/7,
    ('Condições das Vias:', 'Abastecimento de Água:'): 1/3,
    ('Condições das Vias:', 'Sistema de Esgotamento:'): 1/7,
    ('Condições das Vias:', 'Depósito Antrópico:'): 1/7,

    ('Histórico de Ocorrências:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 3,
    ('Histórico de Ocorrências:', 'Tipo das Edificações:'): 3,
    ('Histórico de Ocorrências:', 'Porte das Edificações:'): 3,
    ('Histórico de Ocorrências:', 'Condições das Vias:'): 7,
    ('Histórico de Ocorrências:', 'Histórico de Ocorrências:'): 1,
    ('Histórico de Ocorrências:', 'Abastecimento de Água:'): 5,
    ('Histórico de Ocorrências:', 'Sistema de Esgotamento:'): 5,
    ('Histórico de Ocorrências:', 'Depósito Antrópico:'): 1/3,

    ('Abastecimento de Água:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 1/5,
    ('Abastecimento de Água:', 'Tipo das Edificações:'): 1,
    ('Abastecimento de Água:', 'Porte das Edificações:'): 1/5,
    ('Abastecimento de Água:', 'Condições das Vias:'): 3,
    ('Abastecimento de Água:', 'Histórico de Ocorrências:'): 1/5,
    ('Abastecimento de Água:', 'Abastecimento de Água:'): 1,
    ('Abastecimento de Água:', 'Sistema de Esgotamento:'): 1/3,
    ('Abastecimento de Água:', 'Depósito Antrópico:'): 1/7,

    ('Sistema de Esgotamento:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 1/3,
    ('Sistema de Esgotamento:', 'Tipo das Edificações:'): 2,
    ('Sistema de Esgotamento:', 'Porte das Edificações:'): 1/5,
    ('Sistema de Esgotamento:', 'Condições das Vias:'): 7,
    ('Sistema de Esgotamento:', 'Histórico de Ocorrências:'): 1/5,
    ('Sistema de Esgotamento:', 'Abastecimento de Água:'): 3,
    ('Sistema de Esgotamento:', 'Sistema de Esgotamento:'): 1,
    ('Sistema de Esgotamento:', 'Depósito Antrópico:'): 1/5,

    ('Depósito Antrópico:', 'Número de Residentes / Densidade habitacional (D= hab/ha )'): 3,
    ('Depósito Antrópico:', 'Tipo das Edificações:'): 7,
    ('Depósito Antrópico:', 'Porte das Edificações:'): 5,
    ('Depósito Antrópico:', 'Condições das Vias:'): 7,
    ('Depósito Antrópico:', 'Histórico de Ocorrências:'): 3,
    ('Depósito Antrópico:', 'Abastecimento de Água:'): 7,
    ('Depósito Antrópico:', 'Sistema de Esgotamento:'): 5,
    ('Depósito Antrópico:', 'Depósito Antrópico:'): 1,

}
B1 = ahpy.Compare(name='B1', comparisons=B1_comparisons, precision=3, random_index='saaty')

def debug_linhas(compare):
    elementos = compare._elements
    matriz = compare._matrix
    somas_colunas = matriz.sum(axis=0)
    matriz_normalizada = matriz / somas_colunas
    pesos_por_media_linha = matriz_normalizada.mean(axis=1)

    print('\nSOMAS DAS COLUNAS')
    for elemento, soma in zip(elementos, somas_colunas):
        print(f'{elemento}: {soma:.3f}')

    print('\nDEBUG POR LINHA')
    for i, elemento_linha in enumerate(elementos):
        print(f'\n{elemento_linha}')
        for j, elemento_coluna in enumerate(elementos):
            valor_original = matriz[i, j]
            valor_normalizado = matriz_normalizada[i, j]
            print(
                f'  vs {elemento_coluna}: '
                f'original={valor_original:.3f}, normalizado={valor_normalizado:.3f}'
            )
        print(f'  media da linha normalizada: {pesos_por_media_linha[i]:.3f}')
        print(f'  target_weight ahpy: {compare.target_weights[elemento_linha]:.3f}')




print('TARGET WEIGHTS')
print(B1.target_weights)

print('\nCONSISTENCY RATIO')
print(B1.consistency_ratio)

debug_linhas(B1)



report = B1.report(show=True)