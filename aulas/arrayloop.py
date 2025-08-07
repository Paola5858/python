"""testando arrays e listas"""
import array

nome = array.array('i', [1, 2, 3, 4, 5])

nome2 = ['a', 'b', 'c']

print(nome2[2])
print(nome[1])

teste = (1,2,3,4)
print(teste)

nome2.append('d')

print(nome2)
nome2.append('nome')
nome2.remove('b')
print(nome2)

print(len(nome))
print(nome.__len__())

for i in range(1,11):
    print(i)

for n in nome2:
    print(n)

for nn in nome:
    print(nn)
