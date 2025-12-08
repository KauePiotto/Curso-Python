# Aprendendo sobre operadores lógicos IN e NOT IN

# Operadores lógicos "in" e "not in"
# Strings sao iteraveis
# 0 1 2 3 4 5
# O T A V I O
# -6-5-4-3-2-1

nome = 'Otavio'

#print(nome[2])
#print(nome[-4])  

# Operador in
print('vio' in nome) # True
print('zero' in nome) # False

print(10 * '-')

# Operador not in
print('zero' not in nome) # True
print('vio' not in nome) # False   

print(10 * '-')

# Exemplo de uso prático
nome = input('Digite seu nome: ')
encontar = input ('Digite o que deseja encontrar: ')

if encontar in nome:
    print(f'Encontrado {encontar} em {nome}')
else:
    print(f'{encontar} nao esta em {nome}')