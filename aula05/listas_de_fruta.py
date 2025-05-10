# Criando a lista de frutas
frutas = ['maçã', 'banana', 'uva', 'laranja']

print(frutas[0]) # Saída: maçã
print(frutas[2]) # Saída: uva
print(frutas[-1]) # Saída: laranja | colocamos -1 pois -0 não existe
print(frutas[-3]) # Saída: banana

# "-1 é sempre o último item"

# Acrescentando um item ao final da lista frutas
frutas.append('kiwi')

print(len(frutas))

print(frutas)

# Percorrendo a lista de frutas
for i in frutas:
  print(i)


print(frutas[0])