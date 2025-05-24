# Tuplas aceitam diversos tipos de variáveis
frutas = ("maçã", "banana", "laranja")
numeros = (1, 2, 3, 4, 5)
misturado = ("texto", 10, 3.14, True)

# Criando uma tupla sem parênteses
frutas = "maçã", "banana", "laranja"

# Você consegue contar quantas vezes um elemento se repete em uma tupla, assim como em uma lista
frutas = ("maçã", "banana", "maçã", "laranja")
print(frutas.count("maçã"))  # Saída: 2

# Assim como nas listas, você também consegue retornar o índice de um elemento
print(frutas.index("banana"))  # Saída: 1

# Fatiando uma tupla, é possível em listas também
frutas = ("maçã", "banana", "laranja")

# Acessando o primeiro elemento
print(frutas[0])  # Saída: maçã

# Acessando o último elemento
print(frutas[-1])  # Saída: laranja

# Percorrendo uma tupla com fatiamento, é possível em listas também
numeros = (1, 2, 3, 4, 5)

# Obtendo uma sub-tupla com os elementos de índice 1 a 3
sub_tupla = numeros[1:4]
print(sub_tupla)  # Saída: (2, 3, 4)

# Colocando dados importantes em uma tupla
def coordenadas():
    x = 10
    y = 20
    return x, y  # Retornando uma tupla

ponto = coordenadas()
print(ponto)  # Saída: (10, 20)