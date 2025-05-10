# Exemplo de criação e uso de variável booleana
idade = 18
maior_de_idade = idade >= 18
print(maior_de_idade)

# Descrevendo exemplo de uso de booleanas com fechamento de notas
nota = 8
aprovado = nota >= 7
print(aprovado)

# Verificando se duas condições são verdadeiras
idade1 = 20
possui_carteira_de_motorista = True
pode_dirigir = idade1 >= 18 and possui_carteira_de_motorista # And só imprimirá true se ambas as afirmações forem verdadeiras

print(pode_dirigir) #Saída: True

# Usando 'or' para verificar múltiplas condições
esta_chovendo = False
tem_guarda_chuva = True

pode_sair = esta_chovendo == False or tem_guarda_chuva == True
print(pode_sair)

# Usando 'not' para inverter uma condição
esta_aberto = True
print(not esta_aberto) #Saída: false

# Exemplo de uso de variável booleana, if, elif e else para aprovação, recuperação e reprovação
nota1 = 7
resultado_final = nota1 >= 7

if resultado_final:
    print('Aprovado')
elif nota1 >= 5:
    print('Recuperação')
else:
    print('Reprovado')
    
# Exemplo de uso de variável booleana, if, elif e else para aprovação, recuperação e reprovação (avançado)
nota2 = 85

if nota2 >= 90:
    print('Nota A: excelente!')
elif nota2 >= 80:
    print('Nota B: muito bom!')
elif nota2 >= 70:
    print('Nota C: bom!')
elif nota2 >= 60:
    print('Nota D: satisfatório!')
else:
    print('Nota F: precisa melhorar!')
    
# Solicitando ao usuário um número
numero = int(input('Digite um número: '))

# Verificando se é par ou ímpar
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')
    
