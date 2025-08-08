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
