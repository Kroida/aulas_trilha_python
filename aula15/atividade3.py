# Crie uma lista de tuplas que contenham coordenadas (x, y) de pontos em um plano cartesiano. Peça ao usuário para adicionar coordenadas e, ao final, exiba todas as coordenadas inseridas.
lista_de_tuplas = []

while True:
  x = int(input('Digite a coordenada x (ou um valor negativo para sair): '))

  if x < 0:
    break
  else:
    y = int(input('Digite a coordenada y: '))
  lista_de_tuplas.append((x, y))

  print('Coordenadas inseridas')
  for tupla in lista_de_tuplas:
    print(tupla)
