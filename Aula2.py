"""A Funcao print ela e utilizada pra exibir as coisas na tela 
e ela recebe algo chamado argumento, arguemnto e algo que voce
passa para funcao ou metodo"""

#Isso em ptython sao chamdas de argumentos nao nomeados
print(12, 34)
#O argumento sep significa separador e pode separar os argumentos nao noemados dos nomeados
print(12, 34, 1011, sep="-") # sep serve para informar o separador que voce quer
print(56, 78, sep="-", end='\n##\n')# O end significa quebra de linha ou serve para colocar algum caracter
print(9, 10, sep="-", end='\n')
print(9, 10, sep="-")

# \r\n -> CRLF (Somente para sistema Windows)
# \n -> LF (Somente para sistemas Linux ou Mac)