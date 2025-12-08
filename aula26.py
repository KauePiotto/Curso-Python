# Aprendendo sobre formatacao de strings com f-strings

"""
Formatacao basica de strings
s - String
d e i - int
f - float
.<numero de digitos>f
x e X - Hexadecimal (ABCDEF5885858) 
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Forca o numero a aparece antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.344534543543:+10,.1f}')
print(f'O hexadecimal de 1500 e {1500:08X}')
print(f'{variavel!r}')
