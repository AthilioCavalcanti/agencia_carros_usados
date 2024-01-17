from datetime import datetime
from carro import Carro
from cliente import Cliente

class Transacao:
    def __init__(self, cliente: Cliente, carro: Carro, valor: float, data: datetime) -> None:
        self.cliente = cliente
        self.carro = carro
        self.valor = valor
        self.data = data

    def __str__(self) -> str:
        return f"{self.cliente.nome} comprou {self.carro} por R${self.carro.preco:.2f}"
    
    def data_transacao(self) -> str:
        return self.data.strftime("%d/%m/%Y %H:%M:%S")
