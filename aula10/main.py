# Método e função - Apresentação
numeros = list(range(1, 21))
numeros.reverse()
print(f'Lista numeros após a declaração e .reverse: {numeros}')
print()

numeros2 = sorted(numeros)
print(f'Lista numeros após o sorted(numeros): {numeros}')
print()

print(f'Lista numeros2 derivada de sorted(numeros): {numeros2}')
print()

numeros.sort()
print(f'Lista numeros após o .sort: {numeros}')