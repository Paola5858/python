"""Programa para demonstrar o uso de classes e herança em Python."""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

    meu_cachorro = Cachorro()
    meu_gato = Gato()
    print(meu_cachorro.falar())  # Saída: Au Au
    print(meu_gato.falar())      # Saída: Miau
