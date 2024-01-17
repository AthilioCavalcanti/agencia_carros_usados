from carro import Carro
from datetime import datetime


class CarroEletrico(Carro):
    def __init__(
            self, 
            placa: str,
            modelo: str, 
            marca: str, 
            tipo_carroceria: str, 
            ano: int, 
            cor: str, 
            preco: float, 
            quilometragem: int, 
            capacidade_bateria: float
        ) -> None:
        super().__init__(placa, modelo, marca, tipo_carroceria, ano, cor, "Eletricidade", preco, quilometragem)
        self.capacidade_bateria = capacidade_bateria
        self.saude_bateria = 100 - ((datetime.now().year - self.ano) *  0.223)

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes()
        print(
            f"Capacidade da bateria: {self.capacidade_bateria}kWh\n" +
            f"Saúde da bateria: {self.saude_bateria:.2f}%"
        )


# Testes
if __name__ == "__main__":
    carro_3 = CarroEletrico("BOO2L22", "Dolphin", "BYD", "Hatch", 2024, "Branco", 179800.0, 5000, 60.5)
    print(carro_3.saude_bateria)
    carro_3.exibir_detalhes()
