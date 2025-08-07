"""Programa para perguntar nome, sexo e calcular anos para aposentadoria."""

NONE = "none"

print("Oii gata")

none = input("Digite seu nome: ")

print(f"Tudo bem, {none}?")

sexo = input("Qual é o seu sexo? (M/F): ").strip().upper()

if sexo == "M":
    print("Você é um homem.")
elif sexo == "F":
    print("Você é uma mulher.")
else:
    print("Sexo inválido.")

print("Vamos falar sobre aposentadoria.")
APOSENTA = 65
idade = int(input("Quantos anos você tem? "))
tempoaposenta = APOSENTA - idade
print(f"Faltam {tempoaposenta} anos para você se aposentar.")

print("Obrigado por usar o programa!")
