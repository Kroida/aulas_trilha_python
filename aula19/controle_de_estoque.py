estoque = {}

while True:
  produto = input('Digite o nome do produto ("ou sair" para finalizar): ')

  if produto.lower() == 'sair':
    break

  quantidade = int(input(f'Digite a quantidade de {produto}: '))

  if produto in estoque:
    estoque[produto] += quantidade # Atualiza a quantidade existente

  else:
    estoque[produto] = quantidade # Adiciona novo produto

# Exibindo o inventário de estoque
for produto, quantidade in estoque.items():
  print(f'{produto}: {quantidade}')