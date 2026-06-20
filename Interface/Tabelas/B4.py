import ahpy


B4_comparisons = {

    ('Evidências de Instabilidade:', 'Evidências de Instabilidade:'): 1,
    ('Evidências de Instabilidade:', 'Processos de Movimentação:'): 1/3,

    ('Processos de Movimentação:', 'Evidências de Instabilidade:'): 3,
    ('Processos de Movimentação:', 'Processos de Movimentação:'): 1,

}
B4 = ahpy.Compare(name='B4', comparisons=B4_comparisons, precision=3, random_index='saaty')

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
print(B4.target_weights)

print('\nCONSISTENCY RATIO')
print(B4.consistency_ratio)

debug_linhas(B4)



report = B4.report(show=True)