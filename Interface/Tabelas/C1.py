import ahpy



C1_comparisons = {

    ('D < 10 Hab/km²', 'D < 10 Hab/km²'): 1,
    ('D < 10 Hab/km²', '10 ≤ D < 50 Hab/km²'): 1/3,
    ('D < 10 Hab/km²', '50 ≤ D < 100 Hab/km²'): 1/5,
    ('D < 10 Hab/km²', '100 ≤ D 150 Hab/km²'): 1/7,
    ('D < 10 Hab/km²', 'D ≥ 150 Hab/km²'): 1/9,

    ('10 ≤ D < 50 Hab/km²', 'D < 10 Hab/km²'): 3,
    ('10 ≤ D < 50 Hab/km²', '10 ≤ D < 50 Hab/km²'): 1,
    ('10 ≤ D < 50 Hab/km²', '50 ≤ D < 100 Hab/km²'): 1/3,
    ('10 ≤ D < 50 Hab/km²', '100 ≤ D 150 Hab/km²'): 1/5,
    ('10 ≤ D < 50 Hab/km²', 'D ≥ 150 Hab/km²'): 1/7,

    ('50 ≤ D < 100 Hab/km²', 'D < 10 Hab/km²'): 5,
    ('50 ≤ D < 100 Hab/km²', '10 ≤ D < 50 Hab/km²'): 3,
    ('50 ≤ D < 100 Hab/km²', '50 ≤ D < 100 Hab/km²'): 1,
    ('50 ≤ D < 100 Hab/km²', '100 ≤ D 150 Hab/km²'): 1/3,
    ('50 ≤ D < 100 Hab/km²', 'D ≥ 150 Hab/km²'): 1/5,

    ('100 ≤ D 150 Hab/km²', 'D < 10 Hab/km²'): 7,
    ('100 ≤ D 150 Hab/km²', '10 ≤ D < 50 Hab/km²'): 5,
    ('100 ≤ D 150 Hab/km²', '50 ≤ D < 100 Hab/km²'): 3,
    ('100 ≤ D 150 Hab/km²', '100 ≤ D 150 Hab/km²'): 1,
    ('100 ≤ D 150 Hab/km²', 'D ≥ 150 Hab/km²'): 1/3,

    ('D ≥ 150 Hab/km²', 'D < 10 Hab/km²'): 9,
    ('D ≥ 150 Hab/km²', '10 ≤ D < 50 Hab/km²'): 7,
    ('D ≥ 150 Hab/km²', '50 ≤ D < 100 Hab/km²'): 5,
    ('D ≥ 150 Hab/km²', '100 ≤ D 150 Hab/km²'): 3,
    ('D ≥ 150 Hab/km²', 'D ≥ 150 Hab/km²'): 1,

}


C1 = ahpy.Compare(name='C1', comparisons=C1_comparisons, precision=3, random_index='saaty')



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


debug_linhas(C1)

print('\nCONSISTENCY RATIO')
print(C1.consistency_ratio)
