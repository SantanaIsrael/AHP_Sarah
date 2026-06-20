import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.


C13_comparisons = {

    ('entre 0° e 17°', 'entre 0° e 17°'): 1,
    ('entre 0° e 17°', 'entre 17,1° e 45°'): 1/3,
    ('entre 0° e 17°', 'entre 45,1° e 60°'): 1/5,
    ('entre 0° e 17°', 'entre 60,1° e 90°'): 1/7,

    ('entre 17,1° e 45°', 'entre 0° e 17°'): 3,
    ('entre 17,1° e 45°', 'entre 17,1° e 45°'): 1,
    ('entre 17,1° e 45°', 'entre 45,1° e 60°'): 1/3,
    ('entre 17,1° e 45°', 'entre 60,1° e 90°'): 1/5,

    ('entre 45,1° e 60°', 'entre 0° e 17°'): 5,
    ('entre 45,1° e 60°', 'entre 17,1° e 45°'): 3,
    ('entre 45,1° e 60°', 'entre 45,1° e 60°'): 1,
    ('entre 45,1° e 60°', 'entre 60,1° e 90°'): 1/3,

    ('entre 60,1° e 90°', 'entre 0° e 17°'): 7,
    ('entre 60,1° e 90°', 'entre 17,1° e 45°'): 5,
    ('entre 60,1° e 90°', 'entre 45,1° e 60°'): 3,
    ('entre 60,1° e 90°', 'entre 60,1° e 90°'): 1,

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


C13 = ahpy.Compare(name='C13', comparisons=C13_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C13.target_weights)

print('\nCONSISTENCY RATIO')
print(C13.consistency_ratio)

#debug_linhas(C13)
