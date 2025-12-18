import random

baralho = {
    "A Pedra do Falar": "Palavra-chave: Comunicação. Enfatizar a importância da comunicação honesta e aberta. Incluir a necessidade de ouvir com atenção e empatia.",
    "O Cachimbo Sagrado": "Palavra-chave: Paz. Destacar a busca pelo equilíbrio interior e a resolução pacífica de conflitos.",
    "A Roda Medicinal": "Palavra-chave: Ciclos e Movimentos. Abordar a natureza cíclica da vida, a aceitação das mudanças e a constante transformação.",
    "O Ritual do Suor": "Palavra-chave: Purificação. Simbolizar a libertação de energias negativas e a busca pela renovação espiritual.",
    "Os Clãs das Avós": "Palavra-chave: Conexão com os Ancestrais. Enfatizar o aprendizado com a história, a tradição e os ensinamentos dos ancestrais.",
    "Os Pássaros Rituais": "Palavra-chave: Elevação do Espírito. Representar a capacidade de superar desafios e elevar-se acima das dificuldades, buscando inspiração e força interior.",
    "O Tambor": "Palavra-chave: Ritmo Interior. Conectar-se com o ritmo natural da vida, encontrar equilíbrio e harmonia interior.",
    "O Totem do Escudo": "Palavra-chave: Autodefesa. Enfatizar a importância de estabelecer limites saudáveis e proteger-se de influências negativas.",
    "O Clã do Lobo": "Palavra-chave: Lealdade. Representar a importância da comunidade, do trabalho em equipe e da fidelidade aos seus valores e princípios.",
    "O Espírito Animal": "Palavra-chave: Conhecimento e Intuição. Conectar-se com a sabedoria animal, confiar em seus instintos e intuição, aprofundar a conexão espiritual.",
    "A Tenda da Lua": "Palavra-chave: Introspecção Feminina. Honrar a sabedoria interior feminina, conectar-se com os ciclos da lua e buscar o autoconhecimento.",
    "O Visionário": "Palavra-chave: Clareza Espiritual. Buscar uma visão clara sobre seu propósito de vida, conectar-se com sua intuição e seguir o caminho da alma.",
    "A Fogueira Interna": "Palavra-chave: Motivação Pessoal. Alimentar a chama da sua motivação pessoal, perseguir seus objetivos com paixão e entusiasmo.",
    "A Árvore de Arco": "Palavra-chave: Conexão com a Natureza. Buscar a estabilidade e o equilíbrio na natureza, conectar-se com a energia da terra e encontrar paz interior.",
    "O Ninho do Corvo": "Palavra-chave: Magia e Mistérios. Aceitar os mistérios da vida como oportunidades de aprendizado, explorar o desconhecido e abraçar a magia do universo.",
    "A Roda do Sol": "Palavra-chave: Iluminação e Verdade. Buscar a verdade, a clareza e a iluminação na sua jornada espiritual, conectar-se com sua essência divina.",
    "Os Sonhos de Águia": "Palavra-chave: Visão Ampliada. Ter uma visão ampla da vida, ampliar suas perspectivas e buscar a compreensão do panorama geral.",
    "O Fogo Sagrado": "Palavra-chave: Transformação. Libertar-se de velhos padrões, crenças limitantes e energias negativas, abraçar a transformação e a renovação.",
    "Os Caminhos da Terra": "Palavra-chave: Respeito pela Vida. Honrar a vida em todas as suas formas, cultivar o respeito pela natureza e viver em harmonia com o planeta.",
    "O Guerreiro Pacífico": "Palavra-chave: Força Interior. Encontrar força na calma e na serenidade, enfrentar os desafios com coragem e sabedoria, sem recorrer à violência.",
    "Os Quatro Ventos": "Palavra-chave: Direções e Propósitos. Buscar orientação espiritual, conectar-se com seu propósito de vida e seguir o caminho que lhe foi destinado.",
    "A Estrela da Manhã": "Palavra-chave: Renovação. Acreditar na possibilidade de recomeços, ter esperança no futuro e abraçar as novas oportunidades que a vida oferece.",
    "Os Espíritos Ancestrais": "Palavra-chave: Sabedoria dos Ancestrais. Conectar-se com a sabedoria dos seus ancestrais, buscar orientação e apoio no reino espiritual, honrar suas raízes.",
    "O Arco-íris": "Palavra-chave: União e Harmonia. Celebrar a diversidade, promover a união e o respeito entre as pessoas, reconhecer a beleza na diferença.",
    "Os Mistérios da Lua": "Palavra-chave: Ciclos de Emoção. Honrar suas emoções, fluir com os ciclos da vida, conectar-se com sua intuição e abraçar a sua sensibilidade.",
    "A Dança do Sol": "Palavra-chave: Celebração da Vida. Celebrar a vida, agradecer pelas bênçãos recebidas, cultivar a alegria e o entusiasmo pela jornada.",
    "O Guardião das Plantas": "Palavra-chave: Cura e Renovação. Conectar-se com o poder curativo das plantas, buscar a cura física, emocional e espiritual, renovar suas energias através da natureza.",
    "O Espírito do Urso": "Palavra-chave: Coragem e Autoconfiança. Encontrar a coragem para enfrentar seus medos, confiar em sua força interior e acreditar em sua capacidade de superar desafios.",
    "O Espírito do Coiote": "Palavra-chave: O Mestre do Truque. Abraçar os desafios como oportunidades de aprendizado, cultivar o bom humor, ser flexível e adaptar-se às mudanças.",
    "A Sabedoria do Avô": "Palavra-chave: Sabedoria Ancestral. Aprender com a experiência dos mais velhos, buscar orientação e conselhos, valorizar a sabedoria e a tradição.",
    "A Tartaruga": "Palavra-chave: Persistência e Paciência. Cultivar a paciência, perseverar em seus objetivos, ter a certeza de que o sucesso vem com o tempo e a constância.",
    "A Mulher Búfalo Branco": "Palavra-chave: Abundância e Dons. Reconhecer as bênçãos em sua vida, cultivar a gratidão e a generosidade, celebrar a abundância e os dons que você possui.",
    "A Borboleta": "Palavra-chave: Transformação e Leveza. Abraçar as mudanças e transformações da vida, encontrar a leveza e a beleza em cada etapa da sua jornada.",
    "O Espírito da Águia": "Palavra-chave: Liberdade e Inspiração. Buscar a liberdade em todas as áreas da sua vida, expandir sua visão, conectar-se com sua inspiração e voar alto.",
    "O Espírito do Golfinho": "Palavra-chave: Alegria e Comunicação. Cultivar a alegria, a leveza e a comunicação autêntica, conectar-se com as pessoas de forma genuína e harmoniosa.",
    "O Espírito do Lobo": "Palavra-chave: Mestre e Guia. Conectar-se com sua força interior, assumir seu papel de líder e guia, confiar em sua intuição e seguir o caminho da sua alma.",
    "A Cobra": "Palavra-chave: Renovação e Mudança. Libertar-se de velhos padrões e crenças limitantes, renovar-se, abraçar a mudança e seguir em frente com mais sabedoria.",
    "O Espírito do Jaguar": "Palavra-chave: Poder Pessoal. Encarar seus medos, acessar sua força interior, reconhecer seu poder pessoal e usá-lo para realizar seus sonhos.",
    "A Tenda da Alma": "Palavra-chave: Refúgio Espiritual. Criar um espaço sagrado para si mesmo, conectar-se com sua alma, buscar paz interior e encontrar refúgio no seu mundo interior.",
    "O Espírito da Fênix": "Palavra-chave: Renascimento. Superar os desafios, renascer das dificuldades, encontrar força para recomeçar e transformar sua vida para melhor.",
    "O Conselho dos Anciões": "Palavra-chave: Sabedoria Coletiva. Buscar orientação e sabedoria com as pessoas mais experientes, valorizar o conhecimento coletivo e aprender com a história.",
    "O Espírito da Raposa": "Palavra-chave: Camuflagem e Inteligência. Usar sua inteligência para superar desafios, ser estratégico, adaptar-se às circunstâncias e encontrar soluções criativas.",
    "O Espírito do Corvo": "Palavra-chave: Magia e Leis Universais. Conectar-se com a magia do universo, compreender as leis universais, buscar o conhecimento oculto e desvendar os mistérios da vida.",
    "A Estrela de Nascente": "Palavra-chave: Esperança e Novos Começos. Ter esperança no futuro, acreditar em novos começos, acolher as novas oportunidades que surgem a cada dia."
}

