"""calcula a média de duas notas e mostra se o aluno foi aprovado ou reprovado"""

# feito com glitter e lógica por @paolakskj 💋

print("Vamos calcular a média de duas notas?")
# Pede as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra a média
print(f"\nA média do aluno é: {media:.2f}")

# Verifica se aprovado ou reprovado
if media >= 7:
    print("💖 APROVADO! Parabéns diva!")
else:
    print("💔 REPROVADO! Não desanime, continue estudando!")
