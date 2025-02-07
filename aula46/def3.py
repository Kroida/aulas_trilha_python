nome = input("Digite seu nome: ").lower()
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo (F ou M): ").lower()
estado_civil = input("Digite seu estado civil (S, C, V ou D): ").lower()

validacoes = {
    "nome": nome,
    "idade": idade,
    "salario": salario,
    "sexo": sexo,
    "estado_civil": estado_civil
}    

while True:
    print("Validando...")
    
    erros = []
    
    if len(validacoes["nome"]) < 3:
        erros.append("Nome inválido!")
    
    if not 0 <= validacoes["idade"] <= 150:
        erros.append("Idade inválida!")
    
    if salario > 0:
        erros.append("Salário inválido!")
    
    if sexo != "f" and sexo != "m":
        erros.append("Sexo inválido!")
    
    if estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
        erros.append("Estado civil inválido!")
    
    if erros:
        print("Erros encontrados:")
        for erro in erros:
            print(f"- {erro}")
        break
    
    else:
        print("Validações concluídas com sucesso!")
        break
    