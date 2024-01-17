from carro import Carro


class CarroCombustao(Carro):
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
            quilometragem: int
        ) -> None:
        super().__init__(placa, modelo, marca, tipo_carroceria, ano, cor, tipo_combustivel, preco, quilometragem)
