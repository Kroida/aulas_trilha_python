# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

inteiros = int(input('Digite um inteiro: '))
inteiros2 = int(input('Digite outro inteiro: '))

intervalo = []

for i in range(inteiros + 1, inteiros2):
    intervalo.append(i)
    
print(f'Números no intervalo: \n {intervalo}')