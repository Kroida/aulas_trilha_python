while True:
    valor = int(input("Digite um número: "))
    
    if not 0 <= valor <= 10:
        print("Valor inválido. Digite um número entre 0 e 10.")
        continue
    else:
        print("Valor válido.")
        break