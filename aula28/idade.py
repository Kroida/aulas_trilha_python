import tkinter as tk

root = tk.Tk()
root.title("Atividade: Captura de Idade")
root.geometry("400x300")
root.configure(bg="lightyellow")

def exibir_idade():
	idade = entrada_idade.get()
	print(f"A idade inserida foi: {idade} 🎂")

def limpar_idade():
	entrada_idade.delete(0, tk.END)

label_idade = tk.Label(root, text="Digite sua idade:", font=("Arial", 14), bg="lightyellow")
label_idade.pack(pady=10)

entrada_idade = tk.Entry(root, font=("Arial", 14))
entrada_idade.pack(pady=10)

botao_exibir = tk.Button(root, text="Exibir", font=("Arial", 14), bg="green", fg="white", command=exibir_idade)
botao_exibir.pack(pady=5)

botao_limpar = tk.Button(root, text="Limpar", font=("Arial", 14), bg="red", fg="white", command=limpar_idade)
botao_limpar.pack(pady=5)

root.mainloop()