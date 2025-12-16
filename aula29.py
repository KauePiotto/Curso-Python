"""
Introducao ao try e except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar

Mesma coisa do try/catch do java
"""

numero_str = input("vou dobrar o número que voce digitar: ")

try:
    numero_float= float(numero_str)
    print( 'FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print("Isso não é um número válido.")
    
#if numero_str.isdigit(): # Verifica se é um número inteiro positivo
#    numero_float= float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 
#else: 
#    print("Isso não é um número válido.")"""