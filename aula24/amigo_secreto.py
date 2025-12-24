import random
# Importa o módulo random da biblioteca padrão
# Ele será usado para embaralhar os participantes de forma aleatória


def get_participants():
    # Solicita ao usuário os nomes dos participantes em uma única linha
    # Espera que os nomes sejam separados por vírgula e espaço (", ")
    participants = input(
        'Digite os nomes dos participantes separados por vírgula: '
    ).split(', ')

    # Remove espaços extras no início e no fim de cada nome
    # Isso evita problemas caso o usuário digite espaços a mais
    return [p.strip() for p in participants]


def draw_secret_santa(participants):
    # Cria uma cópia da lista original para não modificá-la diretamente
    friends = participants.copy()

    # Embaralha a lista de amigos de forma aleatória (in-place)
    random.shuffle(friends)

    # Percorre os índices da lista para comparar posições equivalentes
    for i in range(len(participants)):
        # Verifica se alguém acabou tirando a si mesmo
        if participants[i] == friends[i]:
            # Caso isso aconteça, o sorteio é inválido
            # A função é chamada novamente para tentar outro embaralhamento
            return draw_secret_santa(participants)

    # Cria e retorna um dicionário:
    # chave   -> quem vai dar o presente
    # valor   -> quem vai receber o presente
    return {
        participants[i]: friends[i]
        for i in range(len(participants))
    }


def display_results(results):
    # Exibe o título do resultado com uma linha em branco antes
    print('\nAmigo Secreto:')

    # Percorre o dicionário de resultados
    for giver, receiver in results.items():
        # Imprime quem tira quem usando f-string
        print(f'{giver} -> {receiver}')


def main():
    # Obtém a lista de participantes a partir da entrada do usuário
    participants = get_participants()

    # Valida se há participantes suficientes para o jogo
    if len(participants) < 2:
        print('É necessário pelo menos 2 participantes.')
        return  # Encerra o programa caso a condição não seja atendida

    # Realiza o sorteio do amigo secreto
    results = draw_secret_santa(participants)

    # Exibe o resultado final do sorteio
    display_results(results)


# Verifica se este arquivo está sendo executado diretamente
# (e não importado como módulo em outro script)
if __name__ == '__main__':
    # Ponto de entrada do programa
    main()