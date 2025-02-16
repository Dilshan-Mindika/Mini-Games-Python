import tkinter as tk
from tkinter import messagebox
import random

class MazeGame:
    def __init__(self, root, grid_size=10):
        self.root = root
        self.grid_size = grid_size
        self.cell_size = 50
        self.maze = []
        self.start = (0, 0)
        self.end = (self.grid_size - 1, self.grid_size - 1)
        self.player_position = self.start
        self.moves = 0

        self.create_maze()

        self.create_widgets()

    def create_widgets(self):
        """Create the UI elements for the game."""
        self.title_label = tk.Label(self.root, text="Maze Game", font=("Roboto", 30, "bold"), fg="white", bg="#2d2d2d")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(self.root, text="Moves: 0", font=("Roboto", 18), fg="white", bg="#2d2d2d")
        self.score_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.cell_size, height=self.grid_size * self.cell_size, bg="#1e1e1e")
        self.canvas.grid(row=2, column=0, columnspan=2, pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Roboto", 16), command=self.quit_game, fg="white", bg="#e74c3c", relief="flat", bd=2)
        self.quit_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

        self.draw_maze()

    def create_maze(self):
        """Generate a random solvable maze."""
        self.maze = [[1] * self.grid_size for _ in range(self.grid_size)]
        self.maze[self.start[0]][self.start[1]] = 0
        self.maze[self.end[0]][self.end[1]] = 0

        # Simple backtracking maze generation
        self._generate_maze(self.start[0], self.start[1])

    def _generate_maze(self, x, y):
        """Recursive backtracking maze generation algorithm."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size and self.maze[nx][ny] == 1:
                self.maze[nx][ny] = 0
                self.maze[x + dx][y + dy] = 0
                self._generate_maze(nx, ny)

    def draw_maze(self):
        """Draw the maze on the canvas."""
        self.canvas.delete("all")

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

        start_x = self.start[1] * self.cell_size
        start_y = self.start[0] * self.cell_size
        self.canvas.create_rectangle(start_x, start_y, start_x + self.cell_size, start_y + self.cell_size, fill="green")

        end_x = self.end[1] * self.cell_size
        end_y = self.end[0] * self.cell_size
        self.canvas.create_rectangle(end_x, end_y, end_x + self.cell_size, end_y + self.cell_size, fill="red")

        player_x = self.player_position[1] * self.cell_size
        player_y = self.player_position[0] * self.cell_size
        self.canvas.create_rectangle(player_x, player_y, player_x + self.cell_size, player_y + self.cell_size, fill="blue")

    def move_left(self, event):
        x, y = self.player_position
        if y > 0 and self.maze[x][y - 1] == 0:
            self.player_position = (x, y - 1)
            self.moves += 1
            self.check_win()
            self.update_score()
            self.draw_maze()

    def move_right(self, event):
        x, y = self.player_position
        if y < self.grid_size - 1 and self.maze[x][y + 1] == 0:
            self.player_position = (x, y + 1)
            self.moves += 1
            self.check_win()
            self.update_score()
            self.draw_maze()

    def move_up(self, event):
        x, y = self.player_position
        if x > 0 and self.maze[x - 1][y] == 0:
            self.player_position = (x - 1, y)
            self.moves += 1
            self.check_win()
            self.update_score()
            self.draw_maze()

    def move_down(self, event):
        x, y = self.player_position
        if x < self.grid_size - 1 and self.maze[x + 1][y] == 0:
            self.player_position = (x + 1, y)
            self.moves += 1
            self.check_win()
            self.update_score()
            self.draw_maze()

    def check_win(self):
        if self.player_position == self.end:
            messagebox.showinfo("You Win!", f"Congratulations! You won in {self.moves} moves!")
            self.reset_game()

    def update_score(self):
        self.score_label.config(text=f"Moves: {self.moves}")

    def reset_game(self):
        self.player_position = self.start
        self.moves = 0
        self.create_maze()
        self.draw_maze()

    def quit_game(self):
        self.root.quit()

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Game")
        self.root.config(bg="#2d2d2d")

        self.create_main_menu()

    def create_main_menu(self):
        """ Create the main menu to choose the level of the game. """
        self.title_label = tk.Label(self.root, text="Maze Game", font=("Roboto", 30, "bold"), fg="white", bg="#2d2d2d")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.easy_button = tk.Button(self.root, text="Easy", font=("Roboto", 16), command=lambda: self.start_game(5), fg="white", bg="#4cd964", relief="flat", bd=2)
        self.easy_button.grid(row=1, column=0, padx=10, pady=10)

        self.medium_button = tk.Button(self.root, text="Medium", font=("Roboto", 16), command=lambda: self.start_game(10), fg="white", bg="#f39c12", relief="flat", bd=2)
        self.medium_button.grid(row=1, column=1, padx=10, pady=10)

        self.hard_button = tk.Button(self.root, text="Hard", font=("Roboto", 16), command=lambda: self.start_game(15), fg="white", bg="#e74c3c", relief="flat", bd=2)
        self.hard_button.grid(row=2, column=0, columnspan=2, pady=20)

    def start_game(self, grid_size):
        """ Start the game with the selected grid size. """
        self.root.destroy()
        game_window = tk.Tk()
        game = MazeGame(game_window, grid_size)
        game_window.mainloop()

# Main function to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
