# Desafio v6 - Luís

# ----------------------
# Manual do Código:
# Este código permite que o usuário insira uma lista de nomes, organizando-os em ordem alfabética e exibindo-os
# com a posição numérica de cada um. Quando o usuário finaliza a entrada, o console é limpo para exibir apenas o
# resultado final, seguido da quantidade total de participantes.
# ----------------------

# ----------------------
# Passo a passo do código:
# ----------------------

from IPython.display import clear_output  # Importa a função para limpar o console no Google Colab

nomes = []  # Inicializa a lista que armazenará os nomes

while True:  # Inicia um loop que continuará até que o usuário decida parar a inserção de nomes
  entrada = input('Digite o nome que você deseja inserir ou S para sair: ').upper()  # Solicita o nome e converte a entrada para maiúsculas para simplificar a verificação

  if entrada == 'S':  # Verifica se a entrada é 'S' (indicando que o usuário quer parar)
    nomes.sort()  # Ordena os nomes em ordem alfabética
    clear_output()  # Limpa o console para exibir somente o resultado final
    break  # Sai do loop, finalizando a entrada de dados

  nomes.append(entrada)  # Adiciona o nome à lista se a entrada não for 'S'

print('~~~ Lista de nomes ~~~')  # Imprime o título para a lista de nomes

for j, i in enumerate(nomes):  # Percorre a lista usando enumerate para obter o índice e o nome
  print(f'P{j+1} - {i.capitalize()}')  # Exibe cada nome com o índice (posição de cada participante) e a primeira letra em maiúscula

print(f'\nParticipantes totais: {len(nomes)}')  # Exibe o total de participantes na lista