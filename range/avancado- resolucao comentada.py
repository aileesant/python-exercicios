#Imprimir números de 1 a 100 divisíveis por 7 e 5 ao mesmo tempo

for i in range(1, 101):                      # Percorre os números de 1 até 100 (inclusive)
    if i % 7 == 0 and i % 5 == 0:            # Verifica se o número é divisível por 7 e por 5
        print(i)                             # Se for, imprime o número

---------------------------------------------------------------------------------------------------------

#Criar lista com números pares de 200 a 100 (ordem decrescente)

pares = [i for i in range(200, 99, -1) if i % 2 == 0]  # Cria uma lista com números pares de 200 até 100
print(pares)                                           # Imprime a lista com os números pares


------------------------------------------------------------------------------------------------------------------

#Imprimir números primos entre 10 e 50

for num in range(10, 51):                           # Percorre os números de 10 a 50 (inclusive)
    primo = True                                    # Assume que o número é primo
    for div in range(2, int(num ** 0.5) + 1):       # Testa divisores de 2 até a raiz quadrada do número
        if num % div == 0:                          # Se o número for divisível por algum deles...
            primo = False                           # ...então ele não é primo
            break                                   # Interrompe o laço de divisores
    if primo:                                       # Se ainda for primo depois da verificação...
        print(num)                                  # ...imprime o número

---------------------------------------------------------------------------------------------
#Montar pirâmide de asteriscos com altura 5

for i in range(1, 6):                               # Controla o número da linha (1 a 5)
    print(" " * (5 - i) + "*" * (2*i - 1))           # Imprime espaços + asteriscos para formar a pirâmide

# * `" " * (5 - i)`: Espaços à esquerda para alinhar
# * `"*" * (2*i - 1)`: Número ímpar de asteriscos por linha

------------------------------------------------------------------------------------------------

#Somar os quadrados dos números de 1 a 20

soma = 0                                            # Inicializa a variável acumuladora
for i in range(1, 21):                              # Percorre os números de 1 a 20
    soma += i ** 2                                  # Soma o quadrado de cada número à variável
print("Soma dos quadrados:", soma)                 # Imprime o resultado da soma

------------------------------------------------------------------------------------------------

#Contagem regressiva a partir de um número informado

n = int(input("Digite um número: "))               # Pede ao usuário um número e converte para inteiro
for i in range(n, -1, -1):                         # Faz contagem regressiva de n até 0
    print(i)                                       # Imprime cada número da contagem
-------------------------------------------------------------------------------------------

#Sequência de Fibonacci até o 10º termo**

a, b = 0, 1                                        # Inicializa os dois primeiros termos da sequência
for _ in range(10):                                # Executa o loop 10 vezes
    print(a, end=" ")                              # Imprime o termo atual (a), na mesma linha
    a, b = b, a + b                                # Atualiza os termos: a vira b, b vira a+b (próximo termo)
