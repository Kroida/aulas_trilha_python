import random
import tkinter as tk
from tkinter import messagebox, ttk

# Definindo variáveis
dados = {str(i): random.randint(1, 6) for i in range(1, 6)}
dados_guardados = {}
pontuacao_total = {}
tentativas = 3
rodada = 1
main_frame = None  # Inicializando main_frame como global

# Definindo cores
BACKGROUND_COLOR = '#1E1E2E'  # Cor de fundo mais escura e moderna
TEXT_COLOR = '#50FA7B'  # Verde mais suave
BUTTON_BG = '#2D2D3F'  # Cor base para botões
BUTTON_HOVER_COLOR = '#3D3D4F'  # Cor quando passa o mouse
BUTTON_ACTIVE_COLOR = '#4D4D5F'  # Cor quando clica
ACCENT_COLOR = '#BD93F9'  # Cor de destaque roxa

# Instanciando janela
root = tk.Tk()
root.title('Jogo General')

# Definindo o tamanho da janela
largura = 800
altura = 800

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

# Criando um estilo personalizado para os botões
class ModernButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            relief='flat',
            borderwidth=0,
            padx=20,
            pady=10,
            font=('Arial', 12, 'bold'),
            activebackground=BUTTON_ACTIVE_COLOR,
            activeforeground=TEXT_COLOR,
            cursor='hand2'
        )
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, e):
        self['background'] = BUTTON_HOVER_COLOR

    def on_leave(self, e):
        self['background'] = BUTTON_BG

# Configurar estilo para os checkbuttons
style = ttk.Style()
style.configure('Custom.TCheckbutton',
                background=BACKGROUND_COLOR,
                foreground=TEXT_COLOR)

