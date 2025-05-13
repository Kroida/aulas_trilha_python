# Compreensão de lista
numeros = list(range(1, 11))

# Expressão # Iterador # Iteravel # Condição
quadrados = [numero ** 2 for numero in numeros]  # if numero % 2 == 0

print(quadrados)
print(numeros)



# Lista achatada
matriz = [[1, 2], [3, 4], [5, 6]]

lista_achatada = [num for sublista in matriz for num in sublista]
 # Resultado: [1, 2, 3, 4, 5, 6]
print(matriz)
print(lista_achatada)



# Matriz
matriz = [[1, 2], [3, 4], [5, 6]]

for i in range(len(matriz)):
  for j in range(len(matriz[0])): # Retorna o número de elementos na primeira sublista
    print(matriz[i][j], end=" ")
  print()
  
  
  
# Comprimemto das palavras
palavras = ['python', 'compreensão', 'lista', 'código']
comprimentos = [len(palavra) for palavra in palavras]
print(comprimentos)



# Exercício 0 - Compreensão de lista
numeros = list(range(1, 101))
                               
impares = [num for num in numeros if num % 3 == 0]

print(impares)



# Exercício 1 - Compreensão de lista
celsius = [32, 25, 41, 55, 15, 0, -5]

fahrenheit = [(c * 9/5) + 32 for c in celsius]

print(fahrenheit)



# Exercício 2 - Compreensão de lista
numeros = list(range(1, 11))

tuplas = [(numero, numero ** 2, numero **3) for numero in numeros]

# Mostra três valores na tela: numero, ao quadrado, ao cubo.
print(tuplas)