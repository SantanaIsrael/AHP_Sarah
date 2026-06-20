import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.




C12_comparisons = {

    ('Convexa', 'Convexa'): 1,
    ('Convexa', 'Planar'): 1/3,
    ('Convexa', 'Côncava'): 1/5,

    ('Planar', 'Convexa'): 3,
    ('Planar', 'Planar'): 1,
    ('Planar', 'Côncava'): 1/3,

    ('Côncava', 'Convexa'): 5,
    ('Côncava', 'Planar'): 3,
    ('Côncava', 'Côncava'): 1,

}


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


C12 = ahpy.Compare(name='C12', comparisons=C12_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C12.target_weights)

print('\nCONSISTENCY RATIO')
print(C12.consistency_ratio)

#debug_linhas(C12)
