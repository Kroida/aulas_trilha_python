# Widgets for the GUI

import tkinter as tk

root = tk.Tk()
root.title('Widgets')
root.geometry('800x600')
root.configure(bg="#272727")

label = tk.Label(root, text="Bem-vindo ao Tkinter!", font=("Arial", 16), bg="#272727", fg="#dc143c")
label.pack(pady=20)  # Exibindo o rótulo com espaçamento vertical

entrada = tk.Entry(root, font=("Arial", 14), fg='#f5002d')
entrada.pack(pady=10)  # Exibindo a entrada com espaçamento vertical

botao = tk.Button(root, text="Clique Aqui!", font=("Arial", 14), bg="#a0203a", fg="white", command=lambda: print("Botão Clicado!"))
botao.pack(pady=10)  # Exibindo o botão com espaçamento vertical

def exibir_texto():
	texto = entrada.get()  # Obtendo o texto inserido pelo usuário
	print(f"Você digitou: {texto}")
 
botao_exibir = tk.Button(root, text="Exibir Texto", font=("Arial", 14), bg="#a0203a", fg="white", command=exibir_texto)
botao_exibir.pack(pady=10)

root.mainloop()