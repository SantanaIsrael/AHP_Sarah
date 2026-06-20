import ahpy

C5_comparisons = {

    ('Sem ocorrências', 'Sem ocorrências'): 1,
    ('Sem ocorrências', '1 a 2 Ocorrências'): 1/5,
    ('Sem ocorrências', 'Mais de 2 Ocorrências'): 1/7,

    ('1 a 2 Ocorrências', 'Sem ocorrências'): 5,
    ('1 a 2 Ocorrências', '1 a 2 Ocorrências'): 1,
    ('1 a 2 Ocorrências', 'Mais de 2 Ocorrências'): 1/3,

    ('Mais de 2 Ocorrências', 'Sem ocorrências'): 7,
    ('Mais de 2 Ocorrências', '1 a 2 Ocorrências'): 3,
    ('Mais de 2 Ocorrências', 'Mais de 2 Ocorrências'): 1,

}
C5 = ahpy.Compare(name='C5', comparisons=C5_comparisons, precision=3, random_index='saaty')

print(C5.target_weights)
print(C5.consistency_ratio)

#report = C5.report(show=True)


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


#debug_linhas(C5)
