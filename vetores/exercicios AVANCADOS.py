#-- Crie uma função que remova elementos duplicados de uma lista sem usar set()
def remover_duplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

print(remover_duplicatas([1, 2, 2, 3, 4, 3, 5]))

#---------------------------------------------------------------------------------------

#-- Ordene uma lista manualmente (sem sort() ou sorted()) usando Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(bubble_sort([5, 2, 9, 1, 5, 6]))

#--------------------------------------------------------------------------------------

#-- Receba 10 números e diga qual a moda (número que mais se repete)
numeros = []
for _ in range(10):
    n = int(input("Número: "))
    numeros.append(n)

moda = max(numeros, key=numeros.count)
print("Moda:", moda)

#-----------------------------------------------------------------------------------------------------

#--- Implemente uma função que rotacione os elementos de uma lista uma posição à direita
def rotacionar_direita(lista):
    return [lista[-1]] + lista[:-1]

print(rotacionar_direita([1, 2, 3, 4]))  # [4, 1, 2, 3]

#-------------------------------------------------------------------------------------------------

#-- Crie uma matriz 3x3 e imprima a soma de cada linha
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    print("Soma da linha:", sum(linha))

#-------------------------------------------------------------------------------------------------

#-- Crie uma função que inverta as palavras de uma frase e as armazene em uma lista
def inverter_frase(frase):
    palavras = frase.split()
    return palavras[::-1]

print(inverter_frase("Eu gosto de Python"))  # ['Python', 'de', 'gosto', 'Eu']

#-------------------------------------------------------------------------------------------------

#-- Calcule a média dos elementos pares de uma lista
lista = [10, 3, 8, 7, 12, 5]
pares = [n for n in lista if n % 2 == 0]
media = sum(pares) / len(pares)
print("Média dos pares:", media)
