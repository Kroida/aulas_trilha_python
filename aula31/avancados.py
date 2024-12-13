# Importando biblioteca
import tkinter as tk
# Importando parte interna da biblioteca Tkinter
from tkinter import ttk

# Criando a janela principal
root = tk.Tk()
root.title("Widgets Avançados 🎨")
root.geometry("800x800")
root.configure(bg="lightgray")

# ---------------------------------------------------------------------------------------------Listbox e Scrollbar---------------------------------------------------------------------------------------------


def exibir_selecao():
	selecionado = listbox.get(listbox.curselection())  # Obtém o item selecionado
	label_resultado.config(text=f"Você selecionou: {selecionado}")


# Adicionando um título
label_titulo = tk.Label(root, text="Selecione um item da lista", font=("Arial", 20), bg="lightgray")
label_titulo.pack(pady=10)

# Criando um Frame para Listbox e Scrollbar
frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

# Criando a Scrollbar
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)

# Criando a Listbox
listbox = tk.Listbox(frame_listbox, font=('Arial', 20), height=6, yscrollcommand=scrollbar.set, selectbackground='green', selectforeground='white', activestyle='dotbox')

# Vinculando a Scrollbar à Listbox
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Adicionando itens à Listbox
# itens = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go", "Swift", "Kotlin"]
itens = {
    'Python': '🐍',
    'Java': '☕',
    'C++': '⚙️',
    'Ruby': '💎',
    'JavaScript': '⚡️',
    'Go': '➡️',
    'Swift': '↗️',
    'Kotlin': '🤖'
}

# Inserindo itens no Listbox
for chave, valor in itens.items():
    listbox.insert(tk.END, chave + " " + valor)

# Botão para exibir o item selecionado
botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 12), bg="green", fg="white", command=exibir_selecao)
botao_exibir.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_resultado.pack(pady=10)

# ----------------------------------------------------------------------------------------Radiobutton e Checkbutton---------------------------------------------------------------------------------------------


def exibir_opcoes():
	linguagem = var_radio.get()
	preferencias = []
	if var_check1.get():
		preferencias.append("Dark Mode")
	if var_check2.get():
		preferencias.append("Auto Save")
		label_opcoes.config(text=f"Linguagem: {linguagem}\nPreferências: {', '.join(preferencias)}")


# Criando Radiobuttons
var_radio = tk.StringVar(value="Python")
label_radio = tk.Label(root, text="Escolha sua linguagem favorita:", font=("Arial", 12), bg="lightgray")
label_radio.pack(pady=10)

for linguagem in ["Python", "Java", "C++"]:
	rb = tk.Radiobutton(root, text=linguagem, variable=var_radio, value=linguagem, bg="lightgray")
	rb.pack(anchor=tk.CENTER)

# Criando Checkbuttons
var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()
label_check = tk.Label(root, text="Selecione suas preferências:", font=("Arial", 12), bg="lightgray")
label_check.pack(pady=10)

check1 = tk.Checkbutton(root, text="Dark Mode", variable=var_check1, bg="lightgray")
check2 = tk.Checkbutton(root, text="Auto Save", variable=var_check2, bg="lightgray")
check1.pack(anchor=tk.CENTER)
check2.pack(anchor=tk.CENTER)

# Botão para exibir as opções selecionadas
botao_opcoes = tk.Button(root, text="Exibir Opções", font=("Arial", 12), bg="blue", fg="white", command=exibir_opcoes)
botao_opcoes.pack(pady=10)

# Label para mostrar o resultado
label_opcoes = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_opcoes.pack(pady=10)

root.mainloop()