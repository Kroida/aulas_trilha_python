while True:
    nome_de_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    
    if nome_de_usuario == senha:
        print('Você não pode usar a mesma senha que o nome de usuário e vice versa.')
    else:
        print('Senha cadastrada com sucesso.')
        break