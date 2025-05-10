numero_secreto = 3

for tentativa in range(3):
  palpite = int(input('Tente adivinhar o número(entre 1 e 5): '))
  if palpite == numero_secreto:
    print('Parabéns, você acertou!')
    break
  else:
    print('Errado. Tente novamente')
else: # Esse else está casando com aquele if porque caso o jogador saia do loop a última condição if não terá sido atendida
  print(f'Você não conseguiu acertar. O número era {numero_secreto}')