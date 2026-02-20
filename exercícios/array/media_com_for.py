"""
Oii gataa! Bora calcular a média de notas?
Autora: Paola Soares Machado
"""
from typing import List


def calcular_media_com_for(notas: List[float]) -> float:
    """Calcula a média de uma lista de notas usando for."""
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


if __name__ == "__main__":
    notas = [8, 7.5, 10, 6, 9]
    media = calcular_media_com_for(notas)
    print(f"💋 A média dessas notas babadeiras foi: {media:.2f}")

# Feito com glitter e lógica por Paola 💋🎀