caixa_de_sequencias = {}

sequencias_para_mostrar = []

def menu():
  print('~~~ Menu ~~~')
  print('1. Tirar sequência')
  print('2. Mostrar sequências')
  print('3. Exibir descrição de uma carta')
  print('4. Embaralhar baralho')
  print('5. Sair')


def tirar_sequencias():
  global baralho, caixa_de_sequencias, sequencias_para_mostrar

  if not baralho:
    print('\nO baralho está vazio.\n')

  else:
    print('\n~~~ Tirando sequência ~~~')
    nova_sequencia = {}
    if len(baralho) < 5:
      for i in range(len(baralho)):
        carta = random.choice(list(baralho.items()))
        del baralho[carta[0]]
        nova_sequencia[carta[0]] = carta[1]
        caixa_de_sequencias[carta[0]] = carta[1]
        print(f'Carta sorteada: {carta[0]}')
      sequencias_para_mostrar.append(nova_sequencia)
      print()

    else:
      for i in range(5):
        carta = random.choice(list(baralho.items()))
        del baralho[carta[0]]
        nova_sequencia[carta[0]] = carta[1]
        caixa_de_sequencias[carta[0]] = carta[1]
        print(f'Carta sorteada: {carta[0]}')
      sequencias_para_mostrar.append(nova_sequencia)
      print()


