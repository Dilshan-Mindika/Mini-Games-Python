import tkinter as tk
import random
import threading
import time

class SnakeGame:
    def __init__(self, root, difficulty="Medium"):
        self.root = root
        self.difficulty = difficulty
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake body
        self.direction = 'Right'
        self.food = None
        self.score = 0
        self.game_over = False
        self.paused = False
        self.speed = self.set_speed()  # Set initial speed based on difficulty

        # Set window title and background color
        self.root.title("Snake Game")
        self.root.config(bg="#2d2d2d")

        # Setup Canvas for Snake and Food
        self.canvas = tk.Canvas(root, width=500, height=500, bg="#1e1e1e", bd=0, highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)

        # Create score label with modern font
        self.score_label = tk.Label(root, text="Score: 0", font=("Roboto", 18, "bold"), fg="white", bg="#2d2d2d")
        self.score_label.pack(pady=10)

        # Pause button with modern design
        self.pause_button = tk.Button(root, text="Pause", command=self.toggle_pause, font=("Roboto", 14), fg="white", bg="#f07b3f", relief="flat", bd=2)
        self.pause_button.pack(pady=10)

        # Start the game by placing the first food
        self.create_food()

        # Keyboard binding for controlling the snake
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)
        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)

        # Run the game loop in a separate thread
        self.game_thread = threading.Thread(target=self.run_game)
        self.game_thread.daemon = True
        self.game_thread.start()

    def set_speed(self):
        """ Set the speed of the snake based on difficulty """
        if self.difficulty == "Easy":
            return 0.15  # Slow speed
        elif self.difficulty == "Medium":
            return 0.1  # Normal speed
        else:  # Hard
            return 0.05  # Fast speed

    def run_game(self):
        """ Main game loop running in a separate thread """
        while not self.game_over:
            if not self.paused:
                self.move_snake()
                self.check_collisions()
                self.update_canvas()
            time.sleep(self.speed)  # Control the speed of the snake

        self.display_game_over()

    def move_snake(self):
        """ Move the snake in the current direction. """
        head_x, head_y = self.snake[0]
        
        if self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10
        elif self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10

        # Add new head and remove tail (simulate movement)
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

        # Check if the snake eats food
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])  # Grow the snake
            self.score += 10  # Increase score
            self.create_food()  # Generate new food
            self.update_score_label()

    def change_direction(self, event):
        """ Change direction based on user input. """
        if event.keysym == "Left" and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == "Right" and self.direction != 'Left':
            self.direction = 'Right'
        elif event.keysym == "Up" and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == "Down" and self.direction != 'Up':
            self.direction = 'Down'

    def create_food(self):
        """ Create a new food at a random position on the canvas. """
        x = random.randint(0, 49) * 10  # Food x-coordinate
        y = random.randint(0, 49) * 10  # Food y-coordinate
        self.food = (x, y)

    def check_collisions(self):
        """ Check if the snake collides with the wall or itself. """
        head_x, head_y = self.snake[0]

        # Collision with walls
        if head_x < 0 or head_x >= 500 or head_y < 0 or head_y >= 500:
            self.game_over = True

        # Collision with itself
        if len(self.snake) > 1 and (head_x, head_y) in self.snake[1:]:
            self.game_over = True

    def update_canvas(self):
        """ Update the canvas by drawing the snake and food. """
        self.canvas.delete("all")  # Clear the canvas

        # Draw the snake
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="#30d158", outline="#1c1c1c")

        # Draw the food
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="#ff3b30", outline="#1c1c1c")

    def update_score_label(self):
        """ Update the score label with the current score. """
        self.score_label.config(text=f"Score: {self.score}")

    def display_game_over(self):
        """ Display game over message when the game ends. """
        self.canvas.create_text(250, 250, text="GAME OVER", fill="white", font=("Roboto", 24, "bold"))
        self.canvas.create_text(250, 280, text=f"Final Score: {self.score}", fill="white", font=("Roboto", 16))

        # Option to restart or quit
        restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
        restart_button.pack(pady=10)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Roboto", 16), fg="white", bg="#ff3b30", relief="flat", bd=2)
        quit_button.pack(pady=10)

    def restart_game(self):
        """ Restart the game. """
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Reset snake body
        self.direction = 'Right'
        self.food = None
        self.score = 0
        self.game_over = False
        self.create_food()
        self.update_score_label()

        # Clear the canvas and start a new game loop
        self.canvas.delete("all")
        self.game_thread = threading.Thread(target=self.run_game)
        self.game_thread.daemon = True
        self.game_thread.start()

    def toggle_pause(self):
        """ Toggle pause and resume the game. """
        if self.paused:
            self.paused = False
            self.pause_button.config(text="Pause")
        else:
            self.paused = True
            self.pause_button.config(text="Resume")

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Menu")

        # Main background color
        self.root.config(bg="#2d2d2d")

        self.title_label = tk.Label(root, text="Snake Game", font=("Roboto", 30, "bold"), fg="white", bg="#2d2d2d")
        self.title_label.pack(pady=50)

        # Start Button
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
        self.start_button.pack(pady=10)

        # High Score Button
        self.high_score_button = tk.Button(root, text="High Score", command=self.show_high_scores, font=("Roboto", 16), fg="white", bg="#007aff", relief="flat", bd=2)
        self.high_score_button.pack(pady=10)

        # Difficulty Button
        self.difficulty_button = tk.Button(root, text="Select Difficulty", command=self.select_difficulty, font=("Roboto", 16), fg="white", bg="#ff3b30", relief="flat", bd=2)
        self.difficulty_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Roboto", 16), fg="white", bg="#ff3b30", relief="flat", bd=2)
        self.exit_button.pack(pady=10)

    def start_game(self):
        """ Start the game with selected difficulty. """
        difficulty = "Medium"  # Default
        game_window = tk.Tk()
        SnakeGame(game_window, difficulty)
        game_window.mainloop()

    def show_high_scores(self):
        """ Show high scores. This is just a placeholder. """
        print("High Scores")

    def select_difficulty(self):
        """ Select the game difficulty. """
        difficulty_window = tk.Toplevel(self.root)
        difficulty_window.title("Select Difficulty")
        difficulty_window.config(bg="#2d2d2d")

        easy_button = tk.Button(difficulty_window, text="Easy", command=lambda: self.start_game_with_difficulty("Easy"), font=("Roboto", 16), fg="white", bg="#4cd964", relief="flat", bd=2)
        easy_button.pack(pady=10)

        medium_button = tk.Button(difficulty_window, text="Medium", command=lambda: self.start_game_with_difficulty("Medium"), font=("Roboto", 16), fg="white", bg="#007aff", relief="flat", bd=2)
        medium_button.pack(pady=10)

        hard_button = tk.Button(difficulty_window, text="Hard", command=lambda: self.start_game_with_difficulty("Hard"), font=("Roboto", 16), fg="white", bg="#ff3b30", relief="flat", bd=2)
        hard_button.pack(pady=10)

    def start_game_with_difficulty(self, difficulty):
        """ Start game with the selected difficulty. """
        self.root.quit()  # Close menu
        game_window = tk.Tk()
        SnakeGame(game_window, difficulty)
        game_window.mainloop()

# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
