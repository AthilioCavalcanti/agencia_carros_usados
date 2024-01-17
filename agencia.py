from typing import List
import datetime
from carro import Carro
from transacao import Transacao
from cliente import Cliente

class Agencia:
    def __init__(self, nome: str) -> None:
        self.__nome: str = nome
        self._carros: List[Carro] = [] # Pode ser legal um dict com as placas como keys
        self._transacoes: List[Transacao] = []
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    def adiciona_carro(self, carro: Carro) -> None: 
        if carro in self._carros:
            raise ValueError("Impossível adicionar! O carro já está na agência.")
        else:
            # Levanta erro se a placa já existir entre os carros da agência
            for carro_agencia in self._carros:
                if carro_agencia.placa == carro.placa:
                    raise ValueError("Impossível adicionar! A placa do carro já está cadastrada")
                
            # Se não tiver erro o carro é adicionado
            self._carros.append(carro)

    def vende_carro(self, carro: Carro, cliente: Cliente) -> None:
        if carro in self._carros:
            transacao = Transacao(cliente, carro, carro.preco, datetime.datetime.now())
            self._transacoes.append(transacao)
            self._carros.remove(carro)

        else:
            raise ValueError("Impossível realizar a venda! A agência não possuí o carro.")

    def exibi_carros(self) -> None:
        print("Lista de carros disponíveis:")
        if len(self._carros):
            for carro in self._carros:
                print(f"* {carro}")
        else:
            print("Não há carros disponíveis para venda")

    def exibi_transacoes(self) -> None:
        print("Histórico de transações:")
        if len(self._transacoes):
            for transacao in self._transacoes:
                print(f"* {transacao}")
        else:
            print("Nenhuma transação foi realizada")

    def carregar_dados(self) -> None:
        pass


# Testes
if __name__ == "__main__":
    minha_agencia = Agencia("Boole Carros")
    carro_1 = Carro("BOO0L00", "Accord", "Honda", "Sedan", 2018, "Preto", "Álcool/Gasolina (Flex)", 170600.0, 65000)
    cliente_1 = Cliente("Fulano", "Rua dos Bobos, 00", "(00)00000-0000")

    minha_agencia.adiciona_carro(carro_1)
    minha_agencia.exibi_carros()
    minha_agencia.exibi_transacoes()
    print()
    minha_agencia._carros[0].exibir_detalhes()
    print()

    minha_agencia.vende_carro(carro_1, cliente_1)
    minha_agencia.exibi_carros()
    minha_agencia.exibi_transacoes()
