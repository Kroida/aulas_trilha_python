# Iterando sobre os itens do dicionário usando items()
dicionario_aluno = ({
    'nome': 'João',
    'idade': 20,
    'curso': 'engenharia',
    'nota_final': 8.5
})

for chave, valor in dicionario_aluno.items():
    print(f'chave: {chave} | valor: {valor}')
    
# Desmembrando os índices do dicionário
emon, edadi, osruc, lanif_aton = dicionario_aluno
print(emon)
print(edadi)
print(osruc)
print(lanif_aton)

# Desmembrando o dicionário
emon, edadi, osruc, lanif_aton = dicionario_aluno.items()
print(emon)
print(edadi)
print(osruc)
print(lanif_aton)

# Iterando sobre as chaves do dicionário usando keys()
for chave in dicionario_aluno.keys():
    print(f'chave: {chave}')
    
# Iterando sobre os valores do dicionário usando values()
for valor in dicionario_aluno.values():
    print(f'valor: {valor}')