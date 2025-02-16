import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, grid_size=3):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.config(bg="#2d2d2d")

        # Set the initial game state
        self.grid_size = grid_size
        self.board = [""] * (grid_size * grid_size)
        self.current_player = "X"
        self.game_over = False

        # Create the grid for Tic-Tac-Toe
        self.buttons = []
        for i in range(grid_size * grid_size):
            button = tk.Button(root, text="", width=10, height=3, font=("Roboto", 20), command=lambda i=i: self.on_click(i),
                               relief="flat", bd=2, fg="white", bg="#333333", activebackground="#555555")
            button.grid(row=i // grid_size, column=i % grid_size, padx=5, pady=5)
            self.buttons.append(button)

        # Create the score label
        self.score_label = tk.Label(root, text=f"Player {self.current_player}'s Turn", font=("Roboto", 18, "bold"), fg="white", bg="#2d2d2d")
        self.score_label.grid(row=grid_size, column=0, columnspan=grid_size, pady=20)

        # Restart Button (visible after the game ends)
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
        self.restart_button.grid(row=grid_size + 1, column=0, columnspan=grid_size, pady=10)
        self.restart_button.grid_forget()  # Initially hide the restart button

    def on_click(self, index):
        """ Handle button click events. """
        if self.game_over or self.board[index] != "":
            return
        
        # Set the button text to the current player
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        # Check for a winner or a draw
        if self.check_winner():
            self.display_winner(self.current_player)
        elif "" not in self.board:
            self.display_winner("Draw")
        else:
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"
            self.score_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        """ Check if the current player has won. """
        winning_combinations = []
        # Rows
        for i in range(self.grid_size):
            winning_combinations.append([i * self.grid_size + j for j in range(self.grid_size)])
        # Columns
        for i in range(self.grid_size):
            winning_combinations.append([i + self.grid_size * j for j in range(self.grid_size)])
        # Diagonals
        winning_combinations.append([i * (self.grid_size + 1) for i in range(self.grid_size)])
        winning_combinations.append([i * (self.grid_size - 1) for i in range(1, self.grid_size + 1)])

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "":
                return True
        return False

    def display_winner(self, winner):
        """ Display the winner message and set game over. """
        self.game_over = True
        if winner == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.score_label.config(text=f"Player {winner} wins!" if winner != "Draw" else "It's a Draw!")
        self.restart_button.grid()  # Show restart button after game ends

    def restart_game(self):
        """ Restart the game by resetting the board. """
        self.board = [""] * (self.grid_size * self.grid_size)
        self.current_player = "X"
        self.game_over = False
        self.score_label.config(text=f"Player {self.current_player}'s Turn")

        for button in self.buttons:
            button.config(text="", bg="#333333")

        self.restart_button.grid_forget()  # Hide restart button until game ends


class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe - Menu")
        self.root.config(bg="#2d2d2d")

        # Title label
        self.title_label = tk.Label(root, text="Tic-Tac-Toe", font=("Roboto", 30, "bold"), fg="white", bg="#2d2d2d")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=50)

        # Start Button
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
        self.start_button.grid(row=1, column=0, columnspan=3, pady=10)

        # Settings Button
        self.settings_button = tk.Button(root, text="Settings", command=self.settings, font=("Roboto", 16), fg="white", bg="#007aff", relief="flat", bd=2)
        self.settings_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Roboto", 16), fg="white", bg="#ff3b30", relief="flat", bd=2)
        self.exit_button.grid(row=3, column=0, columnspan=3, pady=10)

    def start_game(self):
        """ Start the game with default 3x3 grid. """
        self.root.quit()  # Close menu
        game_window = tk.Tk()
        TicTacToe(game_window, grid_size=3)  # Start with 3x3 grid
        game_window.mainloop()

    def settings(self):
        """ Open settings to customize grid size. """
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.config(bg="#2d2d2d")

        # Grid size buttons
        for size in [3, 4, 5]:
            button = tk.Button(settings_window, text=f"{size}x{size}", command=lambda size=size: self.start_game_with_size(size),
                               font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
            button.grid(row=size - 2, column=0, pady=10)

    def start_game_with_size(self, grid_size):
        """ Start game with selected grid size. """
        self.root.quit()  # Close settings window
        game_window = tk.Tk()
        TicTacToe(game_window, grid_size=grid_size)
        game_window.mainloop()


# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
