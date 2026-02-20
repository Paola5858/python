"""
Calcula a média de duas notas e mostra se o aluno foi aprovado ou reprovado
Autora: Paola Soares Machado
"""


def calcular_media(nota1: float, nota2: float) -> float:
    """Calcula a média de duas notas."""
    return (nota1 + nota2) / 2


def verificar_aprovacao(media: float) -> None:
    """Verifica se o aluno foi aprovado ou reprovado."""
    print(f"\nA média do aluno é: {media:.2f}")
    if media >= 7:
        print("💖 APROVADO! Parabéns diva!")
    else:
        print("💔 REPROVADO! Não desanime, continue estudando!")


if __name__ == "__main__":
    print("Vamos calcular a média de duas notas?")
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = calcular_media(nota1, nota2)
        verificar_aprovacao(media)
    except ValueError:
        print("❌ Eita! Digite números válidos, gata!")

# Feito com glitter e lógica por Paola 💋🎀
