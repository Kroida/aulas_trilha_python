total = 0.0

while True:
  preco = float(input('Digite o preço do item(ou 0 para finalizar): '))
  if preco == 0:
    break
  total += preco
print(f'O total da compra é: R$ {total:.2f}') # ':.2f' declara as casas decimais depois da vírgula