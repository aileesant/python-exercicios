# E se quisermos ligar os dados da mesma pessoa de forma mais organizada?

class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
 
    def apresentar(self): 
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.") 
 
# Criando objetos Pessoa 
pessoa1 = Pessoa("Ana", 25) 
pessoa2 = Pessoa("Lucas", 30) 
 
# Chamando o método 
pessoa1.apresentar() 
pessoa2.apresentar() 
