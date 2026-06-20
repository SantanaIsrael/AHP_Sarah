import ahpy
import numpy as np
 
#target_weights: Prioridades globais de todos os nós folha (alternativas) em relação ao objetivo raiz.
#local_weights: Prioridades relativas ao pai ou mãe imediato na hierarquia.
#global_weights: Prioridades de critérios ou subcritérios relativos ao objetivo raiz.


C15_comparisons = {

    ('Inclinação em árvores, postes e similares', 'Inclinação em árvores, postes e similares'): 1,
    ('Inclinação em árvores, postes e similares', 'Fendas / Trincas no terreno'): 1/5,
    ('Inclinação em árvores, postes e similares', 'Patologias nas construções'): 1/3,
    ('Inclinação em árvores, postes e similares', 'Cicatriz de deslizamento'): 5,
    ('Inclinação em árvores, postes e similares', 'Outras evidências de instabilidade'): 3,

    ('Fendas / Trincas no terreno', 'Inclinação em árvores, postes e similares'): 5,
    ('Fendas / Trincas no terreno', 'Fendas / Trincas no terreno'): 1,
    ('Fendas / Trincas no terreno', 'Patologias nas construções'): 3,
    ('Fendas / Trincas no terreno', 'Cicatriz de deslizamento'): 9,
    ('Fendas / Trincas no terreno', 'Outras evidências de instabilidade'): 7,

    ('Patologias nas construções', 'Inclinação em árvores, postes e similares'): 3,
    ('Patologias nas construções', 'Fendas / Trincas no terreno'): 1/3,
    ('Patologias nas construções', 'Patologias nas construções'): 1,
    ('Patologias nas construções', 'Cicatriz de deslizamento'): 7,
    ('Patologias nas construções', 'Outras evidências de instabilidade'): 5,

    ('Cicatriz de deslizamento', 'Inclinação em árvores, postes e similares'): 1/5,
    ('Cicatriz de deslizamento', 'Fendas / Trincas no terreno'): 1/9,
    ('Cicatriz de deslizamento', 'Patologias nas construções'): 1/7,
    ('Cicatriz de deslizamento', 'Cicatriz de deslizamento'): 1,
    ('Cicatriz de deslizamento', 'Outras evidências de instabilidade'): 1/3,

    ('Outras evidências de instabilidade', 'Inclinação em árvores, postes e similares'): 1/3,
    ('Outras evidências de instabilidade', 'Fendas / Trincas no terreno'): 1/7,
    ('Outras evidências de instabilidade', 'Patologias nas construções'): 1/5,
    ('Outras evidências de instabilidade', 'Cicatriz de deslizamento'): 3,
    ('Outras evidências de instabilidade', 'Outras evidências de instabilidade'): 1,

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


C15 = ahpy.Compare(name='C15', comparisons=C15_comparisons, precision=3, random_index='saaty')

print('TARGET WEIGHTS')
print(C15.target_weights)

print('\nCONSISTENCY RATIO')
print(C15.consistency_ratio)

#debug_linhas(C15)

