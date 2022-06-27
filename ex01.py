#
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 1 - Programa que imprime a quantidade de números
# pares de 100 até 200, incluindo-os.
#
# usando o laço While
# entrada de dados
num = 100 # criar uma variável para armazenar o número inicial
contadorPares = 0 # criar uma variável para armazenar a quantidade de números pares entre 100 e 200
while num <= 200: # criar um laço para calcular a quantidade de números pares entre 100 e 200 incluindo-os
  if num % 2 == 0: # se o resto da divisão do número informado pelo usuário por 2 for igual a 0 (número par)
    contadorPares = contadorPares + 1 # incrementar a quantidade de números pares informados pelo usuário + 1
  num = num + 1 # ficar atento a identação do bloco para evitar um loop infinito
print(contadorPares) # imprimir a quantidade de números pares entre 100 e 200 incluindo-os
print("fim do programa")




###############################################################################
print("###############################################################################")

# usando o laço FOR:
# entrada de dados
quantidade = 0 # criar uma variável para armazenar a quantidade de números pares

# processamento de dados
for i in range(100, 201): # criar um laço para calcular a quantidade de números pares de 100 até 200
    if i % 2 == 0: # se o resto da divisão do número informado pelo usuário por 2 for igual a 0
        print(i) # imprimir o número informado pelo usuário
        quantidade += 1 # incrementar a quantidade de números pares informados pelo usuário
    else: # se o resto da divisão do número informado pelo usuário por 2 não for igual a 0 (número impar)
        continue # continuar o laço de repetição

# saida de dados
print(f"A quantidade de números pares de 100 até 200 é {quantidade}")
print("fim do programa")
