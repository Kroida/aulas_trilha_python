import random # Biblioteca != de API

numero_secreto = random.randint(1, 102)

while True:
  palpite = int(input('Adivinhe o número secreto (1 à 100): '))

  if palpite == numero_secreto:
    print('Parabéns, você acertou!')
    break
  elif palpite > numero_secreto:
    print('O número secreto é menor')
  else:
    print('O número secreto é maior')