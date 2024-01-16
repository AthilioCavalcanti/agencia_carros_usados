from typing import List
from carro import Carro
from transacao import Transacao
from cliente import Cliente

class Agencia:
    def __init__(self, nome: str) -> None:
        self.__nome: str = nome
        self._carros: List[Carro] = []
        self._transacoes: List[Transacao] = []
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    def adiciona_carro(self, carro: Carro) -> None:
        pass

    def vende_carro(self, carro: Carro, cliente: Cliente) -> None:
        pass

    def exibi_carros(self) -> None:
        pass

    def exibi_transacoes(self) -> None:
        pass
