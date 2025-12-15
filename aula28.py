# Exercicio 4 para testa conhecimento

"""
Exercicio 
Peca ao usuario para digitar seu nome
peca ao usuario para digitar sua idade
Se o nome e idade forem digitados:
     Exiba:
        Seu nome e {nome}
        Seu nome invertido e {nome invertido}
        Seu nome contem (ou nao) espacos
        Seu nome tem {n} letras
        A primeira letra do seu nome e {letra}
        A ultima letra do seu nome e {letra}
Se nada for digitado em nome ou idade: 
    Exiba:
      "Desculpa, voce deixou campos vazios."
"""
entrada_nome = input('Digite seu nome: ').strip()
entrada_idade = input('Digite sua idade: ').strip()


if(entrada_nome and entrada_idade):
    nome_invertido = entrada_nome[::-1]
    contem_espacos = 'sim' if ' ' in entrada_nome else 'nao'
    numero_letras = len(entrada_nome.replace(' ', ''))
    primeira_letra = entrada_nome[0]
    ultima_letra = entrada_nome[-1]

    print(f'Seu nome e {entrada_nome}')
    print(f'Seu nome invertido e {nome_invertido}')
    print(f'Seu nome contem espacos? {contem_espacos}')
    print(f'Seu nome tem {numero_letras} letras')
    print(f'A primeira letra do seu nome e {primeira_letra}')
    print(f'A ultima letra do seu nome e {ultima_letra}')
else:
    print('Desculpa, voce deixou campos vazios.')