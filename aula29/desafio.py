import random
import tkinter as tk
from tkinter import messagebox, ttk

# Definindo variáveis
dados = {str(i): random.randint(1, 6) for i in range(1, 6)}
dados_guardados = {}
pontuacao_total = {}
tentativas = 3
rodada = 1

# Definindo cores
BACKGROUND_COLOR = '#212121'
TEXT_COLOR = '#00ff40'
BUTTON_HOVER_COLOR = '#303030'
BUTTON_ACTIVE_COLOR = '#404040'

# Instanciando janela
root = tk.Tk()
root.title('Jogo General')

# Definindo o tamanho da janela
largura = 800
altura = 600

# Obtendo o tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Calculando a posição x e y para centralizar
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

# Definindo a geometria da janela centralizada
root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

# Configurando a cor de fundo da janela
root.configure(bg=BACKGROUND_COLOR)

# Função para criar representação visual do dado
def criar_dado(parent, valor):
    dado_frame = tk.Frame(parent, width=60, height=60, bg='white', relief='raised', bd=2)
    dado_frame.pack_propagate(False)
    
    # Layout dos pontos do dado
    pontos = {
        1: [(30, 30)],
        2: [(15, 15), (45, 45)],
        3: [(15, 15), (30, 30), (45, 45)],
        4: [(15, 15), (15, 45), (45, 15), (45, 45)],
        5: [(15, 15), (15, 45), (30, 30), (45, 15), (45, 45)],
        6: [(15, 15), (15, 30), (15, 45), (45, 15), (45, 30), (45, 45)]
    }
    
    # Criar canvas para desenhar o dado
    canvas = tk.Canvas(dado_frame, width=60, height=60, bg='white', highlightthickness=0)
    canvas.pack(fill='both', expand=True)
    
    # Desenhar os pontos
    for x, y in pontos[valor]:
        canvas.create_oval(x-4, y-4, x+4, y+4, fill='black')
    
    return dado_frame

# Função para efeito hover nos botões
def on_enter(e):
    e.widget['background'] = BUTTON_HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BACKGROUND_COLOR

# Funções de cada opção
def calcular_pontuacao(dados_guardados):
    valores = sorted(dados_guardados.values())
    if len(dados_guardados) < 5:
        return 0

    if valores in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
        messagebox.showinfo("Pontuação", "Sequência Baixa! (+20 pontos)")
        return 20
    elif len(set(valores)) == 2 and valores.count(valores[0]) in [2, 3]:
        messagebox.showinfo("Pontuação", "Full House! (+30 pontos)")
        return 30
    elif any(valores.count(v) == 4 for v in valores):
        messagebox.showinfo("Pontuação", "Quadra! (+40 pontos)")
        return 40
    elif len(set(valores)) == 1:
        messagebox.showinfo("Pontuação", "General! (+50 pontos)")
        return 50
    messagebox.showinfo("Pontuação", "Nenhuma combinação especial encontrada.")
    return 0

def organizar_dados():
    global tentativas, dados, dados_guardados, rodada
    pontos = calcular_pontuacao(dados_guardados)
    pontuacao_total[rodada] = pontos
    messagebox.showinfo("Pontuação", f"Pontuação da rodada {rodada}: {pontos}")

    dados.update(dados_guardados)
    dados_guardados.clear()
    tentativas = 3
    rodada += 1
    atualizar_interface()

