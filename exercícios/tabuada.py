"""mostrar a tabuada de um número de 1 a 10"""

# Feito com glitter e lógica por @paolakskj 💋

print("Bora fazer a tabuada?")
# Pede o número
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")

# Loop de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
