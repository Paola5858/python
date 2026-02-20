"""
Oi lindaaa, me diz 10 números aí e vou mostrar só os pares, tá?
Autora: Paola Soares Machado
"""
from typing import List


def ler_numeros(quantidade: int) -> List[int]:
    """Lê uma quantidade de números do usuário."""
    numeros = []
    for i in range(quantidade):
        while True:
            try:
                num = int(input(f" Digita o {i + 1}º número: "))
                numeros.append(num)
                break
            except ValueError:
                print("❌ Precisa ser um número inteiro, gata!")
    return numeros


def filtrar_pares(numeros: List[int]) -> List[int]:
    """Retorna apenas os números pares de uma lista."""
    return [num for num in numeros if num % 2 == 0]


if __name__ == "__main__":
    numeros = ler_numeros(10)
    pares = filtrar_pares(numeros)
    
    print("\n💋 Olha só os números pares que você mandou:")
    if pares:
        for num in pares:
            print(f"💋 {num}")
    else:
        print("Nenhum número par encontrado!")

# Feito com glitter e lógica por Paola 💋🎀
