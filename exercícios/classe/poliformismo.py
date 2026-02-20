"""
Polimorfismo: um mesmo método, comportamentos diferentes
Autora: Paola Soares Machado
"""
import math
from typing import List


class Forma:
    """Classe base para formas geométricas."""
    
    def calcular_area(self) -> float:
        raise NotImplementedError("Toda forma precisa saber calcular sua área!")


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> float:
        return self.largura * self.altura
    
    def __str__(self) -> str:
        return f"Retângulo ({self.largura}x{self.altura})"


class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)
    
    def __str__(self) -> str:
        return f"Círculo (raio {self.raio})"


class Triangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
    
    def __str__(self) -> str:
        return f"Triângulo (base {self.base}, altura {self.altura})"


def imprimir_areas(formas: List[Forma]) -> None:
    """Demonstra polimorfismo: mesmo método, comportamentos diferentes."""
    for forma in formas:
        print(f"{forma} → Área: {forma.calcular_area():.2f}")


if __name__ == "__main__":
    formas = [
        Retangulo(5, 10),
        Circulo(7),
        Triangulo(6, 4)
    ]
    print("💋 Calculando áreas com polimorfismo:\n")
    imprimir_areas(formas)

# Feito com glitter e lógica por Paola 💋🎀
