import ahpy


C20_comparisons = {

    ('de rasa profundidade (até 0,5m)', 'de rasa profundidade (até 0,5m)'): 1,
    ('de rasa profundidade (até 0,5m)', 'de média profundidade (de 0,5m a 1m)'): 5,
    ('de rasa profundidade (até 0,5m)', 'de grande profundidade (superior a 1m)'): 7,

    ('de média profundidade (de 0,5m a 1m)', 'de rasa profundidade (até 0,5m)'): 1/2,
    ('de média profundidade (de 0,5m a 1m)', 'de média profundidade (de 0,5m a 1m)'): 1,
    ('de média profundidade (de 0,5m a 1m)', 'de grande profundidade (superior a 1m)'): 3,

    ('de grande profundidade (superior a 1m)', 'de rasa profundidade (até 0,5m)'): 1/7,
    ('de grande profundidade (superior a 1m)', 'de média profundidade (de 0,5m a 1m)'): 1/3,
    ('de grande profundidade (superior a 1m)', 'de grande profundidade (superior a 1m)'): 1,

}
C20 = ahpy.Compare(name='C20', comparisons=C20_comparisons, precision=3, random_index='saaty')

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
print(C20.target_weights)

print('\nCONSISTENCY RATIO')
print(C20.consistency_ratio)

debug_linhas(C20)



report = C20.report(show=True)