# Widgets for the GUI
import tkinter as tk

# Cria a janela principal da aplicação
root = tk.Tk()
root.title('Widgets')
root.geometry('450x550')
root.configure(bg="#272727")

# Adiciona um rótulo, uma entrada de texto e um botão
label = tk.Label(root, text="Bem-vindo ao Tkinter!", font=("Arial", 20), bg="#272727", fg="#dc143c")
label.pack(pady=20)  # Exibindo o rótulo com espaçamento vertical

# Adiciona uma entrada de texto
entrada = tk.Entry(root, font=("Arial", 14), fg='#f5002d')
entrada.pack(pady=10)  # Exibindo a entrada com espaçamento vertical

# Adiciona um botão
botao = tk.Button(root, text="Clique Aqui!", font=("Arial", 14), bg="#a0203a", fg="white", command=lambda: print("Botão Clicado!"))
botao.pack(pady=10)  # Exibindo o botão com espaçamento vertical

# Função para exibir o texto inserido na entrada
def exibir_texto():
	texto = entrada.get()  # Obtendo o texto inserido pelo usuário
	print(f"Você digitou: {texto}")

# Adiciona um botão para exibir o texto inserido
botao_exibir = tk.Button(root, text="Exibir Texto", font=("Arial", 14), bg="#a0203a", fg="white", command=exibir_texto)
botao_exibir.pack(pady=10)

root.mainloop()