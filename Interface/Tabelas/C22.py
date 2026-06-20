import ahpy



C22_comparisons = {

    ('Quase rigido: Transfere toda energia de vento ao solo', 'Quase rigido: Transfere toda energia de vento ao solo'): 1,
    ('Quase rigido: Transfere toda energia de vento ao solo', 'Semi-flexível: Transfere parcialmente a carga de vento ao solo'): 5,
    ('Quase rigido: Transfere toda energia de vento ao solo', 'Não há transferência de energia ao solo'): 7,

    ('Semi-flexível: Transfere parcialmente a carga de vento ao solo', 'Quase rigido: Transfere toda energia de vento ao solo'): 1/5,
    ('Semi-flexível: Transfere parcialmente a carga de vento ao solo', 'Semi-flexível: Transfere parcialmente a carga de vento ao solo'): 1,
    ('Semi-flexível: Transfere parcialmente a carga de vento ao solo', 'Não há transferência de energia ao solo'): 3,

    ('Não há transferência de energia ao solo', 'Quase rigido: Transfere toda energia de vento ao solo'): 1/7,
    ('Não há transferência de energia ao solo', 'Semi-flexível: Transfere parcialmente a carga de vento ao solo'): 1/3,
    ('Não há transferência de energia ao solo', 'Não há transferência de energia ao solo'): 1,

}


C22 = ahpy.Compare(name='A', comparisons=C22_comparisons, precision=3, random_index='saaty')

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
print(C22.target_weights)

print('\nCONSISTENCY RATIO')
print(C22.consistency_ratio)

debug_linhas(C22)



report = C22.report(show=True)