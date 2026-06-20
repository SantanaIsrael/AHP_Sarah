import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.


C14_comparisons = {

    ('Material estável', 'Material estável'): 1,
    ('Material estável', 'Rocha alterada / Matacões'): 1/3,
    ('Material estável', 'Solo Laterítico'): 1/5,
    ('Material estável', 'Solos Transportados'): 1/7,
    ('Material estável', 'Material Predominantemente Orgânico'): 1/9,

    ('Rocha alterada / Matacões', 'Material estável'): 3,
    ('Rocha alterada / Matacões', 'Rocha alterada / Matacões'): 1,
    ('Rocha alterada / Matacões', 'Solo Laterítico'): 1/3,
    ('Rocha alterada / Matacões', 'Solos Transportados'): 1/5,
    ('Rocha alterada / Matacões', 'Material Predominantemente Orgânico'): 1/7,

    ('Solo Laterítico', 'Material estável'): 5,
    ('Solo Laterítico', 'Rocha alterada / Matacões'): 3,
    ('Solo Laterítico', 'Solo Laterítico'): 1,
    ('Solo Laterítico', 'Solos Transportados'): 1/3,
    ('Solo Laterítico', 'Material Predominantemente Orgânico'): 1/5,

    ('Solos Transportados', 'Material estável'): 7,
    ('Solos Transportados', 'Rocha alterada / Matacões'): 5,
    ('Solos Transportados', 'Solo Laterítico'): 3,
    ('Solos Transportados', 'Solos Transportados'): 1,
    ('Solos Transportados', 'Material Predominantemente Orgânico'): 1/3,

    ('Material Predominantemente Orgânico', 'Material estável'): 9,
    ('Material Predominantemente Orgânico', 'Rocha alterada / Matacões'): 7,
    ('Material Predominantemente Orgânico', 'Solo Laterítico'): 5,
    ('Material Predominantemente Orgânico', 'Solos Transportados'): 3,
    ('Material Predominantemente Orgânico', 'Material Predominantemente Orgânico'): 1,

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


C14 = ahpy.Compare(name='C14', comparisons=C14_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C14.target_weights)

print('\nCONSISTENCY RATIO')
print(C14.consistency_ratio)

#debug_linhas(C14)