def jogar_dados():
    global tentativas
    if tentativas <= 0:
        messagebox.showwarning("Aviso", "Você não tem mais tentativas!")
        return

    # Criar uma nova janela para mostrar os dados
    janela_dados = tk.Toplevel(root)
    janela_dados.title("Jogar Dados")
    janela_dados.geometry("500x600")
    janela_dados.configure(bg=BACKGROUND_COLOR)
    
    # Frame principal
    main_dados_frame = tk.Frame(janela_dados, bg=BACKGROUND_COLOR)
    main_dados_frame.pack(expand=True, fill='both', padx=20, pady=20)
    
    # Título
    titulo = tk.Label(
        main_dados_frame,
        text="Seus Dados",
        font=('Arial', 16, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    )
    titulo.pack(pady=(0, 20))

    # Frame para os dados
    frame_dados = tk.Frame(main_dados_frame, bg=BACKGROUND_COLOR)
    frame_dados.pack(pady=20)

    # Mostrar os dados disponíveis
    for num, valor in dados.items():
        frame_dado = tk.Frame(frame_dados, bg=BACKGROUND_COLOR)
        frame_dado.pack(pady=10)
        
        # Criar representação visual do dado
        dado_visual = criar_dado(frame_dado, valor)
        dado_visual.pack(side=tk.LEFT, padx=10)
        
        # Label com número do dado
        tk.Label(
            frame_dado,
            text=f'Dado {num}',
            font=('Arial', 12),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        ).pack(side=tk.LEFT, padx=5)
        
        # Checkbox estilizado
        var = tk.BooleanVar()
        check = ttk.Checkbutton(
            frame_dado,
            variable=var,
            style='Custom.TCheckbutton'
        )
        check.pack(side=tk.LEFT, padx=5)
        frame_dado.var = var
        frame_dado.num = num

    def confirmar_selecao():
        global dados, dados_guardados, tentativas
        
        # Coletar dados selecionados
        for widget in frame_dados.winfo_children():
            if hasattr(widget, 'var') and widget.var.get():
                num = widget.num
                if num in dados:
                    dados_guardados[num] = dados.pop(num)

        # Jogar novamente os dados não selecionados
        for num in dados:
            dados[num] = random.randint(1, 6)

        tentativas -= 1
        janela_dados.destroy()
        atualizar_interface()

    # Frame para botões
    frame_botoes = tk.Frame(main_dados_frame, bg=BACKGROUND_COLOR)
    frame_botoes.pack(pady=20)

    # Botões estilizados
    botao_confirmar = tk.Button(
        frame_botoes,
        text="Confirmar Seleção",
        command=confirmar_selecao,
        font=('Arial', 12, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR,
        relief='raised',
        bd=2,
        padx=20,
        pady=10
    )
    botao_confirmar.pack(side=tk.LEFT, padx=10)
    
    botao_cancelar = tk.Button(
        frame_botoes,
        text="Cancelar",
        command=janela_dados.destroy,
        font=('Arial', 12),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR,
        relief='raised',
        bd=2,
        padx=20,
        pady=10
    )
    botao_cancelar.pack(side=tk.LEFT, padx=10)

    # Adicionar efeitos hover aos botões
    for botao in [botao_confirmar, botao_cancelar]:
        botao.bind("<Enter>", on_enter)
        botao.bind("<Leave>", on_leave)

def ver_dados_guardados():
    if not dados_guardados:
        messagebox.showinfo("Dados Guardados", "Nenhum dado foi guardado nesta rodada.")
        return
    
    # Criar janela para mostrar dados guardados
    janela_dados = tk.Toplevel(root)
    janela_dados.title("Dados Guardados")
    janela_dados.geometry("500x600")
    janela_dados.configure(bg=BACKGROUND_COLOR)
    
    # Título
    tk.Label(
        janela_dados,
        text="Dados Guardados",
        font=('Arial', 16, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=20)
    
    # Frame para os dados
    frame_dados = tk.Frame(janela_dados, bg=BACKGROUND_COLOR)
    frame_dados.pack(pady=20)
    
    # Mostrar cada dado guardado
    for num, valor in dados_guardados.items():
        frame_dado = tk.Frame(frame_dados, bg=BACKGROUND_COLOR)
        frame_dado.pack(pady=10)
        
        # Criar representação visual do dado
        dado_visual = criar_dado(frame_dado, valor)
        dado_visual.pack(side=tk.LEFT, padx=10)
        
        # Label com número do dado
        tk.Label(
            frame_dado,
            text=f'Dado {num}',
            font=('Arial', 12),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        ).pack(side=tk.LEFT, padx=5)

def ver_pontuacao():
    if not pontuacao_total:
        messagebox.showinfo("Pontuação", "Nenhuma pontuação foi registrada até o momento.")
        return
    
    # Criar janela para mostrar pontuação
    janela_pontuacao = tk.Toplevel(root)
    janela_pontuacao.title("Pontuação das Rodadas")
    janela_pontuacao.geometry("400x300")
    janela_pontuacao.configure(bg=BACKGROUND_COLOR)
    
    # Título
    tk.Label(
        janela_pontuacao,
        text="Pontuação das Rodadas",
        font=('Arial', 16, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=20)
    
    # Frame para pontuações
    frame_pontuacao = tk.Frame(janela_pontuacao, bg=BACKGROUND_COLOR)
    frame_pontuacao.pack(pady=20)
    
    # Mostrar pontuação de cada rodada
    for num, pontos in pontuacao_total.items():
        tk.Label(
            frame_pontuacao,
            text=f"Rodada {num}: {pontos} pontos",
            font=('Arial', 12),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=5)

def atualizar_interface():
    # Limpar labels anteriores
    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text").startswith("Rodada:"):
            widget.destroy()
    
    # Atualizar informações na interface com estilo melhorado
    info_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    info_frame.pack(pady=10)
    
    tk.Label(
        info_frame,
        text=f"Rodada: {rodada}",
        font=('Arial', 12, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(side=tk.LEFT, padx=10)
    
    tk.Label(
        info_frame,
        text="|",
        font=('Arial', 12),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(side=tk.LEFT, padx=10)
    
    tk.Label(
        info_frame,
        text=f"Tentativas restantes: {tentativas}",
        font=('Arial', 12, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(side=tk.LEFT, padx=10)

# Configurar estilo para os checkbuttons
style = ttk.Style()
style.configure('Custom.TCheckbutton',
                background=BACKGROUND_COLOR,
                foreground=TEXT_COLOR)

# Frame principal
main_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
main_frame.pack(expand=True, fill='both', pady=20)

# Título do jogo
titulo_jogo = tk.Label(
    main_frame,
    text='Jogo General',
    font=('Arial', 24, 'bold'),
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)
titulo_jogo.pack(pady=(0, 20))

# Frame para os botões
frame_botao = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
frame_botao.pack(pady=20)

# Opções do menu como botões
botoes = [
    ('Jogar Dados', jogar_dados),
    ('Ver Dados Guardados', ver_dados_guardados),
    ('Ver Pontuação das Rodadas', ver_pontuacao),
    ('Sair', root.destroy)
]

for texto, comando in botoes:
    botao = tk.Button(
        frame_botao,
        text=texto,
        command=comando,
        font=('Arial', 14),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR,
        relief='raised',
        bd=2,
        padx=20,
        pady=10
    )
    botao.pack(pady=10)
    
    # Adicionar efeitos hover
    botao.bind("<Enter>", on_enter)
    botao.bind("<Leave>", on_leave)

# Inicializar interface
atualizar_interface()

root.mainloop()