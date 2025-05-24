# Crie uma tupla contendo os dias da semana e permita que o usuário escolha um número de 1 a 7 para exibir o dia correspondente.

# Código feito pelo professor
dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

# Solicitando ao usuário um número de 1 a 7
dia_numero = int(input("Digite um número de 1 a 7 para ver o dia da semana: "))

# Exibindo o dia correspondente | Verifica se o valor digitado pelo usuário está dentro do intervalo de 1 a 7.
if 1 <= dia_numero <= 7:
    print(f"O dia correspondente é: {dias_da_semana[dia_numero - 1]}") # Se o usuário digitar 1, o programa acessa dias_da_semana[0], que é "Domingo".
else:
    print("Número inválido! Por favor, insira um número de 1 a 7.")