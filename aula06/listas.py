# Declarando as listas
frutas = ['maçã', 'banana', 'laranja', 'morango', 'banana']
b = ['batata', 'cebola', 'pinhão']
print('Declarando as listas\n', frutas, '\n', b)

# Atribuindo um item à lista
frutas.append('kiwi')
print('Atribuindo um item à lista\n', frutas)

# Removendo um item da lista | Note que somente o primeiro item será removido
frutas.remove('banana')
print('Removendo um item da lista\n', frutas)

# Sobreescrevendo o índice 1
frutas[1] = 'uva'
print('Sobreescrevendo o índice 1\n', frutas)

# Atribuindo um item à lista | Repare que o item não sobreescreverá o índice 1, e sim forçará os outros itens a se deslocarem para o lado
frutas.insert(1, 'abacaxi')
print('Atribuindo um item à lista\n', frutas)

# Ordenando a lista frutas
frutas.sort()
print('Ordenando a lista frutas\n', frutas)

# Invertendo a ordem dos elementos na lista
frutas.reverse()
print('Invertendo a ordem dos elementos na lista\n', frutas)

# Percorrendo a lista frutas
print('Percorrendo a lista frutas')
for fruta in frutas:
    print(fruta)

# Somando os elementos de uma lista
notas = [8, 7.5, 9, 6, 10]
soma = 0

for nota in notas:
  soma += nota

media = soma / len(notas)
print(f'A média das notas é: {media:.2f}')