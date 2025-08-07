"""oi lindaaa, agora me diz 10 números aí e vou mostrar só os pares, tá?"""

numeros = []

for i in range(10):
    num = int(input(f" digita o {i + 1}º número: "))
    numeros.append(num)

print("\n olha só os números pares que você mandou:")
for num in numeros:
    if num % 2 == 0:
        print(f"💋 {num}")
