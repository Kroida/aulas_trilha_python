import random
import tkinter as tk
from tkinter import messagebox

class Cartela:
    def __init__(self, tamanho, intervalo_min, intervalo_max):
        self.tamanho = tamanho
        self.intervalo_min = intervalo_min
        self.intervalo_max = intervalo_max
        self.matriz = []
        self.marcados = []
        self.gerar_cartela()

    def gerar_cartela(self):
        # Cria lista de números únicos dentro do intervalo e embaralha
        numeros = random.sample(range(self.intervalo_min, self.intervalo_max + 1), self.tamanho * self.tamanho)
        
        # Cria a matriz da cartela
        self.matriz = [numeros[i:i + self.tamanho] for i in range(0, len(numeros), self.tamanho)]
        
        # Marca o meio como livre (0)
        meio = self.tamanho // 2
        self.matriz[meio][meio] = 0 

        # Inicializa matriz de marcados como False
        self.marcados = [[False for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def marcar_numero(self, numero):
      for i in range(self.tamanho):
        for j in range(self.tamanho):
          if self.matriz[i][j] == numero:
             self.marcados[i][j] = True

    def verificar_vitoria(self):
      for row in self.marcados:
          if not all(row):
              return False
      return True


class Sorteador:
    def __init__(self, intervalo_min, intervalo_max):
        self.intervalo_min = intervalo_min
        self.intervalo_max = intervalo_max
        self.numeros = list(range(intervalo_min, intervalo_max + 1))
        random.shuffle(self.numeros)
        self.sorteados = set()

    def sortear(self):
        if self.numeros:
            numero = self.numeros.pop(0)
            self.sorteados.add(numero)
            return numero
        return None

class BingoApp:
    def __init__(self, tamanho_cartela, intervalo_min_cartela, intervalo_max_cartela, intervalo_min_sorteador, intervalo_max_sorteador):
        self.tamanho_cartela = tamanho_cartela
        self.cartela = Cartela(tamanho_cartela, intervalo_min_cartela, intervalo_max_cartela)
        self.sorteador = Sorteador(intervalo_min_sorteador, intervalo_max_sorteador)
        self.numero_sorteado = None
        
        # Cores modernas
        self.cores = {
            'primary': "#FF3B3B",      # Vermelho vibrante
            'secondary': "#2C2C2C",    # Cinza escuro
            'background': "#1A1A1A",   # Preto suave
            'text': "#FFFFFF",         # Branco
            'accent': "#FFD700",       # Dourado
            'cell_bg': "#FFFFFF",      # Branco
            'marked_bg': "#FF6B6B"     # Vermelho claro
        }

        self.root = tk.Tk()
        self.root.title("Bingo")
        self.root.configure(bg=self.cores['background'])
        
        # Configuração da janela
        largura = 600
        altura = 820
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = (altura_tela - altura) // 3
        self.root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
        
        # Container principal
        self.main_container = tk.Frame(self.root, bg=self.cores['background'])
        self.main_container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Título BINGO com efeito de sombra
        self.title_frame = tk.Frame(self.main_container, bg=self.cores['background'])
        self.title_frame.pack(pady=20)
        
        self.shadow_label = tk.Label(self.title_frame, text="BINGO", 
                                   font=("Helvetica", 48, "bold"),
                                   fg=self.cores['secondary'],
                                   bg=self.cores['background'])
        self.shadow_label.place(x=2, y=2)
        
        self.title_label = tk.Label(self.title_frame, text="BINGO",
                                  font=("Helvetica", 48, "bold"),
                                  fg=self.cores['primary'],
                                  bg=self.cores['background'])
        self.title_label.pack()

        # Frame da cartela com borda arredondada
        self.frame_cartela = tk.Frame(self.main_container, bg=self.cores['secondary'],
                                    highlightbackground=self.cores['primary'],
                                    highlightthickness=2,
                                    bd=0)
        self.frame_cartela.pack(pady=20)

        # Frame do sorteio
        self.frame_sorteio = tk.Frame(self.main_container, bg=self.cores['background'])
        self.frame_sorteio.pack(pady=0)

        # Display do número sorteado
        self.numero_sorteado_display = tk.Label(self.frame_sorteio,
                                              text="--",
                                              font=("Helvetica", 36, "bold"),
                                              width=3,
                                              fg=self.cores['primary'],
                                              bg=self.cores['secondary'],
                                              relief="flat")
        self.numero_sorteado_display.pack(pady=10)

        # Botão de sortear estilizado
        self.botao_sortear = tk.Button(self.frame_sorteio,
                                     text="SORTEAR",
                                     command=self.sortear_numero,
                                     font=("Helvetica", 14, "bold"),
                                     fg=self.cores['text'],
                                     bg=self.cores['primary'],
                                     activebackground=self.cores['secondary'],
                                     activeforeground=self.cores['text'],
                                     relief="flat",
                                     width=15,
                                     cursor="hand2")
        self.botao_sortear.pack(pady=10)

        # Frame dos números sorteados
        self.frame_numeros_sorteados = tk.Frame(self.main_container, bg=self.cores['background'])
        self.frame_numeros_sorteados.pack(pady=20)

        self.label_lista_sorteados = tk.Label(self.frame_numeros_sorteados,
                                            text="Números Sorteados",
                                            font=("Helvetica", 14),
                                            fg=self.cores['text'],
                                            bg=self.cores['background'])
        self.label_lista_sorteados.pack()

        # Frame da lista de sorteados com borda arredondada
        self.frame_lista_sorteados = tk.Frame(self.frame_numeros_sorteados,
                                            bg=self.cores['secondary'],
                                            highlightbackground=self.cores['primary'],
                                            highlightthickness=1,
                                            bd=0)
        self.frame_lista_sorteados.pack(padx=5, pady=5)

        self.coluna_atual = 0
        self.lista_sorteados_labels = []
        self.labels_cartela = []
        self.criar_cartela_interface()

    def criar_cartela_interface(self):
        for i in range(self.tamanho_cartela):
            linha_labels = []
            for j in range(self.tamanho_cartela):
                num = self.cartela.matriz[i][j]
                label = tk.Label(self.frame_cartela,
                               text=str(num),
                               width=5,
                               height=2,
                               relief="flat",
                               font=("Helvetica", 16, "bold"),
                               bg=self.cores['cell_bg'],
                               fg=self.cores['secondary'])
                label.grid(row=i, column=j, padx=3, pady=3)
                linha_labels.append(label)
            self.labels_cartela.append(linha_labels)
        
        meio = self.tamanho_cartela // 2
        self.labels_cartela[meio][meio].config(
            text="LIVRE",
            fg=self.cores['primary']
        )

    def atualizar_interface(self):
        for i in range(self.tamanho_cartela):
            for j in range(self.tamanho_cartela):
                if self.cartela.marcados[i][j]:
                    self.labels_cartela[i][j].config(
                        bg=self.cores['marked_bg'],
                        fg=self.cores['text']
                    )
        
        if self.numero_sorteado is not None:
            self.numero_sorteado_display.config(text=str(self.numero_sorteado))
            # Efeito de piscar ao mostrar novo número
            self.root.after(100, lambda: self.numero_sorteado_display.config(fg=self.cores['accent']))
            self.root.after(500, lambda: self.numero_sorteado_display.config(fg=self.cores['primary']))

    def sortear_numero(self):
        numero = self.sorteador.sortear()
        if numero is not None:
            self.numero_sorteado = numero
            self.cartela.marcar_numero(numero)
            self.atualizar_interface()
            self.adicionar_numero_sorteado_interface(numero)
            self.verificar_ganhador()
        else:
           messagebox.showinfo("Fim de Jogo", "BINGO!")
           self.botao_sortear.config(state="disabled")

    def adicionar_numero_sorteado_interface(self, numero):
        label = tk.Label(self.frame_lista_sorteados,
                        text=str(numero),
                        font=("Helvetica", 12),
                        width=3,
                        fg=self.cores['text'],
                        bg=self.cores['secondary'])
        label.grid(row=len(self.lista_sorteados_labels) // 5,
                  column=self.coluna_atual,
                  padx=3,
                  pady=3)
        self.lista_sorteados_labels.append(label)
        self.coluna_atual += 1
        if self.coluna_atual > 4:
            self.coluna_atual = 0
        self.gerenciar_lista_deslizante()

    def gerenciar_lista_deslizante(self):
        if len(self.lista_sorteados_labels) > 15:
            for i in range(5):
                label_a_remover = self.lista_sorteados_labels.pop(0)
                label_a_remover.destroy()
            self.atualizar_posicao_labels()

    def atualizar_posicao_labels(self):
        for i, label in enumerate(self.lista_sorteados_labels):
            label.grid(row=i // 5, column=i % 5, padx=3, pady=3)

    def verificar_ganhador(self):
        if self.cartela.verificar_vitoria():
            messagebox.showinfo("Vencedor!", "Parabéns, você venceu!")
            self.botao_sortear.config(state="disabled")

    def iniciar_jogo(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BingoApp(5, 1, 75, 1, 75)
    app.iniciar_jogo()