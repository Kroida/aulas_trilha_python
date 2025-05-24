# Importa o módulo os para limpar a saída do console no Windows
import os

# Inicializa o dicionário que armazenará as turmas e os alunos cadastrados
turmas = {}

def limpar_output():
    """
    Limpa a saída do console no Windows.
    """
    os.system('cls')

def exibir_menu():
    """
    Exibe o menu principal do programa com as opções disponíveis.
    """
    print('~~~ Menu principal - Escolha uma das opções abaixo ~~~\n')
    print('1. Para criar uma turma')
    print('2. Para cadastrar um aluno e sua nota')
    print('3. Para exibir as informações cadastradas')
    print('4. Para fazer as médias')
    print('5. Para sair')

def criar_turma():
    """
    Cria uma nova turma. Solicita ao usuário o nome da turma e adiciona ao dicionário `turmas`,
    caso ela ainda não exista.
    """
    limpar_output()
    print('~~~ Criação de turma ~~~\n')
    nome_turma = input('Nome da turma: ')
    if nome_turma in turmas:
        limpar_output()
        print(f'"{nome_turma}" já existe.\n')
    else:
        turmas[nome_turma] = {}  # Adiciona a nova turma como um dicionário vazio
        limpar_output()
        print(f'"{nome_turma}" criada com sucesso.\n')

def cadastrar_aluno():
    """
    Cadastra um aluno e sua nota em uma turma específica. Verifica se a turma existe
    e se a nota fornecida está no intervalo permitido (0 a 10).
    """
    if not turmas:
        limpar_output()
        print('Nenhuma turma cadastrada. Crie uma turma antes de cadastrar um aluno.\n')
    else:
        limpar_output()
        print('~~~ Cadastro do aluno ~~~\n')
        print('Turmas disponíveis:')
        for turma in turmas:  # Lista as turmas existentes
            print(f'- {turma}')
        turma_escolhida = input('\nDigite o nome da turma onde deseja cadastrar o aluno: ')

        if turma_escolhida in turmas:
            limpar_output()
            print('~~~ Cadastro do aluno ~~~\n')
            nome = input('Nome do aluno: ')
            try:
                nota = float(input('Nota do aluno: '))  # Solicita a nota e converte para float
                if nota < 0 or nota > 10:  # Verifica se a nota está entre 0 e 10
                    raise ValueError
                turmas[turma_escolhida][nome] = nota  # Adiciona o aluno à turma
                limpar_output()
                print(f'Aluno "{nome}" adicionado à "{turma_escolhida}" com sucesso.\n')
            except ValueError:
                limpar_output()
                print('Nota inválida! Insira um valor NUMÉRICO entre 0 e 10.\n')
        else:
            limpar_output()
            print(f'"{turma_escolhida}" não encontrada.\n')

def exibir_informacoes():
    """
    Exibe as informações cadastradas em uma turma específica, incluindo os nomes dos alunos
    e suas respectivas notas.
    """
    if not turmas:
        limpar_output()
        print('Nenhuma turma cadastrada. Crie uma turma antes de exibir as informações cadastradas.\n')
    else:
        limpar_output()
        print('~~~ Informações das turmas ~~~\n')
        print('Turmas disponíveis:')
        for turma in turmas:  # Lista as turmas existentes
            print(f'- {turma}')
        turma_escolhida = input('\nDigite o nome da turma que deseja visualizar: ')

        if turma_escolhida in turmas:
            limpar_output()
            print(f'Alunos da "{turma_escolhida}": ')
            if turmas[turma_escolhida]:  # Verifica se há alunos cadastrados na turma
                for aluno, nota in turmas[turma_escolhida].items():
                    print(f'- Nome: {aluno}, nota: {nota:.2f}')
                print()
            else:
                print('Nenhum aluno cadastrado nesta turma.\n')
        else:
            limpar_output()
            print(f'"{turma_escolhida}" não encontrada.\n')

def fazer_media():
    """
    Calcula e exibe a média das notas dos alunos de uma turma específica. Verifica se há alunos cadastrados
    antes de realizar o cálculo.
    """
    if not turmas:
        limpar_output()
        print('Nenhuma turma cadastrada. Crie uma turma antes de calcular a média de uma turma.\n')
    else:
        limpar_output()
        print('~~~ Média das turmas ~~~\n')
        print('Turmas disponíveis:')
        for turma in turmas:  # Lista as turmas existentes
            print(f'- {turma}')
        turma_escolhida = input('\nDigite o nome da turma que deseja calcular a média: ')

        if turma_escolhida in turmas:
            limpar_output()
            if turmas[turma_escolhida]:  # Verifica se há alunos na turma
                media = sum(turmas[turma_escolhida].values()) / len(turmas[turma_escolhida].values())
                print(f'Média da "{turma_escolhida}": {media:.2f}\n')
            else:
                print(f'A "{turma_escolhida}" não tem alunos cadastrados para cálculo da média.\n')
        else:
            limpar_output()
            print(f'"{turma_escolhida}" não encontrada.\n')

def rodar_programa():
    """
    Controla o fluxo principal do programa. Exibe o menu, recebe a escolha do usuário
    e executa a funcionalidade correspondente até que o usuário opte por sair.
    """
    while True:
        # Laço para garantir que a entrada seja válida
        while True:
            try:
                exibir_menu()
                escolha = int(input('Selecione uma opção (1/2/3/4/5): '))
                if not (1 <= escolha <= 5):  # Verifica se a escolha está entre 1 e 5
                    raise ValueError
                else:
                    break
            except ValueError:
                limpar_output()
                print('Entrada inválida! Por favor, insira um número válido.\n')

        # Processa a escolha do usuário
        if escolha == 1:
            criar_turma()
        elif escolha == 2:
            cadastrar_aluno()
        elif escolha == 3:
            exibir_informacoes()
        elif escolha == 4:
            fazer_media()
        elif escolha == 5:
            limpar_output()
            print('Encerrando programa...')
            break  # Encerra o programa
        else:
            limpar_output()
            print('Opção inválida!\n')

    print('Programa encerrado.')

# Define o ponto de entrada principal do programa
if __name__ == '__main__':
    rodar_programa()