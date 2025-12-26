import tkinter as tk  # Importa o módulo tkinter para criar interfaces gráficas

# Cria a janela principal da aplicação
root = tk.Tk()

# Define o título da janela
root.title("Minha Primeira Janela Tkinter")

# Define o ícone da janela (certifique-se de que o arquivo 'fruta.ico' esteja no mesmo diretório do script)
root.iconbitmap('fruta.ico')

# Define o tamanho da janela: 400 pixels de largura por 300 pixels de altura
root.geometry("400x300")

# Define a cor de fundo da janela como azul claro
root.configure(bg="lightblue")

# Inicia o loop principal para exibir a janela e mantê-la aberta
root.mainloop()