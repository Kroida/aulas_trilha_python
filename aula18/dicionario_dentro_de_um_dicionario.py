# Inicializa um dicionário vazio para armazenar as turmas e seus respectivos alunos
turmas1 = {}

# Define o nome e a nota de um aluno
nome1 = 'João'  # Nome do primeiro aluno
nota1 = 8.5     # Nota do primeiro aluno

# Define o nome e a nota de outro aluno
nome2 = 'Maria' # Nome do segundo aluno
nota2 = 9.0     # Nota do segundo aluno

# Adiciona uma nova turma chamada 'Turma1' ao dicionário principal
turmas1['Turma1'] = {}

# Adiciona o primeiro aluno e sua nota ao dicionário da turma 'Turma1'
turmas1['Turma1'][nome1] = nota1

# Adiciona o segundo aluno e sua nota ao dicionário da turma 'Turma1'
turmas1['Turma1'][nome2] = nota2

# Exibe o dicionário final, contendo as turmas, alunos e suas notas
print(turmas1)
# Saída esperada:
# {'Turma1': {'João': 8.5, 'Maria': 9.0}}