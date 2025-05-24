# Sistema de controle de estoque

# Objetivo: criar um pequeno sistema para controlar o estoque atualizando listas e tuplas como exemplo para manipular e armazenar informação dos itens.

# Feito com o Professor
# Lista para armazenar os itens de estoque, onde cada item será uma tupla(nome, quantidade, preço)
estoque = [
    ('Lápis', 100, 1.50),
    ('Caneta', 200, 2.00),
    ('Caderno', 50, 10.00),
    ('Borracha', 150, 0.75)
]

# Função para exibir o menu principal
def menu_principal():
  print('\n=== SISTEMA DE CONTROLE DE ESTOQUE ===')
  print('1. Visualizar estoque')
  print('2. Adicionar item ao estoque')
  print('3. Atualizar quantidade do item do estoque')
  print('4. Remover item do estoque')
  print('5. Sair')
  opcao = int(input('Escolha uma opção: '))

  if opcao == 1:
    visualizar_estoque()
  elif opcao == 2:
    adicionar_item()
  elif opcao == 3:
    atualizar_quantidade()
  elif opcao == 4:
    remover_item()
  elif opcao == 5:
    print('Saindo...')
    exit()
  else:
    print('Opção inválida!')

# Função visualizar estoque
def visualizar_estoque():
  print('\n=== ESTOQUE ATUAL ===')
  for item in estoque:
    nome, quantidade, preco = item
    print(f'Nome: {nome}, Quantidade: {quantidade}, Preço: R$ {preco:.2f}')

# Função adicionar item ao estoque
def adicionar_item():
  nome = input('Digite o nome do item: ')
  quantidade = int(input('Digite a quantidade do item: '))
  preco = float(input('Digite o preço do item: '))
  novo_item = (nome, quantidade, preco)
  estoque.append(novo_item)
  print(f'O item {nome} foi adicionado ao estoque.')

def atualizar_quantidade():
  nome = input('Digite o nome do item que deseja atualizar a quantidade: ')
  for i, item in enumerate(estoque):
    if item[0].lower() == nome.lower():
      nova_quantidade = int(input('Digite a nova quantidade do item: '))
      # Criando uma tupla com os valores atualizados
      estoque[i] = (item[0], nova_quantidade, item[2])
      print(f'A quantidade do item {item[0]} foi atualizada para {nova_quantidade}.')
      break
    else:
      print('Não encontrado')
      break

def remover_item():
  nome = input('Digite o nome do item que deseja remover: ')
  for i, item in enumerate(estoque):
    if item[0].lower() == nome.lower():
      estoque.pop(i)
      print(f'O item {nome} foi removido do estoque.')
      break
    else:
      print('Não encontrado')
      break

if __name__ == '__main__':
  menu_principal()