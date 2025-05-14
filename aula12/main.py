from IPython.display import clear_output # biblioteca para limpar a tela

# Lista vazia para armazenar as tarefas
tarefas = []

# Loop para interagir com o usuário
while True:
    print("Menu de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Visualizar Tarefas Ordenadas")
    print("4. Sair")

    try:
      opcao = int(input("Escolha uma opção: "))
    except:
      clear_output()
      print("Opção inválida. Tente novamente.\n")
      continue

    if opcao == 1:
        # Adicionar tarefa
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        clear_output()
        print(f"Tarefa '{tarefa}' adicionada com sucesso!\n")
    elif opcao == 2:
        # Remover tarefa
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            clear_output()
            print(f"Tarefa '{tarefa}' removida com sucesso!\n")
        else:
            clear_output()
            print(f"Tarefa '{tarefa}' não encontrada na lista.\n")
    elif opcao == 3:
        if len(tarefas) == 0:
          clear_output()
          print('Não há tarefas na lista.\n')
        else:
          # Visualizar tarefas ordenadas
          tarefas.sort()
          clear_output()
          print("Tarefas Ordenadas:")
          for tarefa in tarefas:
              print(f"- {tarefa}")
          print()
    elif opcao == 4:
        # Sair do programa
        clear_output()
        print("Saindo do programa...")
        break
    else:
        clear_output()
        print("Opção inválida. Tente novamente.\n")