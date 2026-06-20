import ahpy



C19_comparisons = {

    ('Ausente / Solo exposto', 'Ausente / Solo exposto'): 1,
    ('Ausente / Solo exposto', 'Presente Esparsada'): 3,

    ('Presente Esparsada', 'Ausente / Solo exposto'): 1/3,
    ('Presente Esparsada', 'Presente Esparsada'): 1,

}


C19 = ahpy.Compare(name='C19', comparisons=C19_comparisons, precision=3, random_index='saaty')

print(C19.target_weights)


print(C19.consistency_ratio)


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


debug_linhas(C19)