import tkinter as tk

# Criando a janela principal
root = tk.Tk()
root.title("Eventos e Interatividade 🎯")
root.geometry("400x300")
root.configure(bg="lightgray")


# Função callback para o evento do botão
def ao_clicar():
    print("Botão foi clicado! 🚀")


# Capturando eventos do teclado
def ao_pressionar_tecla(event):
    print(f"Você pressionou: {event.char} 🆘")


# Eventos do Mouse
def ao_mover_mouse(event):
    print(f"Mouse em: x={event.x}, y={event.y}")


# Criando um botão com interatividade
botao = tk.Button(
    root,
    text="Clique Aqui!",
    font=("Arial", 14),
    bg="green",
    fg="white",
    command=ao_clicar
)
botao.pack(pady=20)

# Associando o evento de teclado à janela principal
root.bind("<w>", ao_pressionar_tecla)

# Associando o evento de movimento do mouse à janela principal
root.bind("<Motion>", ao_mover_mouse)

root.mainloop()
