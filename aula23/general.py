import random

# Dicionário para armazenar os valores dos dados
dados = {
    '1': random.randint(1, 6),
    '2': random.randint(1, 6),
    '3': random.randint(1, 6),
    '4': random.randint(1, 6),
    '5': random.randint(1, 6)
}

# Dicionário para armazenar os dados que o jogador escolhe guardar
dados_guardados = {}

# Dicionário para armazenar a pontuação total de cada rodada
pontuacao_total = {}

# Contador de tentativas disponíveis por rodada
tentativas = 3

# Contador para rastrear o número da rodada
rodada = 1

def menu():
    """
    Exibe o menu principal com as opções disponíveis para o jogador.
    """
    print('~~~ Menu ~~~~')
    print('1. Jogar dados')
    print('2. Ver dados guardados')
    print('3. Ver pontuação das rodadas')
    print('4. Sair')

def calcular_pontuacao():
    """
    Calcula a pontuação com base nas combinações:
    - Sequência Baixa (S): 1-2-3-4-5 ou 2-3-4-5-6 (20 pontos).
    - Full House (F): 3 dados de um valor + 2 de outro (30 pontos).
    - Quadra (P): 4 dados iguais (40 pontos).
    - General (G): 5 dados iguais (50 pontos).
    """
    valores = list(dados_guardados.values())
    valores.sort()
    pontos = 0

    # Sequência Baixa
    if valores == [1, 2, 3, 4, 5] or valores == [2, 3, 4, 5, 6]:
        pontos += 20
        print('Sequência Baixa! (+20 pontos)')
    
    # Full House
    # len(set(valores)) == 3
    # → verifica se existem exatamente três valores diferentes na lista
    #   (o set remove duplicatas e o len conta quantos valores únicos existem)

    # valores.count(valores[0]) in [2]
    # → conta quantas vezes o primeiro valor da lista aparece
    #   e verifica se ele aparece 2 vezes

    # and
    # → as duas condições precisam ser verdadeiras ao mesmo tempo

    # Em conjunto, essa condição verifica se a lista possui:
    # - apenas dois valores distintos
    # - um deles aparecendo 3 vezes e o outro 2 vezes (ex: 3 iguais + 2 iguais)
    elif len(set(valores)) == 3 and (valores.count(valores[0]) in [2]):
        pontos += 30
        print('Full House! (+30 pontos)')

    # Quadra
    # Verifica se existe pelo menos um valor na lista que aparece exatamente 4 vezes.
    # Para cada elemento 'v' em 'valores', conta quantas vezes ele ocorre.
    # A função any() retorna True assim que encontrar um valor com contagem igual a 4,
    # indicando a presença de uma "quadra" (quatro valores iguais).
    elif any(valores.count(v) == 4 for v in valores):
        pontos += 40
        print('Quadra! (+40 pontos)')

    # General
    elif len(set(valores)) == 1:
        pontos += 50
        print('General! (+50 pontos)')

    else:
        print('Nenhuma combinação especial encontrada.')

    return pontos

def organizar_dados():
    """
    Finaliza a rodada:
    - Atualiza o número de tentativas.
    - Move os dados guardados para o conjunto principal de dados.
    - Calcula e registra a pontuação total da rodada.
    - Reseta os dados e prepara para a próxima rodada.
    """
    global tentativas, dados, dados_guardados, rodada, pontuacao_total

    tentativas = 3  # Reinicia as tentativas para a próxima rodada
    pontos_especiais = calcular_pontuacao()  # Calcula pontos adicionais baseados nas combinações
    pontuacao_total[rodada] = pontos_especiais  # Registra a pontuação total da rodada
    if len(dados_guardados) == 5:
      print(f'Pontuação da rodada {rodada}: {pontuacao_total[rodada]}\n')

    else:
      print(f'Pontuação da rodada {rodada}: 0\n')

    dados_guardados.update(dados)  # Adiciona os dados restantes ao conjunto guardado
    dados.clear()  # Limpa os dados principais
    dados_organizados = list(dados_guardados.items())  # Converte para lista de tuplas
    dados_organizados.sort()  # Ordena pelo número do dado
    dados_organizados = dict(dados_organizados)  # Converte de volta para dicionário
    dados.update(dados_organizados)  # Atualiza o dicionário principal
    dados_guardados.clear()  # Limpa os dados guardados

    rodada += 1  # Incrementa o número da rodada

def jogar_dados():
    """
    Simula o lançamento dos dados:
    - Exibe os valores atuais dos dados.
    - Permite ao jogador escolher quais dados guardar.
    - Reatribui valores aleatórios aos dados restantes.
    """
    global tentativas, dados

    print('\n~~~ Dados jogados ~~~')
    for i, j in dados.items():
        print(f'Dado {i}, lado {j}')

    dado = input('\nQuais dados você deseja guardar? (separe por "/"): ')
    print()

    s = dado.split('/')  # Divide a entrada do usuário por "/"

    for i in s:
        if i in dados.keys():  # Verifica se o dado escolhido existe
            dados_guardados[i] = dados[i]  # Move o dado escolhido para os guardados
            del dados[i]  # Remove o dado dos não guardados
        else:
          print('Dado não encontrado\n')
          tentativas += 1

    for i in dados.keys():
        dados[i] = random.randint(1, 6)  # Reatribui valores aos dados restantes

def ver_dados():
    """
    Exibe os dados que o jogador já guardou nesta rodada.
    """
    if not dados_guardados:
        print('\nNenhum dado foi guardado nesta rodada.\n')
    else:
        print('\n~~~ Dados guardados ~~~')
        for i, j in dados_guardados.items():
            print(f'Dado {i}, lado {j}')
        print()

def ver_pontuacao():
    """
    Exibe a pontuação acumulada de cada rodada até o momento.
    """
    if not pontuacao_total:
        print('\nNenhuma pontuação foi registrada até o momento.\n')
    else:
        print('\n~~~ Pontuação das rodadas ~~~')
        for i, j in pontuacao_total.items():
            print(f'Rodada {i}: {j} pontos')
        print()

def rodar_programa():
    """
    Controla o fluxo principal do jogo:
    - Exibe o menu.
    - Processa a escolha do jogador.
    - Verifica se as tentativas acabaram para finalizar a rodada.
    """
    global tentativas

    while True:
        if tentativas == 0 or not dados:  # Finaliza a rodada se as tentativas acabaram ou se todos os dados foram guardados
            organizar_dados()

        menu()
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            jogar_dados()
            tentativas -= 1

        elif escolha == '2':
            ver_dados()

        elif escolha == '3':
            ver_pontuacao()

        elif escolha == '4':
            print('\nEncerrando programa...')
            break

        else:
            print('\nOpção inválida!\n')
    print('Programa encerrado.')

if __name__ == '__main__':
    rodar_programa()