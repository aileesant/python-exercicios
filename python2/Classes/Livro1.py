class Livro: 
    def __init__(self, titulo, autor): 
        self.titulo = titulo 
        self.autor = autor 
 
    def descrever(self): 
        print(f"'{self.titulo}', escrito por {self.autor}.") 
 
# Criando dois objetos 
livro1 = Livro("1984", "George Orwell") 
livro2 = Livro("Dom Casmurro", "Machado de Assis") 
 
# Chamando os métodos 
livro1.descrever() 
livro2.descrever() 
