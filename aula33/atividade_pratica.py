import tkinter as tk

root = tk.Tk()
root.title('Atividade prática')
root.geometry('400x300')
root.configure(bg='#212121')

def atividade_pratica():
    janela_atividade = tk.Toplevel(root)
    janela_atividade.title('Atividade Prática 🛠️')
    janela_atividade.geometry('400x400')
    janela_atividade.configure(bg='#212121')
    
    # Título com pack()
    titulo = tk.Label(janela_atividade, text='Interface Combinada', font=('Arial', 20), bg='#212121', fg='#f7f7f7')
    titulo.pack(fill=tk.X, pady=10)

    frame_grid = tk.Frame(janela_atividade)
    frame_grid.pack(pady=5)
    
    dados = [
        ["ID", "Nome", "Idade", "País"],
        [1, "João", 25, "Brasil"],
    ]
    
    # Configurações de estilo para os títulos e linhas
    header_bg = "#dc143c"  # Cor de fundo do cabeçalho
    header_fg = "white"    # Cor do texto do cabeçalho
    row_bg1 = "#f2f2f2"    # Cor de fundo das linhas ímpares
    row_bg2 = "#ffffff"    # Cor de fundo das linhas pares
    
    # Criando a tabela com grid
    for i, linha in enumerate(dados):
        for j, valor in enumerate(linha):
            if i == 0:  # Estiliza o cabeçalho
                cell = tk.Label(
                    frame_grid,
                    text=valor,
                    bg=header_bg,
                    fg=header_fg,
                    font=("Arial", 12, "bold"),
                    padx=10,
                    pady=5,
                    borderwidth=1,
                    relief="solid"
                )
            else:  # Estiliza as linhas de dados
                bg_color = row_bg1 if i % 2 == 0 else row_bg2
                cell = tk.Label(
                    frame_grid,
                    text=valor,
                    bg=bg_color,
                    fg="black",
                    font=("Arial", 11),
                    padx=10,
                    pady=5,
                    borderwidth=1,
                    relief="solid"
                )
            cell.grid(row=i, column=j, sticky="nsew", ipadx=5, ipady=5)

    # Ajustando o tamanho das colunas dinamicamente
    for coluna in range(len(dados[0])):
        root.grid_columnconfigure(coluna, weight=1)

    # Botões com place()
    tk.Button(janela_atividade, text='Fechar', font=('Arial', 14), bg='#dc143c', fg='#f7f7f7', command=janela_atividade.destroy).place(x=150, y=300, width=100, height=30)


btn_atividade = tk.Button(root, text='Atividade Prática', font=('Arial', 14), bg='#dc143c', fg='#f7f7f7', command=atividade_pratica)
btn_atividade.pack(pady=20)

root.mainloop()