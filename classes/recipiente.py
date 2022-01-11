class Recipiente:
    def __init__(self, tamanho):
        self.tamanho: float = tamanho if tamanho > 0 else 0
        self.conteudo: float = 0
        self.limpo: bool = True

    def esvaziar(self) -> None:
        self.conteudo = 0
    
    def esta_vazio(self) -> bool:
        return True if self.conteudo == 0 else False
    
    def lavar(self) -> None:
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self) -> bool:
        return self.limpo
    
    def estado(self) -> str:
        return "limpo" if self.limpo else "sujo"
    
    def sujar(self) -> None:
        self.limpo = False
    
    def __repr__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"
    
    def __str__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"