from dataclasses import dataclass

@dataclass
class Carro:
    modelo: str
    ano: int
    velocidade: int = 0  # valor padrão

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)

    def mostrar_velocidade(self):
        print(f"{self.modelo} está a {self.velocidade} km/h")


# Quando usar dataclass?
# A classe for usada para armazenar dados
# Você não precisa de muita lógica no __init__
# Quer manter o código mais limpo e legível
# ---------------------------------------------
# Quando não usar?
# Se sua classe tiver lógica complexa de inicialização
# Se você for trabalhar com herança mais sofisticada (há exceções, mas cuidado)
