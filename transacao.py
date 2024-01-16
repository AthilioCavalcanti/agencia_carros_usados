from datetime import datetime
from carro import Carro
from cliente import Cliente

class Transacao:
    def __init__(self, cliente: Cliente, carro: Carro, valor: float, data: datetime) -> None:
        self.cliente = cliente
        self.carro = carro
        self.valor = valor
        self.data = data
