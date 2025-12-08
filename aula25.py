# Aprendendo sobre  interpolacao de strings com %

"""
Interpolação basica de strings
s - String
d e i - int
f - float
x e X - Hexadecimal (ABCDEF5885858) 
"""

nome = 'Luiz'
preco = 1000.95897634
variavel = '%s, o preco total foi R$ %.2f %s' % (nome, preco, 'reais')
print(variavel)
print('O hexadecimal de %d e %08X' % (1500, 1500))
