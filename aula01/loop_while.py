# Exemplo 1: Pedindo ao usuário para digitar um número positivo
numero = 0
while numero <= 0:
    numero = float(input("Digite um número positivo: "))
print("Obrigado por digitar um número positivo!")

# Exemplo 2: Simulando uma adivinhação de número
import random
numero_secreto = random.randint(1, 100)
chute = 0
while chute != numero_secreto:
    chute = int(input("Adivinhe o número (entre 1 e 100): "))
    if chute < numero_secreto:
        print("Chute mais alto!")
    elif chute > numero_secreto:
        print("Chute mais baixo!")
print("Parabéns! Você acertou!")