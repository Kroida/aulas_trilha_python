import tkinter as tk
import random

# Classe para representar cada célula do jogo
class Cell:
    def __init__(self):
        self.has_mine = False
        self.adjacent_mines = 0
        self.state = 'hidden'  # 'hidden', 'revealed', 'marked'

# Classe para representar o tabuleiro do jogo
class Grid:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[Cell() for _ in range(self.height)] for _ in range(self.width)]
        self.generate_mines()
        self.calculate_adjacencies()

    def generate_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if not self.board[x][y].has_mine:
                self.board[x][y].has_mine = True
                mines_placed += 1

    def calculate_adjacencies(self):
        for x in range(self.width):
            for y in range(self.height):
                if not self.board[x][y].has_mine:
                    self.board[x][y].adjacent_mines = self.count_adjacent_mines(x, y)

    def count_adjacent_mines(self, x, y):
        adjacent_mines = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.board[nx][ny].has_mine:
                        adjacent_mines += 1
        return adjacent_mines

    def reveal_cell(self, x, y):
        cell = self.board[x][y]
        if cell.state == 'revealed' or cell.state == 'marked':
            return
        if cell.has_mine:
            self.game_over()
        cell.state = 'revealed'
        if cell.adjacent_mines == 0:
            self.reveal_adjacent_cells(x, y)
    
    def reveal_adjacent_cells(self, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    self.reveal_cell(nx, ny)

    def mark_cell(self, x, y):
        cell = self.board[x][y]
        if cell.state == 'revealed':
            return
        cell.state = 'marked' if cell.state == 'hidden' else 'hidden'

    def game_over(self):
        print("Game Over! Você clicou em uma mina.")
        exit()  # Finaliza o jogo

# Função para criar a interface gráfica do Minesweeper
def minesweeper_interface():
    root = tk.Tk()
    root.title('Minesweeper - L')
    root.configure(bg='#f7f7f7')
    
    # Definindo o tamanho da janela
    largura = 450
    altura = 450

    # Obtendo o tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calculando a posição x e y para centralizar
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 3

    # Definindo a geometria da janela centralizada
    root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
    
    # Criando o grid lógico do jogo
    grid = Grid(9, 9, 10)  # 9x9 com 10 minas
    
    # Função para manipular o clique nos botões
    def on_button_click(x, y):
        grid.reveal_cell(x, y)
        update_buttons()

    def update_buttons():
        # Atualiza os botões na interface gráfica conforme o estado do jogo
        for i in range(9):
            for j in range(9):
                cell = grid.board[i][j]
                button = buttons[i][j]
                if cell.state == 'revealed':
                    if cell.has_mine:
                        button.config(text='M', bg='black', fg='white')
                    else:
                        button.config(text=str(cell.adjacent_mines), bg='lightgrey', fg='black')
                elif cell.state == 'marked':
                    button.config(text='F', bg='yellow', fg='black')
                else:
                    button.config(text=f'Row {i}, Col {j}', bg='gray', fg='white')

    # Criação do grid de 9x9 de botões
    buttons = [[None for _ in range(9)] for _ in range(9)]  # Matriz para armazenar os botões
    for i in range(9):
        for j in range(9):
            button = tk.Button(root, text=f'Row {i}, Col {j}', font=('Arial', 10), bg='gray', fg='white', width=4, height=2,
                               command=lambda i=i, j=j: on_button_click(i, j))  # Passando i, j para a função de clique
            button.grid(row=i, column=j, padx=0, pady=0)
            buttons[i][j] = button  # Armazena o botão na matriz para atualizá-lo depois

    # Ajuste das colunas e linhas para que ocupem o espaço sem margens
    for i in range(9):
        root.grid_columnconfigure(i, weight=1, minsize=50)
        root.grid_rowconfigure(i, weight=1, minsize=50)

    return root

# Iniciar o jogo
if __name__ == '__main__':
    janela = minesweeper_interface()
    janela.mainloop()