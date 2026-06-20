import ahpy



C2_comparisons = {

    ('Alvenaria estrutural', 'Alvenaria estrutural'): 1,
    ('Alvenaria estrutural', 'Madeira'): 9,
    ('Alvenaria estrutural', 'Concreto'): 3,
    ('Alvenaria estrutural', 'Mista'): 7,

    ('Madeira', 'Alvenaria estrutural'): 1/9,
    ('Madeira', 'Madeira'): 1,
    ('Madeira', 'Concreto'): 1/7,
    ('Madeira', 'Mista'): 1/3,

    ('Concreto', 'Alvenaria estrutural'): 1/3,
    ('Concreto', 'Madeira'): 7,
    ('Concreto', 'Concreto'): 1,
    ('Concreto', 'Mista'): 7,

    ('Mista', 'Alvenaria estrutural'): 1/7,
    ('Mista', 'Madeira'): 3,
    ('Mista', 'Concreto'): 1/7,
    ('Mista', 'Mista'): 1,

}
C2 = ahpy.Compare(name='C2', comparisons=C2_comparisons, precision=3, random_index='saaty')

print(C2.target_weights)
print(C2.consistency_ratio)

#report = C2.report(show=True)


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


#debug_linhas(C2)
