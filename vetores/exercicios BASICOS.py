#-- Crie uma lista com 5 nomes e imprima todos
nomes = ["Ana", "Bruno", "Carlos", "Duda", "Edu"]
for nome in nomes:
    print(nome)   
    
#--- Adicione mais um nome à lista com append()
nomes.append("Fernanda")

#-- Substitua o segundo nome por outro
nomes[1] = "Beatriz"

#-- Remova o último nome da lista
nomes.pop()  # ou nomes.pop(-1)

#-- Imprima os nomes usando um for
for nome in nomes:
    print(nome)
