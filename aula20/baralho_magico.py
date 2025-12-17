import random

baralho = {
    'Leste': 'Representa a lição para remover as limitações que impedem o alcance de outros níveis de consciência.\nObserve atentamente o que você ainda não conseguiu alcançar dentro da lição desta carta para que suas próprias limitações se tornem mais claras.',
    'Sul': 'Aponta para a lição que auxiliará na restauração da confiança e fé.\nRevela os aspectos do ego que precisam ser trabalhados, como curar a dor da traição e como evitar o papel de vítima, encorajando a coragem para viver a vida como uma aventura.',
    'Oeste': 'Indica a lição para encontrar a verdade pessoal e reconhecer o que é mais adequado para você.',
    'Norte': 'Ensina a lição para reconhecer seus talentos e dons.\nValorize suas habilidades e posses materiais para não se afastar da abundância e reconhecer a beleza das dádivas que você possui.',
    'Montanha Sagrada': 'simboliza a lição final para encontrar a liberdade pessoal, abandonando as limitações que você impôs a si mesmo.\nAo confrontar seus medos e autolimitações, você poderá desfrutar de uma visão ilimitada e alcançar o conhecimento interior e equilíbrio.'
}

baralho_sorteado = {}

def menu():
  print('~~~ Carta para a Sequência da Montanha Sagrada ~~~')
  print('1. Tirar carta')
  print('2. Mostrar baralho')
  print('3. Exibir descrição de uma sequência')
  print('4. Embaralhar baralho')
  print('5. Sair')


def tirar_carta():
  if not baralho:
    print('\nO baralho está vazio.\n')

  else:
    carta = random.choice(list(baralho.items()))
    del baralho[carta[0]]
    baralho_sorteado[carta[0]] = carta[1]
    print(f'\nCarta sorteada: {carta[0]}\n')


def mostrar_baralho_sorteado():
    if not baralho_sorteado:
        print('\nO baralho está vazio. Suas cartas sorteadas aparecerão aqui.\n')

    else:
        print('\n~~~ Cartas disponíveis ~~~')
        for carta in baralho_sorteado:
            print(carta)
        print()


def embaralhar():
  if len(baralho_sorteado) == 0:
    print('\nO baralho está vazio.\n')

  elif len(baralho_sorteado) < 5:
    print('\nO baralho precisa estar cheio para o embaralharamento.\n')

  else:
    baralho.update(baralho_sorteado)
    baralho_sorteado.clear()
    baralho_embaralhado = list(baralho.items())
    baralho.clear()
    random.shuffle(baralho_embaralhado)
    for carta, descricao in baralho_embaralhado:
      baralho[carta] = descricao
    print('\nBaralho embaralhado\n')


def exibir_info():
  carta_escolhida = input('\nDigite o nome da carta que deseja ver a descrição: ')
  if carta_escolhida in baralho_sorteado.keys():
    carta_para_mostrar = {}
    carta_para_mostrar[carta_escolhida] = baralho_sorteado[carta_escolhida]
    print()
    for carta, descricao in carta_para_mostrar.items():
      print(f'Carta: {carta}')
      print(f'Descrição: {descricao}')
    print()
  else:
    print('\nCarta não encontrada.\n')


def rodar_programa():
  while True:
    menu()
    escolha = int(input('Escolha uma opção (1/2/3/4/5): '))

    if escolha == 1:
      tirar_carta()

    elif escolha ==2:
      mostrar_baralho_sorteado()

    elif escolha == 3:
      exibir_info()

    elif escolha == 4:
      embaralhar()

    elif escolha == 5:
      print('\nEncerrando Programa...')
      break

    else:
      print('Opção inválida. Tente novamente.')


  print('Programa encerrado.')

if __name__ == '__main__':
  rodar_programa()