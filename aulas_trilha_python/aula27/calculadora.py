import tkinter as tk

root = tk.Tk()
root.title("Calculadora Simples 📏")
root.geometry("800x300")
root.configure(bg="#272727")

label_titulo = tk.Label(root, text="Calculadora Simples", font=("Arial", 16), bg="#272727", fg='#dc143c')
label_titulo.pack(pady=10)

entrada1 = tk.Entry(root, font=("Arial", 14), fg="#f5002d")
entrada1.pack(pady=5)
entrada2 = tk.Entry(root, font=("Arial", 14), fg="#f5002d")
entrada2.pack(pady=5)

def somar():
	try:
		num1 = float(entrada1.get())
		num2 = float(entrada2.get())
		resultado = num1 + num2
		label_resultado.config(text=f"Resultado: {resultado}")
	except ValueError:
		label_resultado.config(text="Por favor, insira números válidos!", fg='#dc143c')

botao_somar = tk.Button(root, text="Somar", font=("Arial", 14), bg="#a0203a", fg="white", command=somar)
botao_somar.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 14), bg="#272727")
label_resultado.pack(pady=10)

root.mainloop()
  
