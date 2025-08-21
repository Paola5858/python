from abc import ABC, abstractmethod

# interface (modelo para quem eu curto conviver)
class PessoaConvivio(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @abstractmethod
    def vibe(self):
        """Cada pessoa tem sua vibe única."""
        pass

    @abstractmethod
    def rolê_favorito(self):
        """O que essa pessoa ama fazer no tempo livre."""
        pass


# classe 1 - melhor amiga
class MelhorAmigo(PessoaConvivio):
    def vibe(self):
        return f"{self._nome} ({self._idade}) sempre chega com piada interna e me faz esquecer os problemas. 😂"

    def rolê_favorito(self):
        return f"{self._nome} ama pedir lanche de madrugada e filosofar sobre a vida."

# classe 2 - parceira de Estudos
class ParceiroEstudos(PessoaConvivio):
    def vibe(self):
        return f"{self._nome} ({self._idade}) é aquele que me lembra que a prova tá chegando. 😅"

    def rolê_favorito(self):
        return f"{self._nome} prefere maratonar cafés comigo na biblioteca e revisar junto."


# testando
if __name__ == "__main__":
    amigo = MelhorAmigo("major", 17)
    parceiro = ParceiroEstudos("squeruque", 18)

    print("- Convívio\n")
    print(amigo.vibe())
    print(amigo.rolê_favorito())
    print()
    print(parceiro.vibe())
    print(parceiro.rolê_favorito())
