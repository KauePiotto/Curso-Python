#Aprendendo formatacao de Strings

nome = 'Kaue Piotto'
altura = 1.80
peso = 70
imc = peso / altura ** 2

# O f antes da String e chamado de f-strings (Formatacao de String)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa: {peso:.2f} quilos e seu IMC e '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)