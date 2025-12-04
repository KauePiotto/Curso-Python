# Aprendendo a formatar String com o metodo format

a = 'AA'
b = 'B'
c = 1.1

string = 'b = {nome2} a = {nome1} a = {nome1} C = {nome3:.2f}'
formato = string.format(nome1 = a,nome2= b, nome3 = c)

print(formato)