import tkinter as tk

# Criando uma função com a janela grid
def criar_interface_grid():
    # janela_grid = tk.TopLevel(root)
    janela_grid = tk.Tk()
    janela_grid.title('Gerenciar grid() 📐')
    janela_grid.configure(bg='lightblue')
    # janela_grid.geometry('300x300')

    # Criando widgets com grid()
    tk.Label(janela_grid, text='Row 0, Col 0', bg='red', fg='white').grid(row=0, column=0, padx=5, pady=5)

    tk.Label(janela_grid, text="Row 0, Col 1", bg="green", fg="white").grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela_grid, text="Row 1, Col 0", bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)

    tk.Label(janela_grid, text="Row 1, Col 1", bg="purple", fg="white").grid(row=1, column=1, padx=5, pady=5)

    tk.Button(janela_grid, text='Fechar', command=janela_grid.destroy).grid(row=2, column=0, columnspan=2, pady=10)
    
    return janela_grid

if __name__ == '__main__':
    janela = criar_interface_grid()
    janela.mainloop()


