# ===Ordem de Exercícios para Desenvolvimento do Jogo da Forca===

# Para ajudar os alunos a desenvolverem suas habilidades de programação, aqui está uma série de exercícios para guiá-los no desenvolvimento do jogo da forca. O objetivo é praticar o uso de listas, métodos de listas, lógica de programação e, posteriormente, tuplas e dicionários.

# Parte 1: Trabalhando com Listas e Métodos de Listas

# Exercício 1: Crie uma lista de palavras para o jogo da forca e escolha uma palavra aleatória usando a função random.choice().

# Objetivo: Entender como listas funcionam e como selecionar elementos aleatórios.

# Exercício 2: Crie uma lista para representar as letras descobertas da palavra, inicialmente contendo apenas sublinhados (_) e faça a atualização com as letras corretas adivinhadas.

# Objetivo: Praticar a modificação de elementos em uma lista.

# Exercício 3: Crie uma lógica para receber uma letra do usuário e verificar se ela está na palavra secreta. Se sim, atualize a lista de letras descobertas.

# Objetivo: Trabalhar com condicionais (if/else) e iteração sobre listas.

# Exercício 4: Implemente uma lista para armazenar letras erradas e mostre ao jogador as letras incorretas já tentadas.

# Objetivo: Utilizar listas para armazenar informações de forma dinâmica.

# Exercício 5: Adicione uma contagem de tentativas e crie uma lista que represente as partes do corpo do boneco da forca. Atualize a lista conforme os erros ocorrem.

# Objetivo: Manipular múltiplas listas simultaneamente e aplicar lógica de decremento de tentativas.

# Jogo da forca em Python
# Objetivo: criar um jogo da forca educativo e didático, aplicando boas práticas de Clean Code e ilustrando o uso de listas e métodos em Python

import random

def jogar_forca():
    # Lista de palavras para o jogo
    palavras = ['python', 'algoritmo', 'programacao', 'forca', 'educacao', 'tecnologia']

    # Escolhe a palavra chave | random.choice() sorteia um item da lista
    palavra_secreta = random.choice(palavras)

    # Inicializar variáveis
    partes_do_corpo = ['cabeça', 'braço esq.', 'braço dir.', 'perna esq.', 'perna dir.']
    letras_erradas = []  # Lista para armazenar letras incorretas
    letras_descobertas = ['_' for _ in palavra_secreta]  # Cria uma lista com sublinhados para cada letra da palavra
    partes_do_corpo_inseridas = []
    tentativas = 6  # Quantidade máxima de tentativas

    # Boas vindas e instruções do jogo
    print('=' * 30)
    print('Bem vindo ao Jogo da Forca!')
    print('Tente adivinhar a palavra secreta!')
    print('=' * 30)

    # Laço principal
    while tentativas > 0 and '_' in letras_descobertas:
        # Exibir o status atual do jogo
        print('\nPalavra: ', ' '.join(letras_descobertas))
        print(f'Letras erradas: {", ".join(letras_erradas)}')
        print(f'Partes do corpo desenhadas: {", ".join(partes_do_corpo_inseridas)}')
        print(f'Tentativas restantes: {tentativas}')

        # Solicitação
        chute = input('\nEntre com seu palpite: ').lower()

        # Validando a entrada | .isalpha() retorna true se todos os itens forem strings de a-z
        if not chute.isalpha() or len(chute) != 1:
            print('Entrada errada, digite apenas uma letra!')
            continue

        # Verifica se a letra já foi chutada
        if chute in letras_erradas or chute in letras_descobertas:
            print('Você já tentou essa letra! Tente outra!')
            continue

        # Atualiza o jogo com base no chute
        if chute in palavra_secreta:
            print(f'Bom trabalho! A letra "{chute}" está na palavra!')
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute

        else:
            print(f'Ops! A letra "{chute}" não está na palavra')
            letras_erradas.append(chute)
            tentativas -= 1
            # Desenhar o corpo
            if partes_do_corpo:
                partes_do_corpo_inseridas.append(partes_do_corpo.pop(0))

    # Verificar o resultado do jogo
    if '_' not in letras_descobertas:
        print('\nParabéns!')
        print(f'A palavra secreta era: {" ".join(palavra_secreta)}')
    else:
        print('Game Over')
        print(f'A palavra secreta era: {" ".join(palavra_secreta)}')
        print('Partes do corpo desenhadas: ', ', '.join(partes_do_corpo_inseridas))

# Função para exibir o menu principal
def menu_principal():
    while True:
        print('\n=== Bem vindo ao jogo da forca! ===')
        print('1 - Jogar')
        print('2 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            jogar_forca()
        elif opcao == '2':
            print('\nSaindo do jogo...')
            break
        else:
            print('\nOpção inválida. Tente novamente.')

# Se o script for principal, o seguinte bloco de comando sempre será executado
if __name__ == '__main__':
    menu_principal()