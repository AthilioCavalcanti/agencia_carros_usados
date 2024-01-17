class Cliente:
    def __init__(self, nome: str, endereco: str, telefone: str) -> None:
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @property
    def telefone(self) -> str:
        return self._telefone
    
    def atualizar_endereco(self, novo_endereco: str) -> None:
        self._endereco = novo_endereco
    
    def atualizar_telefone(self, novo_numero: str) -> None:
        self._telefone = novo_numero
