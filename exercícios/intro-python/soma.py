"""
Programa simples para somar dois números
Autora: Paola Soares Machado
"""


def somar(num1: float, num2: float) -> float:
    """Retorna a soma de dois números."""
    return num1 + num2


if __name__ == "__main__":
    print("Vamos somar dois números?")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = somar(num1, num2)
        print(f"\n💋 A soma de {num1} + {num2} é {resultado}")
    except ValueError:
        print("❌ Digite números válidos, diva!")

# Feito com glitter e lógica por Paola 💋🎀
