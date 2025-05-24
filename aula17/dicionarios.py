# Declarando dicionários
dic_cidades = {
    'cidade': (30.023, 55.034)
}

dicionario_aluno = ({
    'nome': 'João',
    'idade': 20,
    'curso': 'engenharia',
    'nota_final': 8.5
})

# lista_alunos = ({
#     'nome': 'Eva',
#     'idade': 21,
#     'curso': 'engenharia',
#     'nota_final': 8.0
# })

print(dicionario_aluno)
# print(lista_alunos)

# Adicionando um novo item ao dicionário
dicionario_aluno['endereco'] = 'Rua das flores, 123' # Basta atribuir um valor a uma nova chave para adicionar um novo par chave valor.
print(dicionario_aluno) # Agora contém a chave "endereco"

# Modificando o valor de uma chave existente
dicionario_aluno['nota_final'] = 9.0 # Basta atribuir um novo valor à chave que já existe.
print(dicionario_aluno) # O valor da chave "nota_final" foi atualizado

# Método pop() - remove o item com a chave especificada e retorna o valor removido
idade_removida = dicionario_aluno.pop('idade')
print(dicionario_aluno) # Saída: {'nome': 'João', 'curso': 'engenharia', 'nota_final': 9.0, 'endereco': 'Rua das flores, 123'}
print(idade_removida) # Saída: 20

# print(dicionario_aluno['idade']) # Saída: KeyError

# Método popitem() - remove o último item e retorna o mesmo
item = dicionario_aluno.popitem()
print(dicionario_aluno) # Saída: {'nome': 'João', 'curso': 'engenharia', 'nota_final': 9.0}
print(item) # Saída

# Keyword del - deleta qualquer coisa
del dicionario_aluno['nome']
print(dicionario_aluno) # Saída: {'curso': 'engenharia', 'nota_final': 9.0}

# Método clear() - remove todos os elementos de uma lista
limpo = dicionario_aluno.clear()
print(dicionario_aluno) # Saída: {}