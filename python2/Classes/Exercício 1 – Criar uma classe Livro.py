class Livro: 
    def __init__(self, titulo, autor): 
        self.titulo = titulo 
        self.autor = autor 
 
    def descrever(self): 
        print(f"'{self.titulo}', escrito por {self.autor}.") 

# crie dois livros e chame-os de formas diferentes
