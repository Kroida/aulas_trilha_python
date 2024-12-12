# Importa o módulo Tkinter para criar interfaces gráficas
import tkinter as tk

# Cria a janela principal da aplicação
root = tk.Tk()
root.title('Interface interativa')  # Define o título da janela
root.geometry('800x600')  # Define o tamanho da janela (largura x altura)
root.configure(bg='#f7f7f7')  # Configura a cor de fundo da janela

# Função chamada ao clicar no botão
def botao_clique():
    # Exibe uma mensagem no console indicando que o botão foi clicado
    print('Ocê clicou no butaum sô 🤠')

# Função chamada ao pressionar uma tecla
def atualizar_label(event):
    """
    Atualiza a cor e o texto da label com a tecla pressionada.
    Parâmetros:
        event (tk.Event): Evento que contém informações sobre a tecla pressionada.
    """
    # Atualiza o texto da label com o caractere da tecla pressionada
    label_resultado.config(text=f"Tecla pressionada: {event.char}")

# Cria uma label de instrução na janela
label = tk.Label(
    root,
    text='Pressione qualquer tecla ou clique no botão',  # Texto exibido na label
    font=('Arial', 20),  # Fonte e tamanho do texto
    bg='#f7f7f7',  # Cor de fundo da label (igual à cor da janela)
    fg='#272727'  # Cor do texto
)
label.pack(pady=20)  # Adiciona a label à janela com espaçamento vertical (padding)

# Cria uma label para exibir o resultado das teclas pressionadas
label_resultado = tk.Label(
    root,
    text="",  # Inicialmente sem texto
    font=("Arial", 14),  # Fonte e tamanho do texto
    bg="#f7f7f7",  # Cor de fundo (igual à janela)
    fg='#272727'  # Cor do texto
)
label_resultado.pack(pady=10)  # Adiciona a label à janela com espaçamento vertical (padding)

# Cria um botão que executa a função `botao_clique` quando clicado
button = tk.Button(
    root,
    text='Clicar',  # Texto exibido no botão
    font=('Arial', 14),  # Fonte e tamanho do texto
    bg='#dc143c',  # Cor de fundo do botão
    fg='#f7f7f7',  # Cor do texto
    command=botao_clique  # Define a função a ser executada ao clicar no botão
)
button.pack(pady=10)  # Adiciona o botão à janela com espaçamento vertical (padding)

# Vincula o evento de pressionar uma tecla à função `atualizar_label`
root.bind("<Key>", atualizar_label)

# Inicia o loop principal da aplicação, mantendo a janela aberta
root.mainloop()