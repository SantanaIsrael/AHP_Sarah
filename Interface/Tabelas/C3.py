import ahpy


C3_comparisons = {

    ('1 a 2 Níveis', '1 a 2 Níveis'): 1,
    ('1 a 2 Níveis', '3 a 5 Níveis'): 1/3,
    ('1 a 2 Níveis', '6 a 8 Níveis'): 1/5,
    ('1 a 2 Níveis', 'Superior a 9 Níveis'): 1/7,

    ('3 a 5 Níveis', '1 a 2 Níveis'): 3,
    ('3 a 5 Níveis', '3 a 5 Níveis'): 1,
    ('3 a 5 Níveis', '6 a 8 Níveis'): 1/3,
    ('3 a 5 Níveis', 'Superior a 9 Níveis'): 1/5,

    ('6 a 8 Níveis', '1 a 2 Níveis'): 5,
    ('6 a 8 Níveis', '3 a 5 Níveis'): 3,
    ('6 a 8 Níveis', '6 a 8 Níveis'): 1,
    ('6 a 8 Níveis', 'Superior a 9 Níveis'): 1/3,

    ('Superior a 9 Níveis', '1 a 2 Níveis'): 7,
    ('Superior a 9 Níveis', '3 a 5 Níveis'): 5,
    ('Superior a 9 Níveis', '6 a 8 Níveis'): 3,
    ('Superior a 9 Níveis', 'Superior a 9 Níveis'): 1,

}



C3 = ahpy.Compare(name='C3', comparisons=C3_comparisons, precision=3, random_index='saaty')

print(C3.target_weights)
print(C3.consistency_ratio)

report = C3.report(show=True)


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


debug_linhas(C3)
