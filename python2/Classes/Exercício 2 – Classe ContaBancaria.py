class ContaBancaria: 
    def __init__(self, titular, saldo): 
        self.titular = titular 
        self.saldo = saldo 
 
    def depositar(self, valor): 
        self.saldo += valor 
 
    def sacar(self, valor): 
        if self.saldo >= valor: 
            self.saldo -= valor 
            return True 
        else: 
            return False 
 
    def mostrar_saldo(self): 
        print(f"{self.titular}, seu saldo é R${self.saldo}") 
  
