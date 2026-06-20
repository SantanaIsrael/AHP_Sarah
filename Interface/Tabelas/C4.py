import ahpy



C4_comparisons = {

    ('Via em Terra', 'Via em Terra'): 1,
    ('Via em Terra', 'Via em Cascalho/Brita'): 2,
    ('Via em Terra', 'Paralelepípedo'): 2,
    ('Via em Terra', 'Pav. Concreto'): 1/5,
    ('Via em Terra', 'Pav. Intertravado'): 1/3,
    ('Via em Terra', 'Pav. Asfáltico'): 1/9,

    ('Via em Cascalho/Brita', 'Via em Terra'): 1/2,
    ('Via em Cascalho/Brita', 'Via em Cascalho/Brita'): 1,
    ('Via em Cascalho/Brita', 'Paralelepípedo'): 1/2,
    ('Via em Cascalho/Brita', 'Pav. Concreto'): 1/7,
    ('Via em Cascalho/Brita', 'Pav. Intertravado'): 1/3,
    ('Via em Cascalho/Brita', 'Pav. Asfáltico'): 1/7,

    ('Paralelepípedo', 'Via em Terra'): 1/2,
    ('Paralelepípedo', 'Via em Cascalho/Brita'): 2,
    ('Paralelepípedo', 'Paralelepípedo'): 1,
    ('Paralelepípedo', 'Pav. Concreto'): 1/5,
    ('Paralelepípedo', 'Pav. Intertravado'): 1,
    ('Paralelepípedo', 'Pav. Asfáltico'): 1/5,

    ('Pav. Concreto', 'Via em Terra'): 5,
    ('Pav. Concreto', 'Via em Cascalho/Brita'): 7,
    ('Pav. Concreto', 'Paralelepípedo'): 5,
    ('Pav. Concreto', 'Pav. Concreto'): 1,
    ('Pav. Concreto', 'Pav. Intertravado'): 3,
    ('Pav. Concreto', 'Pav. Asfáltico'): 1/5,

    ('Pav. Intertravado', 'Via em Terra'): 3,
    ('Pav. Intertravado', 'Via em Cascalho/Brita'): 3,
    ('Pav. Intertravado', 'Paralelepípedo'): 1,
    ('Pav. Intertravado', 'Pav. Concreto'): 1/3,
    ('Pav. Intertravado', 'Pav. Intertravado'): 1,
    ('Pav. Intertravado', 'Pav. Asfáltico'): 1/3,

    ('Pav. Asfáltico', 'Via em Terra'): 9,
    ('Pav. Asfáltico', 'Via em Cascalho/Brita'): 7,
    ('Pav. Asfáltico', 'Paralelepípedo'): 5,
    ('Pav. Asfáltico', 'Pav. Concreto'): 5,
    ('Pav. Asfáltico', 'Pav. Intertravado'): 3,
    ('Pav. Asfáltico', 'Pav. Asfáltico'): 1,

}

C4 = ahpy.Compare(name='C4', comparisons=C4_comparisons, precision=3, random_index='saaty',iterations=100, tolerance=0.0001, cr=True)

print(C4.target_weights)
print(C4.consistency_ratio)

report = C4.report(show=True)

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


debug_linhas(C4)