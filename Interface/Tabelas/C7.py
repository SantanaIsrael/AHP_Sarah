import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.


C7_comparisons = {

    ('Fossa', 'Fossa'): 1,
    ('Fossa', 'Despejo direto na encosta'): 1/5,
    ('Fossa', 'Conectada à rede de drenagem/esgoto'): 3,

    ('Despejo direto na encosta', 'Fossa'): 5,
    ('Despejo direto na encosta', 'Despejo direto na encosta'): 1,
    ('Despejo direto na encosta', 'Conectada à rede de drenagem/esgoto'): 9,

    ('Conectada à rede de drenagem/esgoto', 'Fossa'): 1/3,
    ('Conectada à rede de drenagem/esgoto', 'Despejo direto na encosta'): 1/9,
    ('Conectada à rede de drenagem/esgoto', 'Conectada à rede de drenagem/esgoto'): 1,

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


C7 = ahpy.Compare(name='C7', comparisons=C7_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C7.target_weights)

print('\nCONSISTENCY RATIO')
print(C7.consistency_ratio)

#debug_linhas(C7)
