def paresim():
    numeros = [int(input(f'Digite o {i}º número: ')) for i in range(1, 11)]

    pares = [i for i in numeros if i % 2 == 0]

    impares = [i for i in numeros if i % 2 != 0]
    
    return print(f'Números pares: {pares}', f'Números ímpares {impares}', sep='\n')

paresim()