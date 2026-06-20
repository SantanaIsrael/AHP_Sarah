import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.



C16_comparisons = {

    ('Escoamento', 'Escoamento'): 1,
    ('Escoamento', 'Escorregamento'): 5,
    ('Escoamento', 'Transporte'): 3,

    ('Escorregamento', 'Escoamento'): 1/5,
    ('Escorregamento', 'Escorregamento'): 1,
    ('Escorregamento', 'Transporte'): 1/3,

    ('Transporte', 'Escoamento'): 1/3,
    ('Transporte', 'Escorregamento'): 3,
    ('Transporte', 'Transporte'): 1,

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


C16 = ahpy.Compare(name='C16', comparisons=C16_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C16.target_weights)

print('\nCONSISTENCY RATIO')
print(C16.consistency_ratio)

#debug_linhas(C16)
