import ahpy



C21_comparisons = {

    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 1,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 5,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 1/3,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 5,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1/3,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 3,
    ('Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/6,

    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 1/5,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 1,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 1/7,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 3,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1/7,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 1/4,
    ('Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/9,

    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 3,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 7,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 1,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 7,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1/2,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 5,
    ('Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/3,

    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 1/5,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 1/3,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 1/7,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 1,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1/7,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 1/3,
    ('Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/9,

    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 3,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 7,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 2,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 7,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 6,
    ('Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/3,

    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 1/3,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 4,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 1/5,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 3,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 1/6,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 1,
    ('Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1/7,

    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Rasteira de raízes rasas (Ex.: Amendoim-forrageiro, Trevos)'): 6,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Rasteira de raízes densas (Ex.: Braquiária, Vetiver, Capim-elefante)'): 9,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Arbustos de até 2m e raízes rasas (Ex: Buxinho, Pitósporo, Bérberis)'): 3,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Arbustos de até 2m e raízes profundas (Ex: Pinheiro rasteiro, Eleagno, Espirradeira)'): 9,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Árvores de raízes rasas (Ex: Bananeira, Palmeiras, Mangueiras)'): 3,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Árvores de Raízes Profundas (Ex: Inguá, Aroeira, Jacarandá, Pata-de-vaca)'): 7,
    ('Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)', 'Vegetação de Solo Exposto (Ex: Cana, Mamão, Capim Colonial)'): 1,

}


C21 = ahpy.Compare(name='A', comparisons=C21_comparisons, precision=3, random_index='saaty')

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
print(C21.target_weights)

print('\nCONSISTENCY RATIO')
print(C21.consistency_ratio)

debug_linhas(C21)



report = C21.report(show=True)