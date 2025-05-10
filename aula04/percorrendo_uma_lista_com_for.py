# Exemplo das frutas
frutas = ["maçã", "banana", "laranja", "morango"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
    
print('\n')
    
# Forma correta
caixa = 0
for i in range(1,11):
  caixa += i
  print(caixa)
print(caixa)

print('\n')

# Erro de lógica
caixa1 = 0
for i in range(1,11):
  i += caixa1
  print(i)
print(i)

print('\n')

# Tabuada
numero = int(input('Digite um número inteiro: '))
tabuada = []
resultado = 0

for i in range(1, 11):
  resultado = numero * i
  tabuada.append(resultado)
print(f'Tabuada: {tabuada}')

print('\n')

# Números pares de 1 à 20
lista = []

for i in range(0, 21, 2):
  lista.append(i)

print(lista)

print('\n')

# Contagem regressiva com for
for i in range(10, 0, -1):
  print(i)
  
print('\n')
  
# Contagem regressiva com while
numero = 10

while numero > 0:
  print(numero)
  numero -= 1