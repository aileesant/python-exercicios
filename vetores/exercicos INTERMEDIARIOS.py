#-- Crie uma lista com 10 números aleatórios e mostre apenas os maiores que 5

numeros = [3, 7, 1, 9, 4, 5, 11, 6, 2, 10]
for n in numeros:
    if n > 5:
        print(n)

#---------------------------------------------------------------

#-- Receba 5 nomes do usuário e armazene em uma lista

nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
print(nomes)

#--------------------------------------------------------------------

#-- Conte quantas vezes um número específico aparece em uma lista

numeros = [2, 5, 3, 5, 7, 5, 1]
print(numeros.count(5))  # Aparece 3 vezes

#--------------------------------------------------------------------

#-- Receba 5 números do usuário e imprima a média

numeros = []
for i in range(5):
    n = int(input("Número: "))
    numeros.append(n)
media = sum(numeros) / len(numeros)
print("Média:", media)

#---------------------------------------------------------------------

#-- Crie uma função que retorna o maior número de uma lista

def maior(lista):
    maior_valor = lista[0]
    for num in lista:
        if num > maior_valor:
            maior_valor = num
    return maior_valor

print(maior([10, 30, 2, 8, 40]))

#---------------------------------------------------------------------------------
#-- Inverta a lista manualmente (sem usar [::-1] nem reverse())

lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(lista)-1, -1, -1):
    invertida.append(lista[i])
print(invertida)

#------------------------------------------------------------------------------------------

#--Receba 5 produtos do usuário e mostre todos em ordem alfabética

produtos = []
for i in range(5):
    produto = input("Produto: ")
    produtos.append(produto)
produtos.sort()
print(produtos)
