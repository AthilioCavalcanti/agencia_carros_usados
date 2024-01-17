class Carro:
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
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.tipo_carroceria = tipo_carroceria
        self.ano = ano
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self._preco = preco
        self._quilometragem = quilometragem

    @property
    def preco(self) -> float:
        return self._preco

    def exibir_detalhes(self) -> None:
        print(
            "----------------------\n" +
            "Informações do veículo\n" +
            "----------------------\n" +
            f"Placa: {self.placa}\n" +
            f"Modelo: {self.modelo}\n" +
            f"Marca: {self.marca}\n" + 
            f"Ano: {self.ano}\n" + 
            f"Cor: {self.cor}\n"
            f"Tipo de carroceria: {self.tipo_carroceria}\n" +
            f"Tipo de combustível: {self.tipo_combustivel}\n" +
            f"Quilometragem: {self._quilometragem}km\n" +
            f"Preço: R$ {self._preco:.2f}"
        )

    def atualizar_preco(self, novo_preco) -> None:
        self._preco = novo_preco

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo}, {self.ano}, {self.cor}"
    