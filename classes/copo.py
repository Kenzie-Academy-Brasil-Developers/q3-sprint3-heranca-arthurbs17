from classes import Recipiente
from typing import Union

class Copo(Recipiente):
    def __init__(self, tamanho: float):
        super().__init__(tamanho)

    def encher(self, bebida: str = 'água') -> Union[str, None]:
        if self.limpo:
            self.conteudo = self.tamanho
            self.bebida = bebida
            self.sujar()
        else:
            return "Não se pode encher um copo sujo"
    
    def beber(self, quantidade: float) -> Union[str, None]:
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade
    
    def lavar(self) -> None:
        super().lavar()
        self.bebida = None

    def __repr__(self) -> str:
        if self.esta_vazio():
            return f"Um copo vazio de {self.tamanho:.1f}ml"
        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"

    def __str__(self) -> str:
        if self.esta_vazio():
            return f"Um copo vazio de {self.tamanho:.1f}ml"
        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"