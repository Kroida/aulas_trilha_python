# Criando um algoritmo de cálculo IMC
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

imc = peso / (altura * altura) # Fórmula IMC

print('Seu IMC é: ', imc)
