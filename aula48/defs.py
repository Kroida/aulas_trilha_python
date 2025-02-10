# 1. Inverter uma String (Tempo sugerido: 5 minutos)

# Pergunta: Escreva uma função que recebe uma string como entrada e retorna a string invertida.

def string_invertida(string):
    return print(string[::-1])

string_invertida("Hello World")

# 2. Soma de Números Pares (Tempo sugerido: 5 minutos)

# Pergunta: Escreva uma função que recebe uma lista de números e retorna a soma dos números pares.

def soma_pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return print(sum(pares))

soma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 3. Encontrar o Segundo Maior Número (Tempo sugerido: 10 minutos)

# Pergunta: Dada uma lista de números, escreva uma função que retorna o segundo maior número.

# def segundo_maior(lista):

# Resolvido pelo Professor:
def segundo_maior(lista):
    lista = list(set(lista))  # Removendo duplicatas
    lista.sort(reverse=True)  # Ordenando em ordem decrescente
    return lista[1] if len(lista) > 1 else None

print(segundo_maior([10, 20, 4, 45, 99, 99]))  # Saída esperada: 45

# Modo alternativo sugerido por um colega
def segundo_maior(lista):
    lista = list(set(lista))  # Removendo duplicatas
    return lista[-2] if len(lista) > 1 else None

print(segundo_maior([10, 20, 4, 45, 99, 99]))  # Saída esperada: 45

# 4. Verificando se é palíndromo

# 5. Construindo uma sequência de fibonacci
def fibonacci(n):
    sequencia = [0, 1]
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    for i in range(2, n):
        numero = sequencia[-1] + sequencia[-2]
        sequencia.append(numero)
        
    return print(sequencia)

fibonacci(9)

    