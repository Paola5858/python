"""
Hora da tabuada, gata!
Autora: Paola Soares Machado
"""


def tabuada_com_for(numero: int) -> None:
    """Mostra a tabuada usando for."""
    print(f"\n💋 A tabuada de {numero} é essa aqui ó:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    try:
        numero = int(input("Me diz um número pra eu te mostrar a tabuada mais chique da aula: "))
        tabuada_com_for(numero)
    except ValueError:
        print("❌ Precisa ser um número inteiro, diva!")

# Feito com glitter e lógica por Paola 💋🎀
