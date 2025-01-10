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
    # height is row -, width is column |
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]
        self.first_click = True


    def generate_mines(self, first_x, first_y):
        """Places mines randomly on the board, avoiding the first clicked cell and its neighbors."""
        # List of safe cells around first click
        safe_cells = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = first_x + dx, first_y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    safe_cells.append((nx, ny))

        # Lists all possible positions except safe cells
        all_positions = [(x, y) for x in range(self.width) for y in range(self.height) 
                        if (x, y) not in safe_cells]
        
        # Choose random positions for mines
        mine_positions = random.sample(all_positions, min(self.num_mines, len(all_positions)))
        
        for x, y in mine_positions:
            self.board[y][x].has_mine = True

        # Update numbers around mines
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x].has_mine:
                    continue
                self.board[y][x].adjacent_mines = self.count_adjacent_mines(x, y)


    def count_adjacent_mines(self, x, y):
        """Counts the number of mines around a cell."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Ignore current cell
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx].has_mine:
                    count += 1
        return count


    def reveal_cell(self, row, col):
        """
        Reveals the cell contents and triggers recursion to free areas.
        """
        cell = self.board[row][col]
        if cell.state != "hidden":
            return

        cell.state = "revealed"

        if cell.has_mine:
            return "game_over"

        if cell.adjacent_mines == 0:
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1)
            ]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.height and 0 <= nc < self.width:
                    self.reveal_cell(nr, nc)
        return "continue"


    def check_victory(self):
        """
        Checks if all safe cells have been revealed.
        """
        for row in self.board:
            for cell in row:
                if not cell.has_mine and cell.state != "revealed":
                    return False
        return True


    def mark_cell(self, row, col):
        """
        Marks or unmarks a cell as suspected of containing a mine.
        """
        cell = self.board[row][col]
        if cell.state == "hidden":
            cell.state = "flagged"
        elif cell.state == "flagged":
            cell.state = "hidden"


def interface():
    root = tk.Tk()
    root.title('Minesweeper - Luís Gustavo')
    root.iconbitmap('senac.ico')
    root.configure(bg='#101010')
    
    # Setting the window size
    largura = 500
    altura = 670

    # Getting the screen size
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calculating x and y position to center
    pos_x = (largura_tela - largura) // 2
    pos_y = (altura_tela - altura) // 3

    # Defining centered window geometry
    root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
    
    # Main frame with padding
    main_frame = tk.Frame(root, bg='#101010', padx=25, pady=25)
    main_frame.pack(expand=True, fill='both')
    
    # Frame for game information (timer and mine counter)
    info_frame = tk.Frame(main_frame, bg='#101010')
    info_frame.pack(fill='x', pady=(0, 20))
    
    # Style for information labels
    info_style = {
        'font': ('Helvetica', 24, 'bold'),
        'bg': '#101010',
        'fg': '#f70813',
        'padx': 15,
        'pady': 10
    }
    
    # Frame for the mine counter (left)
    mines_frame = tk.Frame(info_frame, bg='#151515', relief='ridge', bd=2)
    mines_frame.pack(side='left')
    mines_count = tk.Label(mines_frame, text="💣 10", **info_style)
    mines_count.pack()
    
    # Frame for timer (right)
    timer_frame = tk.Frame(info_frame, bg='#151515', relief='ridge', bd=2)
    timer_frame.pack(side='right')
    timer_label = tk.Label(timer_frame, text="⏱️ 000", **info_style)
    timer_label.pack()
    
    # Variables for control
    time_count = 0
    remaining_mines = 10
    game_active = True
    
    
    def update_timer():
        nonlocal time_count
        if game_active:
            time_count += 1
            timer_label.config(text=f"⏱️ {time_count:03d}")
            root.after(1000, update_timer)
    
    # Game frame with border
    game_container = tk.Frame(main_frame, bg='#151515', relief='ridge', bd=2)
    game_container.pack(padx=10, pady=10)
    
    game_frame = tk.Frame(game_container, bg='#151515', padx=10, pady=10)
    game_frame.pack()
    
    # Status label with improved style
    status_frame = tk.Frame(main_frame, bg='#151515', relief='ridge', bd=2)
    status_frame.pack(fill='x', pady=20)
    status_label = tk.Label(status_frame, text="Game in Progress", bg='#151515', fg='#f70813', 
                           font=('Helvetica', 16, 'bold'), pady=10)
    status_label.pack()
    
    # Create game grid
    grid = Grid(9, 9, 10)  # 9x9 board with 10 mines
    buttons = []
    
    # Default style for buttons
    button_style = {
        'width': 3,
        'height': 1,
        'font': ('Helvetica', 12, 'bold'),
        'bg': '#202020',
        'fg': '#f70813',
        'relief': 'raised',
        'bd': 2
    }
    
    
    def on_left_click(x, y):
        nonlocal game_active
        cell = grid.board[y][x]
        button = buttons[y][x]
        
        if cell.state == Cell.FLAGGED:
            return
        
        # If it is the first click, generate mines and start timer
        if grid.first_click:
            grid.generate_mines(x, y)
            grid.first_click = False
            update_timer()
            
        if cell.has_mine:
            button.configure(text="💣", bg='#f70813', fg='black')
            status_label.configure(text="Game Over! 💥")
            game_active = False
            reveal_all()
        else:
            reveal_cell(x, y)
            if grid.check_victory():
                status_label.configure(text="You Won! 🎉")
                game_active = False
                reveal_all()


    def on_right_click(event, x, y):
        nonlocal remaining_mines
        cell = grid.board[y][x]
        button = buttons[y][x]
        
        if cell.state == Cell.REVEALED or not game_active:
            return
            
        if cell.state == Cell.HIDDEN:
            cell.state = Cell.FLAGGED
            button.configure(text="🚩", fg='#f70813')
            remaining_mines -= 1
        else:
            cell.state = Cell.HIDDEN
            button.configure(text="", **button_style)
            remaining_mines += 1
            
        mines_count.config(text=f"💣 {remaining_mines:02d}")


    def reveal_cell(x, y, depth=0):
        cell = grid.board[y][x]
        if cell.state != Cell.HIDDEN or depth > 3:  # Limits the depth of recursion
            return

        button = buttons[y][x]
        cell.state = Cell.REVEALED

        if cell.adjacent_mines == 0:
            button.configure(text="", relief='sunken', bg='#303030')
            # Reveal neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < grid.width and 0 <= new_y < grid.height:
                        reveal_cell(new_x, new_y, depth + 1)
        else:
            colors = ['#4287f5', '#42f54b', '#f70813', '#9942f5', '#f542f2', '#42f5f5', '#f5d442', '#f58742']
            button.configure(text=str(cell.adjacent_mines),
                           relief='sunken',
                           bg='#303030',
                           fg=colors[cell.adjacent_mines - 1])


    def reveal_all():
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.board[y][x]
                button = buttons[y][x]

                if cell.has_mine:
                    button.configure(text="💣", bg='#f70813', fg='black')
                elif cell.adjacent_mines > 0:
                    colors = ['#4287f5', '#42f54b', '#f70813', '#9942f5', '#f542f2', '#42f5f5', '#f5d442', '#f58742']
                    button.configure(text=str(cell.adjacent_mines),
                                   relief='sunken',
                                   bg='#303030',
                                   fg=colors[cell.adjacent_mines - 1])
                else:
                    button.configure(text="",
                                   relief='sunken',
                                   bg='#303030')

    # Create grid buttons
    for y in range(grid.height):
        row = []
        for x in range(grid.width):
            button = tk.Button(game_frame, **button_style)
            button.grid(row=y, column=x, padx=1, pady=1)
            button.configure(command=lambda x=x, y=y: on_left_click(x, y))
            button.bind('<Button-3>', lambda event, x=x, y=y: on_right_click(event, x, y))
            row.append(button)
        buttons.append(row)

    # Frame for new game button
    control_frame = tk.Frame(main_frame, bg='#151515', relief='ridge', bd=2)
    control_frame.pack(fill='x', pady=(0, 10))
    
    
    # New game button with improved style
    def new_game():
        root.destroy()
        new_window = interface()
        new_window.mainloop()
        
    new_game_button = tk.Button(control_frame,
                               text="New Game",
                               font=('Helvetica', 14, 'bold'),
                               bg='#202020',
                               fg='#f70813',
                               relief='raised',
                               bd=3,
                               padx=20,
                               pady=5,
                               command=new_game)
    new_game_button.pack(pady=10)

    return root


if __name__ == "__main__":
    window = interface()
    window.mainloop()