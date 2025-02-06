nome = input("Digite seu nome: ").lowercase()
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo (F ou M): ").lowercase()
estado_civil = input("Digite seu estado civil (S, C, V ou D): ").lowercase()

validacoes = {
    'nome': nome,
    'idade': idade,
    'salario': salario,
    'sexo': sexo,
    'estado_civil': estado_civil
}    

while True:
    print('Validando...')
    if len(validacoes['nome']) < 3:
        print('Nome inválido!')
        break
    elif not 0 <= validacoes['idade'] <= 150:
        print('Idade inválida!')
        break
    elif salario > 0:
        print('Salário inválido!')
        break
    elif sexo != 'f' and sexo != 'm':
        print('Sexo inválido!')
        break
    elif estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        print('Estado civil inválido!')
        break
    else:
        print('Validações concluídas com sucesso!')
        break
    