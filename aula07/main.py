# Comparando append com extends
a = ['maçã', 'banana', 'laranja', 'morango']
b = ['batata', 'cebola', 'pinhão']

a.append(b)
a.extend(b)
frutas = a + b
print(frutas)

# Contador de números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1

print(f"Existem {contador_pares} números pares na lista.")

# Contador de números pares enxuto corrigido
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usa list comprehension para filtrar os números pares e calcula o comprimento da lista resultante. [expressão for elemento in iterável if condição]
contador_pares = len([numero for numero in numeros if numero % 2 == 0])

# Imprime a quantidade de números pares na lista
print(f'Existem {contador_pares} números pares na lista.')

# Limpando a lista frutas
frutas = ['maçã', 'banana', 'laranja', 'morango']

while len(frutas) > 0:
  fruta = frutas.pop() # Remove o último item da lista
  print(f'Removendo {fruta}, itens restantes: {len(frutas)}')
print('Todas as frutas foram removidas.')

# Lista de números para busca.
numeros = [5, 3, 8, 2, 7, 9, 1]

i = 0 # Variável inicial para a posição do índice da lista.

encontrado = False # Variável para indicar se o número 7 foi encontrado ou não.

# Inicia um loop 'while' que vai continuar enquanto 'i' for menor que o comprimento da lista 'numeros'.
while i < len(numeros):
    # Verifica se o número atual na posição 'i' é igual a 7.
    if numeros[i] == 7:
        # Se for igual, define 'encontrado' como True.
        encontrado = True
        # Imprime a posição onde o número 7 foi encontrado.
        print(f"Número 7 encontrado na posição {i}")
        # Interrompe o loop com 'break' porque o número já foi encontrado.
        break
    # Incrementa +1 ao índice para avançar a lista
    i += 1

# Se 'encontrado' for False, significa que o número 7 não foi encontrado na lista.
if not encontrado:
    print("Número 7 não encontrado na lista.")
    
# Programa que permite o usuário criar uma lista de compras
lista = []

while True:
  item = input('Digite um item ou 0 para finalizar: ')
  if item == '0':
    print(f'Lista finalizada: {lista}')
    break
  lista.append(item)
  print(f'lista atual: {lista}')
  
# Programa que permite o usuário criar uma lista de compras corrigido
lista_de_compras = []

while True:
  item = input('Digite o produto para lista ou S para sair: ').upper()
  if item == 'S':
    break
  lista_de_compras.append(item)
  lista_de_compras.sort()
print('Esta é sua lista de compras')
for i, item in enumerate(lista_de_compras): # enumerate() para enumerar a lista de compras
  print(f'{i+1} - {item}')
  
# Imprimindo números pares e impares
numeros = []

while True:
  digitado = int(input('Digite um número: '))
  if digitado == 0:
    break
  numeros.append(digitado)

numeros_pares = []
numeros_impares = []

# Separando os números em pares e ímpares
for numero in numeros:
  if numero % 2 == 0:
    numeros_pares.append(numero)
  else:
    numeros_impares.append(numero)

# Exibindo os resultados
print("Números ímpares:", numeros_impares)
print("Números pares:", numeros_pares)