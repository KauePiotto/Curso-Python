# Aprendendo sobre o operador logico AND

# Operador logico
# AND (E) or (OU) not (NAO)
# and - Todas as condicoes precisam ser 
# verdadeiras para retornar True
# Se qualquer valor for considerado falso,
# a expressao toda sera avaliada naquele valor
# Sao considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Tambem existe o tipo None que e 
# usado para representar um nao valor

# Exemplo de uso do AND
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_confirmada = '123456'

if entrada == 'E' and senha_digitada == senha_confirmada:
   print('Entrar')
else:
   print('Sair')

# Avalicao de curto circuito
print(True and False and True)  
print(True and 0 and True)

# Uma string vazia e considerada como false