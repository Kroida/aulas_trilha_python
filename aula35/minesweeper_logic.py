import tkinter as tk
import random


class Cell:
    HIDDEN = 'hidden'
    REVEALED = 'revealed'
    FLAGGED = 'flagged'

    def __init__(self):
        self.has_mine = False
        self.adjacent_mines = 0
        self.state = Cell.HIDDEN


class Grid:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]

    def generate_mines(self):
        """Coloca minas aleatoriamente no tabuleiro."""
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            cell = self.board[y][x]  # Lembre-se: y é a linha, x é a coluna
            if not cell.has_mine:
                cell.has_mine = True
                mines_placed += 1

        # Atualizar números ao redor das minas
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x].has_mine:
                    continue
                self.board[y][x].adjacent_mines = self.count_adjacent_mines(x, y)

    def count_adjacent_mines(self, x, y):
        """Conta o número de minas ao redor de uma célula."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Ignorar a célula atual
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx].has_mine:
                    count += 1
        return count


if __name__ == "__main__":
    grid = Grid(9, 9, 10)  # Tabuleiro de 8x8 com 10 minas
    grid.generate_mines()

    # Mostrar o tabuleiro no terminal
    for row in grid.board:
        print(" ".join(
            "M" if cell.has_mine else str(cell.adjacent_mines) for cell in row
        ))

        