# Se aprofundando em dicionários

# Inicializa um dicionário vazio que irá armazenar as informações dos alunos
alunos = {}

# Inicializa uma lista vazia que irá armazenar o dicionário de cada aluno
dados = []

# Laço for que irá iterar 3 vezes, permitindo a entrada de dados de 3 alunos
for i in range(0, 3):
    # Recebe o nome do aluno e armazena no dicionário 'alunos' com a chave 'nome'
    aluno = alunos['nome'] = input('Digite o nome do aluno: ')

    # Recebe a nota do aluno e armazena no dicionário 'alunos' com a chave 'nota'
    aluno = alunos['nota'] = input('Digite a nota do aluno: ')

    # Adiciona uma cópia do dicionário 'alunos' à lista 'dados'
    # Usamos 'copy()' para garantir que cada entrada no loop seja uma nova instância do dicionário 'alunos'
    dados.append(alunos.copy())
    
print(dados)