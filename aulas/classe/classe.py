"""
Estudando classes em Python
Autora: Paola Soares Machado
"""


class Pessoa:
    """Classe que representa uma pessoa com nome e idade."""
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        """Exibe nome e idade da pessoa."""
        print(f"💋 Oiee meu nome é {self.nome} e tenho {self.idade} anos")
    
    def __str__(self) -> str:
        return f"Pessoa(nome={self.nome}, idade={self.idade})"


class Animal:
    """Classe que representa um animal com espécie e família."""
    
    def __init__(self, especie: str, familia: str):
        self.especie = especie
        self.familia = familia

    def apresentar(self) -> None:
        """Exibe informações sobre o animal."""
        print(f"💋 Essa espécie: {self.especie} é dessa família: {self.familia}")
    
    def __str__(self) -> str:
        return f"Animal(espécie={self.especie}, família={self.familia})"


if __name__ == "__main__":
    print("\n💋 Testando classes:\n")
    
    paola = Pessoa("Paola", 17)
    paola.apresentar()
    
    cachorro = Animal("Canis familiaris", "Canidae")
    cachorro.apresentar()

# Feito com glitter e lógica por Paola 💋🎀
