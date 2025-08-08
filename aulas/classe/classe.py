"""estudando classes em python"""

class Pessoa:
    """Classe que representa uma pessoa com nome e idade."""
    def __init__(self):
        self.nome = None
        self.idade = None

    def apresenta(self):
        """Exibe nome e idade da pessoa."""
        print(f"oiee meu nome é {self.nome} e tenho {self.idade} anos")


paola = Pessoa()
paola.nome = "Paola"
paola.idade = 17
paola.apresenta()


class Animal:
    """Classe que representa um animal com espécie e família."""
    def __init__(self, especie, familia):
        self.especie = especie
        self.familia = familia

    def apresenta(self):
        """Exibe informações sobre o animal."""
        print(f"essa espécie: {self.especie}. é dessa familia: {self.familia}")


cachorro = Animal("canis familiaris", "canidae")
cachorro.apresenta()

