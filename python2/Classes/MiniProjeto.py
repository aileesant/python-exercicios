# Crie uma classe Carro com atributos como modelo, ano e velocidade atual.
# Inclua métodos acelerar(), frear() e mostrar_velocidade().

class Carro: 
    def __init__(self, modelo, ano): 
        self.modelo = modelo 
        self.ano = ano 
        self.velocidade = 0  # Começa parado 
 
    def acelerar(self): 
        self.velocidade += 10 
        print(f"{self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h") 
 
    def frear(self): 
        self.velocidade = max(0, self.velocidade - 10) 
        print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h") 
 
    def mostrar_velocidade(self): 
        print(f"{self.modelo} está a {self.velocidade} km/h") 
 
# Exemplo de uso 
carro1 = Carro("Civic", 2020) 
carro1.acelerar() 
carro1.acelerar() 
carro1.frear() 
carro1.mostrar_velocidade() 
 
