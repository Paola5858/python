"""
Mostrar a tabuada de um número de 1 a 10
Autora: Paola Soares Machado
"""


def mostrar_tabuada(numero: int) -> None:
    """Exibe a tabuada de um número de 1 a 10."""
    print(f"\n💋 Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


if __name__ == "__main__":
    print("Bora fazer a tabuada?")
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        mostrar_tabuada(numero)
    except ValueError:
        print("❌ Eita! Digite um número inteiro válido, diva!")

# Feito com glitter e lógica por Paola 💋🎀
