# Crie uma função que receba duas notas de um aluno e retorne a média, além da maior e menor nota, como uma tupla.
def analise_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    maior = max(nota1, nota2)
    menor = min(nota1, nota2)
    return media, maior, menor  # Retornando os valores como uma tupla

# Solicitando ao usuário as notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Obtendo os resultados e exibindo
resultado = analise_notas(n1, n2) # Tupla para armazenar as notas retornadas

# É interessante ver que a tupla pegou e armazenou todos os dados retornados, contudo você não irá conseguir retorna-los como variáveis e sim como índices por meio do slicing
print(f"Média: {resultado[0]}, Maior Nota: {resultado[1]}, Menor Nota: {resultado[2]}")