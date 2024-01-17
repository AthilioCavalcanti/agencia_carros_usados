from carro import Carro
from datetime import datetime


class CarroHibrido(Carro):
    def __init__(
            self, 
            placa: str,
            modelo: str, 
            marca: str, 
            tipo_carroceria: str, 
            ano: int, 
            cor: str, 
            tipo_combustivel: str, 
            preco: float, 
            quilometragem: int,
            capacidade_bateria: float
        ) -> None:
        super().__init__(placa, modelo, marca, tipo_carroceria, ano, cor, tipo_combustivel, preco, quilometragem)
        self.capacidade_bateria = capacidade_bateria
        self.saude_bateria = 100 - ((datetime.now().year - self.ano) *  0.25)

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes()
        print(
            f"Capacidade da bateria: {self.capacidade_bateria}kWh\n" +
            f"Saúde da bateria: {self.saude_bateria:.2f}%"
        )


# Testes
if __name__ == "__main__":
    carro_2 = CarroHibrido("BOO1L11","Compass S 4xe", "Jeep", "SUV", 2024, "Azul", "Eletricidade/Gasolina", 347300.0, 5000, 60.5)
    print(carro_2.saude_bateria)
    carro_2.exibir_detalhes()
