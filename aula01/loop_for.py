# Exemplo 1: Imprimindo os números pares de 1 a 20
for i in range(2, 21, 2): # range(2, 21, 2): Cria uma sequência de números pares de 2 a 20.
    print(i)


# Exemplo 2: Pedindo ao usuário para digitar 5 números e calculando a soma
soma = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    soma += numero
print("A soma dos números é:", soma)