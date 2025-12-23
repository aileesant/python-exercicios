#-- Imprima os números entre 1 e 100 que são divisíveis por 7 e 5 ao mesmo tempo
for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
#-------------------------------------------------------------------------------------

#-- Crie uma lista com todos os números pares entre 200 e 100 (em ordem decrescente)
pares = [i for i in range(200, 99, -1) if i % 2 == 0]
print(pares)
#------------------------------------------------------------------------

#-- Imprima todos os números primos entre 10 e 50
for num in range(10, 51):
    primo = True
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            primo = False
            break
    if primo:
        print(num)
#--------------------------------------------------------------------------------------       
#--Use range() para montar uma pirâmide de asteriscos com altura 5
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2*i - 1))

#--------------------------------------------------------------------------------------------    
#-- Mostre a soma dos quadrados dos números de 1 a 20
soma = 0
for i in range(1, 21):
    soma += i ** 2
print("Soma dos quadrados:", soma)

#----------------------------------------------------------------------------------------------
#-- Imprima uma contagem decrescente a partir de um número informado pelo usuário até 0
n = int(input("Digite um número: "))
for i in range(n, -1, -1):
    print(i)

#------------------------------------------------------------------------------------------    
#-- Gere uma sequência de Fibonacci com range() e for até o 10º termo
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
