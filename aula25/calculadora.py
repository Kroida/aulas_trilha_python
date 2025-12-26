# Importa o módulo tkinter e o apelida de tk, usado para criar interfaces gráficas em Python
import tkinter as tk

# Cria a janela principal da aplicação
root = tk.Tk()
root.title("Calculadora Simples 📏")
root.geometry("450x550")
root.configure(bg="#272727")

# Cria um rótulo (label) para o título da calculadora
label_titulo = tk.Label(root, text="Calculadora Simples", font=("Arial", 20), bg="#272727", fg='#dc143c')
label_titulo.pack(pady=15)

# Cria os campos de entrada para os números
entrada1 = tk.Entry(root, font=("Arial", 14), fg="#f5002d")
entrada1.pack(pady=15)
entrada2 = tk.Entry(root, font=("Arial", 14), fg="#f5002d")
entrada2.pack(pady=10)

# Função chamada ao clicar no botão "Somar"
def somar():
	try:
		# Obtém os valores dos campos de entrada e converte para float
		num1 = float(entrada1.get())
		num2 = float(entrada2.get())
		# Realiza a soma
		resultado = num1 + num2
		# Exibe o resultado na label
		label_resultado.config(text=f"Resultado: {resultado}")
	except ValueError:
		# Caso o valor inserido não seja um número válido
		label_resultado.config(text="Por favor, insira números válidos!", fg='#dc143c')

# Cria o botão que executa a soma ao ser clicado
botao_somar = tk.Button(root, text="Somar", font=("Arial", 14), bg="#a0203a", fg="white", command=somar)
botao_somar.pack(pady=10)

# Label para exibir o resultado ou mensagens de erro
label_resultado = tk.Label(root, text="", font=("Arial", 14), bg="#272727")
label_resultado.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
  
