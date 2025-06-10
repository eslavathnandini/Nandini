import tkinter as tk
import random

class WordCrossPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Cross Puzzle")
        self.words = ["PYTHON", "JAVA", "CODE", "ALGORITHM"]
        self.grid_size = 10
        self.grid = []
        self.selected = []
        self.score = 0
        self.create_grid()
        self.setup_ui()

    def create_grid(self):
        # Initialize empty grid
        self.grid = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                      for _ in range(self.grid_size)]
                      for _ in range(self.grid_size)]
        # Place words randomly
        for word in self.words:
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            row = random.randint(0, self.grid_size - len(word))
            col = random.randint(0, self.grid_size - len(word))
            for i, letter in enumerate(word):
                if direction == 'horizontal':
                    self.grid[row][col + i] = letter
                elif direction == 'vertical':
                    self.grid[row + i][col] = letter
                else:  # diagonal
                    self.grid[row + i][col + i] = letter

    def setup_ui(self):
        self.buttons = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                btn = tk.Button(self.root, text=self.grid[i][j], width=3,
                               command=lambda i=i, j=j: self.select_cell(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.grid(row=self.grid_size, columnspan=self.grid_size)

    def select_cell(self, row, col):
        self.selected.append((row, col))
        if len(self.selected) == 1:
            self.buttons[row][col].config(bg='yellow')
        else:
            self.validate_word()

    def validate_word(self):
        # Check if selected letters form a valid word
        word = ''.join([self.grid[r][c] for r, c in self.selected])
        if word in self.words:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            for r, c in self.selected:
                self.buttons[r][c].config(bg='green')
        else:
            for r, c in self.selected:
                self.buttons[r][c].config(bg='red')
        self.selected = []

if __name__ == "__main__":
    root = tk.Tk()
    game = WordCrossPuzzle(root)
    root.mainloop()
