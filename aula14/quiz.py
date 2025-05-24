# Jogo de Quiz em Python
# Objetivo: criar um jogo de perguntas e respostas como exercício de fixação para listas e seus métodos.

import random

# Função principal do jogo quiz
def jogar_quiz():
# Lista de perguntas e respostas (usando listas aninhadas)
  perguntas = [
      ["Qual a capital da França?", "paris"],
      ["Quanto é 5 + 3?", "8"],
      ["Qual a cor do céu em um dia claro?", "azul"],
      ["Quem descobriu o Brasil?", "pedro alvares cabral"],
      ["Quantos dias há em um ano bissexto?", "366"],
      ["Qual função é usada para imprimir algo na tela em Python?", "print"],
      ["Como declaramos uma lista em Python?", "usando colchetes"],
      ["Qual método adiciona um elemento ao final da lista?", "append"],
      ["Como removemos o último elemento da lista?", "pop"],
      ["Como verificamos o tamanho de uma lista?", "len"],
      ["Como criamos uma tupla em Python?", "usando parênteses"],
      ["Qual palavra-chave é usada para definir uma função?", "def"],
      ["Como fazemos um loop que percorre todos os elementos de uma lista?", "for"],
      ["Como verificamos se um valor está presente em uma lista?", "in"],
      ["Qual método ordena uma lista em ordem crescente?", "sort"],
      ["Qual operador é usado para verificar igualdade?", "=="],
      ["Como declaramos um dicionário em Python?", "usando chaves"],
      ["Como acessamos um valor em um dicionário?", "usando a chave"],
      ["Qual método retorna o número de vezes que um valor aparece na lista?", "count"],
      ["Como podemos inverter a ordem de uma lista?", "reverse"],
      ["Como adicionamos um elemento em uma posição específica da lista?", "insert"],
      ["Qual é a estrutura condicional em Python?", "if, elif, else"],
      ["Como indicamos um comentário em Python?", "#"],
      ["Qual operador é usado para a divisão inteira?", "//"],
      ["Como podemos concatenar duas listas?", "usando +"],
      ["Qual método remove um elemento específico da lista?", "remove"],
      ["Como declaramos uma variável em Python?", "apenas atribuindo um valor"],
      ["Qual função retorna o maior valor em uma lista?", "max"],
      ["Qual função retorna o menor valor em uma lista?", "min"],
      ["Como podemos obter uma sub-lista a partir de uma lista?", "usando fatiamento"]
  ]

  # Embaralhar perguntas
  random.shuffle(perguntas)

  # Inicializar pontuação
  pontuacao = 0

  # Lista para armazenar as perguntas
  perguntas_corretas = []
  perguntas_incorretas = []
  lista_total = perguntas_corretas + perguntas_incorretas

  # Boas vindas ao jogo
  print('=' * 30)
  print('Bem vindo ao Jogo de Quiz!')
  print('Responda as perguntas e teste seu conhecimento.')
  print('=' * 30)

  # Laço principal para fazer as perguntas
  for pergunta, resposta_correta in perguntas:
    # Mostrar a pergunta ao jogador
    resposta_jogador = input(f'\n{pergunta}').lower()
    # Verificar a resposta do jogador
    if resposta_jogador == resposta_correta:
      print('Resposta correta! 🎉')
      pontuacao += 1
      perguntas_corretas.append(pergunta) # Armazenando pergunta respondida corretamente
    else:
      print(f'Resposta incorreta! A resposta correta era {resposta_correta}')
      perguntas_incorretas.append(pergunta)

  # Exibir o resultado final
  print('\n=== Resultado Final ===')
  print(f'Pontuação: {pontuacao / len(perguntas)}')
  print(f'Perguntas erradas: {len(perguntas_incorretas)}')
  print(f'Perguntas certas: {len(perguntas_corretas)}')

  # Lista perguntas corretas e incorretas
  if perguntas_corretas:
    print('\nVocê acertou as seguintes perguntas: ')
    for p in perguntas_corretas:
      print(f'- {p}')
  if perguntas_incorretas:
    print('\nVocê errou as seguintes perguntas: ')
    for p in perguntas_incorretas:
      print(f'- {p}')

# Função para exibir o menu principal
def menu_principal():
  while True:
    print('\n=== JOGO QUIZ ===')
    print('1. Jogar')
    print('2. Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
      jogar_quiz()
    elif opcao == '2':
      print('Obrigado por jogar! Até a próxima 🥸')
      break
    else:
      print('Opção inválida! Por favor, escolha 1 ou 2.')

if __name__ == '__main__':
  menu_principal()