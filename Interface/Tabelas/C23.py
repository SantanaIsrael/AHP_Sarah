import ahpy




C23_comparisons = {

    ('Copa frondosa', 'Copa frondosa'): 1,
    ('Copa frondosa', 'Copa escassa'): 7,

    ('Copa escassa', 'Copa frondosa'): 1/7,
    ('Copa escassa', 'Copa escassa'): 1,

}


C23 = ahpy.Compare(name='A', comparisons=C23_comparisons, precision=3, random_index='saaty')

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
print(C23.target_weights)

print('\nCONSISTENCY RATIO')
print(C23.consistency_ratio)

debug_linhas(C23)



report = C23.report(show=True)