# Função para criar frame com borda arredondada
def create_rounded_frame(parent, **kwargs):
    frame = tk.Frame(parent, bg=BACKGROUND_COLOR, **kwargs)
    canvas = tk.Canvas(frame, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    return frame

# Função para criar título estilizado
def create_title(parent, text):
    title_frame = tk.Frame(parent, bg=BACKGROUND_COLOR)
    title = tk.Label(
        title_frame,
        text=text,
        font=('Arial', 24, 'bold'),
        fg=ACCENT_COLOR,
        bg=BACKGROUND_COLOR
    )
    title.pack(pady=20)
    return title_frame

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
        messagebox.showinfo("Pontuação", "Nenhuma combinação especial encontrada.")
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
    else:
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
    global main_frame, tentativas
    if tentativas <= 0:
        messagebox.showwarning("Aviso", "Você não tem mais tentativas!")
        return

    if main_frame:
        main_frame.destroy()

    main_frame = create_rounded_frame(root)
    main_frame.pack(expand=True, fill='both', padx=40, pady=20)

    # Título
    title_frame = create_title(main_frame, 'Jogar Dados')
    title_frame.pack(fill='x')

    # Frame para os dados
    dice_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    dice_frame.pack(pady=20)

    # Variáveis para checkboxes
    check_vars = {}

    # Mostrar os dados disponíveis
    for num, valor in dados.items():
        dice_container = tk.Frame(dice_frame, bg=BACKGROUND_COLOR)
        dice_container.pack(pady=10)
        
        # Criar representação visual do dado
        dado_visual = criar_dado(dice_container, valor)
        dado_visual.pack(side=tk.LEFT, padx=10)
        
        # Label com número do dado
        tk.Label(
            dice_container,
            text=f'Dado {num}',
            font=('Arial', 12),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        ).pack(side=tk.LEFT, padx=5)
        
        # Checkbox para seleção
        var = tk.BooleanVar()
        check_vars[num] = var
        check = ttk.Checkbutton(
            dice_container,
            variable=var,
            style='Custom.TCheckbutton'
        )
        check.pack(side=tk.LEFT, padx=5)

    # Frame para botões de ação
    button_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    button_frame.pack(pady=20, fill='x')

    def confirmar_selecao():
        global dados, dados_guardados, tentativas
        
        # Coletar dados selecionados
        for num, var in check_vars.items():
            if var.get() and num in dados:
                dados_guardados[num] = dados.pop(num)

        # Se não houver mais dados disponíveis, finalizar a rodada
        if not dados:
            organizar_dados()
            show_main_menu()
            return

        # Jogar novamente os dados não selecionados
        for num in dados:
            dados[num] = random.randint(1, 6)

        tentativas -= 1
        
        if tentativas <= 0:
            # Calcular pontuação e iniciar nova rodada
            organizar_dados()
        
        show_main_menu()  # Redirecionar para o menu principal

    # Botões de ação no centro
    buttons_container = tk.Frame(button_frame, bg=BACKGROUND_COLOR)
    buttons_container.pack(expand=True)

    confirmar_button = ModernButton(
        buttons_container,
        text="Confirmar Seleção",
        command=confirmar_selecao
    )
    confirmar_button.pack(side=tk.LEFT, padx=10)

    # Informações do jogo
    info_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    info_frame.pack(pady=20)

    rodada_label = tk.Label(
        info_frame,
        text=f'Rodada: {rodada}',
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    )
    rodada_label.pack(side='left', padx=20)

    tentativas_label = tk.Label(
        info_frame,
        text=f'Tentativas restantes: {tentativas}',
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    )
    tentativas_label.pack(side='left', padx=20)

def ver_dados_guardados():
    if not dados_guardados:
        messagebox.showinfo("Dados Guardados", "Nenhum dado foi guardado nesta rodada.")
        return
    
    # Criar janela para mostrar dados guardados
    janela_dados = tk.Toplevel(root)
    janela_dados.title("Dados Guardados")
    center_window(janela_dados, 500, 600)
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
    center_window(janela_pontuacao, 400, 400)
    janela_pontuacao.configure(bg=BACKGROUND_COLOR)
    
    # Título
    tk.Label(
        janela_pontuacao,
        text="Pontuação das Rodadas",
        font=('Arial', 16, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=20)
    
    # Frame para mostrar as pontuações
    frame_pontuacao = tk.Frame(janela_pontuacao, bg=BACKGROUND_COLOR)
    frame_pontuacao.pack(pady=20)
    
    # Mostrar pontuação de cada rodada
    total_pontos = 0
    for rodada_num, pontos in pontuacao_total.items():
        total_pontos += pontos
        tk.Label(
            frame_pontuacao,
            text=f'Rodada {rodada_num}: {pontos} pontos',
            font=('Arial', 12),
            bg=BACKGROUND_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=5)
    
    # Mostrar pontuação total
    tk.Label(
        janela_pontuacao,
        text=f'\nPontuação Total: {total_pontos} pontos',
        font=('Arial', 14, 'bold'),
        bg=BACKGROUND_COLOR,
        fg=ACCENT_COLOR
    ).pack(pady=20)

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
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    ).pack(side='left', padx=20)
    
    tk.Label(
        info_frame,
        text="|",
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    ).pack(side='left', padx=20)
    
    tk.Label(
        info_frame,
        text=f"Tentativas restantes: {tentativas}",
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    ).pack(side='left', padx=20)

def show_main_menu():
    global main_frame
    if main_frame:
        main_frame.destroy()

    main_frame = create_rounded_frame(root)
    main_frame.pack(expand=True, fill='both', padx=40, pady=20)

    # Título
    title_frame = create_title(main_frame, 'Jogo General')
    title_frame.pack(fill='x')

    # Botões principais
    buttons_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    buttons_frame.pack(pady=20)

    jogar_button = ModernButton(buttons_frame, text='Jogar Dados', command=jogar_dados)
    jogar_button.pack(pady=10)

    ver_dados_button = ModernButton(buttons_frame, text='Ver Dados Guardados', command=ver_dados_guardados)
    ver_dados_button.pack(pady=10)

    ver_pontuacao_button = ModernButton(buttons_frame, text='Ver Pontuação das Rodadas', command=ver_pontuacao)
    ver_pontuacao_button.pack(pady=10)

    sair_button = ModernButton(buttons_frame, text='Sair', command=root.quit)
    sair_button.pack(pady=10)

    # Informações do jogo
    info_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    info_frame.pack(pady=20)

    rodada_label = tk.Label(
        info_frame,
        text=f'Rodada: {rodada}',
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    )
    rodada_label.pack(side='left', padx=20)

    tentativas_label = tk.Label(
        info_frame,
        text=f'Tentativas restantes: {tentativas}',
        font=('Arial', 12),
        fg=TEXT_COLOR,
        bg=BACKGROUND_COLOR
    )
    tentativas_label.pack(side='left', padx=20)

def center_window(window, width, height):
    # Obtendo o tamanho da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculando a posição x e y para centralizar
    pos_x = (screen_width - width) // 2
    pos_y = (screen_height - height) // 2

    # Definindo a geometria da janela centralizada
    window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')

# Inicializar interface
show_main_menu()

root.mainloop()