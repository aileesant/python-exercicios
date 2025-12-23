# Serve para reduzir o código repetitivo (como __init__, __repr__, etc.) quando queremos apenas guardar dados em uma classe.

# sem dataclass :(
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# COM data class  :)
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

# Isso já cria automaticamente: __init__, __repr__, __eq__ (comparação) e muito mais!
