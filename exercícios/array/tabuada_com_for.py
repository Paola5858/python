"""hora da tabuada, gata!"""

numero = int(input("me diz um número pra eu te mostrar a tabuada mais chique da aula: "))

print(f"\n💋 a tabuada de {numero} é essa aqui ó:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
