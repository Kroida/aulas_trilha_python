import os

agenda = {}  # Dicionário para armazenar os contatos

while True:
    print('~~~ Bem vindo ao menu ~~~')
    print('1. Adicionar contato')
    print('2. Exibir contatos')
    print('3. Sair')

    escolha = int(input('Digite a opção desejada (1/2/3): '))

    if escolha == 1:
        # Adiciona novo contato
        nome = input('\nDigite o nome do contato: ').lower()
        numero = int(input('Digite o número do contato: '))

        if nome in agenda:
            print('\nEsse contato já existe!\n')
        else:
            agenda[nome] = numero
            print('\nContato adicionado com sucesso!\n')
    elif escolha == 2:
        # Mostra todos os contatos
        print('\n~~~ Listando contatos ~~~')
        for contato in agenda:
            print(f'- {contato.capitalize()}, {agenda[contato]}')
        print()
    elif escolha == 3:
        # Encerra o programa
        os.system('cls')
        print('Encerrando programa...')
        break
    else:
        print('\nOpção inválida!\n')

print('Programa encerrado.')