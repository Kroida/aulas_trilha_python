# Importando a biblioteca tkinter que é usada para criar aplicativos GUI
import tkinter as tk
# Importando o módulo ttk do tkinter para widgets temáticos
from tkinter import ttk

# Criando a janela principal do aplicativo
root = tk.Tk()

# Definindo o título da janela
root.title("Widgets Avançados 🎨")

# Definindo o tamanho da janela
root.geometry("1024x800")

# Maximiza automaticamente a janela
root.state('zoomed')

# Definindo a cor de fundo da janela
root.configure(bg="lightgray")

# ---------------------------------------------------------------------------------------------Listbox e Scrollbar---------------------------------------------------------------------------------------------


# Função para exibir o item selecionado da listbox
def exibir_selecao():
    # Obtendo o item selecionado da listbox
	selecionado = listbox.get(listbox.curselection())  # Obtém o item selecionado
 	# Atualizando o rótulo de resultado com o item selecionado
	label_resultado.config(text=f"Você selecionou: {selecionado}")


# Criando um widget de rótulo com o texto "Selecione um item da Lista"
# Definindo a fonte para Arial, tamanho 24, e cor de fundo para cinza claro
label_titulo = tk.Label(root, text="Selecione um item da lista", font=("Arial", 20), bg="lightgray")
# Colocando o rótulo na janela com algum espaçamento
label_titulo.pack(pady=10)

# Criando um frame para conter a listbox e sua barra de rolagem
frame_listbox = tk.Frame(root)

# Colocando o frame na janela com algum espaçamento
frame_listbox.pack(pady=10)

# Criando um widget de barra de rolagem e associando-o ao frame
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)

# Criando um widget de listbox e associando-o ao frame
listbox = tk.Listbox(frame_listbox, font=('Arial', 20), height=6, yscrollcommand=scrollbar.set, selectbackground='green', selectforeground='white', activestyle='dotbox')

# Configurando a barra de rolagem para funcionar com a listbox
scrollbar.config(command=listbox.yview)

# Colocando a barra de rolagem no lado direito e fazendo-a preencher o eixo Y
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Colocando a listbox no lado esquerdo e fazendo-a preencher os eixos X e Y
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Definindo um dicionário com linguagens de programação como chaves e seus emojis como valores
# A linha comentada mostra uma lista alternativa de itens sem emojis
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
# itens = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go", "Swift", "Kotlin"]

# Iterando sobre os itens do dicionário (linguagem e emoji)
for chave, valor in itens.items():
    # Inserindo cada linguagem e seu emoji na listbox
    listbox.insert(tk.END, chave + " " + valor)

# Criando um widget de botão rotulado "Exibir Seleção"
# Definindo a fonte para Arial, tamanho 18, cor de fundo para verde, e cor do texto para branco
# Associando o botão à função exibir_selecao para exibir o item selecionado
botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 24), bg="green", fg="white", command=exibir_selecao)
# Colocando o botão na janela com algum espaçamento
botao_exibir.pack(pady=10)

# Criando um widget de rótulo para exibir o resultado da seleção
# Definindo a fonte para Arial, tamanho 12, e cor de fundo para cinza claro
label_resultado = tk.Label(root, text="", font=("Arial", 20), bg="lightgray")
# Colocando o botão na janela com algum espaçamento
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


frame_lc = tk.Frame(root, bg='lightgray')
frame_lc.pack(pady=10)

# Criando Radiobuttons
var_radio = tk.StringVar(value="Python")
label_radio = tk.Label(frame_lc, text="Escolha sua linguagem favorita:", font=("Arial", 20), bg="lightgray")
label_radio.pack(pady=10)

for linguagem in ["Python", "Java", "C++"]:
	rb = tk.Radiobutton(frame_lc, text=linguagem, font=("Arial", 20), variable=var_radio, value=linguagem, bg="lightgray")
	rb.pack(anchor=tk.W)

# Criando Checkbuttons
var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()
label_check = tk.Label(frame_lc, text="Selecione suas preferências:", font=("Arial", 20), bg="lightgray")
label_check.pack(pady=10)

check1 = tk.Checkbutton(frame_lc, text="Dark Mode", font=("Arial", 20), variable=var_check1, bg="lightgray")
check2 = tk.Checkbutton(frame_lc, text="Auto Save", font=("Arial", 20), variable=var_check2, bg="lightgray")
check1.pack(anchor=tk.W)
check2.pack(anchor=tk.W)

# Botão para exibir as opções selecionadas
botao_opcoes = tk.Button(frame_lc, text="Exibir Opções", font=("Arial", 24), bg="blue", fg="white", command=exibir_opcoes)
botao_opcoes.pack(pady=10)

# Label para mostrar o resultado
label_opcoes = tk.Label(frame_lc, text="", font=("Arial", 20), bg="lightgray")
label_opcoes.pack(pady=10)

# ------------------------------------------------------------------------------------------------------- Combobox ---------------------------------------------------------------------------------------------------------------------

# Função para exibir a seleção da Combobox
def exibir_combobox():
    selecao = combobox.get()  # Obtém o valor selecionado
    label_combobox.config(text=f"Você escolheu: {selecao}")

# Label de instrução
label_combobox_instrucao = tk.Label(root, text="Escolha uma IDE da lista:", font=("Arial", 12), bg="lightgray")
label_combobox_instrucao.pack(pady=10)

# Combobox
combobox = ttk.Combobox(root, values=["PyCharm", "VSCode", "Eclipse", "IntelliJ"])
combobox.pack(pady=5)
combobox.set("PyCharm")  # Valor inicial

# Label para exibir a escolha
label_combobox = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
label_combobox.pack(pady=10)

# Botão para exibir a seleção
botao_combobox = tk.Button(root, text="Exibir Escolha", font=("Arial", 12), bg="purple", fg="white", command=exibir_combobox)
botao_combobox.pack(pady=10)

# Iniciando o loop de eventos do Tkinter para executar o aplicativo
root.mainloop()