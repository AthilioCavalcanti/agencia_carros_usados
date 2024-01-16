class Carro:
    def __init__(
            self, 
            modelo: str, 
            marca: str, 
            tipo_carroceria: str, 
            ano: int, 
            cor: str, 
            preco: float, 
            quilometragem: int
        ) -> None:
        self.modelo = modelo
        self.marca = marca
        self.tipo_carroceria = tipo_carroceria
        self.ano = ano
        self.cor = cor
        self.preco = preco
        self.quilometragem = quilometragem

    def exibir_detalhes(self) -> None:
        pass

    def calcular_depreciacao(self) -> None:
        pass
