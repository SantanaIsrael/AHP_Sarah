import ahpy




B3_comparisons = {

    ('Drenagem de águas pluviais:', 'Drenagem de águas pluviais:'): 1,
    ('Drenagem de águas pluviais:', 'Infiltrações no solo:'): 1/3,

    ('Infiltrações no solo:', 'Drenagem de águas pluviais:'): 3,
    ('Infiltrações no solo:', 'Infiltrações no solo:'): 1,

}
B3 = ahpy.Compare(name='B3', comparisons=B3_comparisons, precision=3, random_index='saaty')

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
print(B3.target_weights)

print('\nCONSISTENCY RATIO')
print(B3.consistency_ratio)

debug_linhas(B3)



report = B3.report(show=True)