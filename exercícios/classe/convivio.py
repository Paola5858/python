"""
Interface e abstração: pessoas do meu convívio
Autora: Paola Soares Machado
"""
from abc import ABC, abstractmethod


class PessoaConvivio(ABC):
    """Interface (modelo para quem eu curto conviver)."""
    
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @abstractmethod
    def vibe(self) -> str:
        """Cada pessoa tem sua vibe única."""
        pass

    @abstractmethod
    def rolê_favorito(self) -> str:
        """O que essa pessoa ama fazer no tempo livre."""
        pass


class MelhorAmigo(PessoaConvivio):
    """Representa o melhor amigo."""
    
    def vibe(self) -> str:
        return f"{self._nome} ({self._idade}) sempre chega com piada interna e me faz esquecer os problemas. 😂"

    def rolê_favorito(self) -> str:
        return f"{self._nome} ama pedir lanche de madrugada e filosofar sobre a vida."


class ParceiroEstudos(PessoaConvivio):
    """Representa o parceiro de estudos."""
    
    def vibe(self) -> str:
        return f"{self._nome} ({self._idade}) é aquele que me lembra que a prova tá chegando. 😅"

    def rolê_favorito(self) -> str:
        return f"{self._nome} prefere maratonar cafés comigo na biblioteca e revisar junto."


if __name__ == "__main__":
    print("\n💋 Convívio:\n")
    
    amigo = MelhorAmigo("Major", 17)
    parceiro = ParceiroEstudos("Squeruque", 18)

    print(amigo.vibe())
    print(amigo.rolê_favorito())
    print()
    print(parceiro.vibe())
    print(parceiro.rolê_favorito())

# Feito com glitter e lógica por Paola 💋🎀