def mostrar_sequencias():
  global caixa_de_sequencias

  if not caixa_de_sequencias:
      print('\nSua sequência está vazia. Suas sequências aparecerão aqui.\n')

  else:
      print('\n~~~ Sequências ~~~')
      for i, sequencia in enumerate(sequencias_para_mostrar):
        print(f'Sequência {i+1}:')
        for j in sequencia.keys():
          print(f'- {j}')
        print()


def exibir_info():
  global caixa_de_sequencias

  if not caixa_de_sequencias:
    print('\nPara ver suas cartas você precisa de pelo menos uma sequência.\n')

  else:
    carta_escolhida = input('\nDigite o nome da carta que deseja ver a descrição: ')
    if carta_escolhida in caixa_de_sequencias:
      carta_para_mostrar = {}
      carta_para_mostrar[carta_escolhida] = caixa_de_sequencias[carta_escolhida]
      print()
      for carta, descricao in carta_para_mostrar.items():
        print(f'~~~ Carta ~~~\n{carta}\n')
        print(f'~~~ Descrição ~~~\n{descricao}\n')
      print()

    else:
      print('\nCarta não encontrada.\n')


def embaralhar():
  global baralho, caixa_de_sequencias, sequencias_para_mostrar

  if not caixa_de_sequencias:
    print('\nVocê ainda não fez nenhuma sequência. Faça no mínimo uma sequência para embaralhar as cartas.\n')

  else:
    baralho.update(caixa_de_sequencias)
    caixa_de_sequencias.clear()
    sequencias_para_mostrar.clear()
    baralho_embaralhado = list(baralho.items())
    baralho.clear()
    random.shuffle(baralho_embaralhado)
    for carta, descricao in baralho_embaralhado:
      baralho[carta] = descricao
    baralho_embaralhado.clear()
    print('\nBaralho embaralhado.\n')


def rodar_programa():
  while True:
    menu()

    while True:
      try:
        escolha = int(input('Escolha uma opção (1/2/3/4/5): '))
        if not 1 <= escolha <= 5:
          raise ValueError
        else:
          break
      except:
        print('\nOpção inválida!\n')
        menu()

    if escolha == 1:
      tirar_sequencias()

    elif escolha ==2:
      mostrar_sequencias()

    elif escolha == 3:
      exibir_info()

    elif escolha == 4:
      embaralhar()

    elif escolha == 5:
      print('\nEncerrando Programa...')
      break

    else:
      print('\nOpção inválida!\n')


  print('Programa encerrado.')

if __name__ == '__main__':
  rodar_programa()