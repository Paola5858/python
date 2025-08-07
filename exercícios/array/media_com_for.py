""" oii gataa! bora calcular a média de 5 notas? """

notas = [8, 7.5, 10, 6, 9]
SOMA = 0

for nota in notas:
    SOMA += nota

MEDIA = SOMA / len(notas)
print(f"🎓 A média dessas notas babadeiras foi: {MEDIA}")
