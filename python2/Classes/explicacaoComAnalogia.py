# Imagine que classe é uma forma de bolo e objeto é o bolo feito a partir dessa forma.
# Todos os bolos feitos a partir da mesma forma têm o mesmo formato,
# mas cada um pode ter recheio e cobertura diferentes (dados diferentes). 

class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
 
    def apresentar(self): 
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.") 
  


# class define a forma 

# __init__ é o que acontece quando o bolo é assado (criação do objeto) 

# self é o próprio objeto (a instância) 

# self.nome guarda o valor dentro do objeto 
