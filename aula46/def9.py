# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numeros = list(range(1, 51))

for numero in numeros:
    if numero % 2 != 0:
        print(numero)