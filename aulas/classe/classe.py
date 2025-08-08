"""estudando classes em python"""
class Pessoa:
    nome = None
    idade = None

    def apresenta(self):
        print(f"Oiee meu nome é {self.nome} e tenho {self.idade} anos")

        Paola = Pessoa()
        Paola.nome = "Paola"
        Paola.idade = 17
        Paola.apresenta()

        class Animal:
            def __init__(self, especie, familia):
                self.especie = especie
                self.familia = familia
            def apresenta(self):
                print(f"Essa espécie: {self.especie}. É dessa familia: {self.familia}")

cachorro = Animal("canis familiaris", "canidae")
cachorro.apresenta()
