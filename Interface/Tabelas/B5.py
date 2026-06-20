import ahpy


B5_comparisons = {

    ('Densidade da Vegetação:', 'Densidade da Vegetação:'): 1,
    ('Densidade da Vegetação:', 'Sitema radicular da vegetação'): 1/3,
    ('Densidade da Vegetação:', 'Tipo de vegetação presente:'): 1/3,
    ('Densidade da Vegetação:', 'Impacto da Vegetação no solo:'): 1/5,
    ('Densidade da Vegetação:', 'Tipo de copa:'): 1/9,

    ('Sitema radicular da vegetação', 'Densidade da Vegetação:'): 3,
    ('Sitema radicular da vegetação', 'Sitema radicular da vegetação'): 1,
    ('Sitema radicular da vegetação', 'Tipo de vegetação presente:'): 3,
    ('Sitema radicular da vegetação', 'Impacto da Vegetação no solo:'): 1/3,
    ('Sitema radicular da vegetação', 'Tipo de copa:'): 1/5,

    ('Tipo de vegetação presente:', 'Densidade da Vegetação:'): 3,
    ('Tipo de vegetação presente:', 'Sitema radicular da vegetação'): 1/3,
    ('Tipo de vegetação presente:', 'Tipo de vegetação presente:'): 1,
    ('Tipo de vegetação presente:', 'Impacto da Vegetação no solo:'): 1/3,
    ('Tipo de vegetação presente:', 'Tipo de copa:'): 1/5,

    ('Impacto da Vegetação no solo:', 'Densidade da Vegetação:'): 5,
    ('Impacto da Vegetação no solo:', 'Sitema radicular da vegetação'): 3,
    ('Impacto da Vegetação no solo:', 'Tipo de vegetação presente:'): 3,
    ('Impacto da Vegetação no solo:', 'Impacto da Vegetação no solo:'): 1,
    ('Impacto da Vegetação no solo:', 'Tipo de copa:'): 1/5,

    ('Tipo de copa:', 'Densidade da Vegetação:'): 9,
    ('Tipo de copa:', 'Sitema radicular da vegetação'): 5,
    ('Tipo de copa:', 'Tipo de vegetação presente:'): 5,
    ('Tipo de copa:', 'Impacto da Vegetação no solo:'): 5,
    ('Tipo de copa:', 'Tipo de copa:'): 1,

}

B5 = ahpy.Compare(name='B5', comparisons=B5_comparisons, precision=3, random_index='saaty')

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
print(B5.target_weights)

print('\nCONSISTENCY RATIO')
print(B5.consistency_ratio)

#debug_linhas(B5)



#report = B5.report(show=True)