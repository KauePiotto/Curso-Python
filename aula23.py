# Aprendendo sobre operadore lógico NOT (nao)

# Operador lógico "not"
# Usado para inverter expressões booleanas
# not True  -> False
# not False -> True

senha = input('Senha: ')

if not senha == "123456":
    print('Voce nao digitou nada')
else:
    print('Voce digitou a senha correta')

print(not True)  # False
print(not False) # True


