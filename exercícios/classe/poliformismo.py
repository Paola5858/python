import math
class Forma:
    def calcular_area(self):
        raise NotImplementedError("Toda forma precisa saber calcular sua área!")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def imprimir_areas(formas):
    for f in formas:
        print(f"Área calculada: {f.calcular_area():.2f}")

formas = [
    Retangulo(5, 10),
    Circulo(7),
    Triangulo(6, 4)
]
imprimir_areas(formas)

# feito com glitter e lógica por Paola 💋🎀
