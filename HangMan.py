import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.config(bg="#2d2d2d")

        # Expanded list of words with hints
        self.words_with_hints = [
            {"word": "PYTHON", "hint": "A popular programming language"},
            {"word": "JAVASCRIPT", "hint": "Language of the web"},
            {"word": "COMPUTER", "hint": "An electronic device"},
            {"word": "PROGRAMMING", "hint": "Creating software"},
            {"word": "DEVELOPER", "hint": "A person who writes code"},
            {"word": "DATABASE", "hint": "An organized collection of data"},
            {"word": "ALGORITHM", "hint": "A step-by-step procedure for solving a problem"},
            {"word": "ARTIFICIAL", "hint": "Related to machine intelligence"},
            {"word": "MACHINE", "hint": "A device that performs a task"},
            {"word": "NETWORK", "hint": "A group of interconnected devices"},
            {"word": "SERVER", "hint": "A system that provides services or resources to clients"},
            {"word": "COMPUTATION", "hint": "The process of performing mathematical calculations"},
            {"word": "SOFTWARE", "hint": "Programs or applications used by a computer"},
            {"word": "HARDWARE", "hint": "Physical components of a computer"},
            {"word": "JAVA", "hint": "A popular object-oriented programming language"},
            {"word": "CLOUD", "hint": "Storing and accessing data over the internet"},
            {"word": "BLOCKCHAIN", "hint": "A decentralized and distributed ledger system"},
            {"word": "ENCRYPTION", "hint": "The process of encoding data to prevent unauthorized access"},
            {"word": "API", "hint": "A set of tools for building software applications"},
            {"word": "DEVOPS", "hint": "A set of practices combining software development and IT operations"},
            {"word": "SECURITY", "hint": "The protection of computer systems from unauthorized access"},
            {"word": "BUG", "hint": "An error or flaw in a program or system"},
            {"word": "DEBUG", "hint": "The process of identifying and fixing errors in software"},
            {"word": "HTML", "hint": "The standard language for creating web pages"},
            {"word": "CSS", "hint": "Style sheet language used for describing web page presentation"},
            {"word": "RESPONSIVE", "hint": "Designing websites to adjust to different screen sizes"},
            {"word": "FRONTEND", "hint": "The client-side part of a web application"},
            {"word": "BACKEND", "hint": "The server-side part of a web application"},
            {"word": "REACT", "hint": "A popular JavaScript library for building user interfaces"},
            {"word": "VUE", "hint": "A progressive JavaScript framework for building UIs"},
            {"word": "NODEJS", "hint": "A JavaScript runtime built on Chrome's V8 JavaScript engine"},
            {"word": "MONGODB", "hint": "A NoSQL database for scalable and high-performance data storage"},
            {"word": "GIT", "hint": "A version control system for tracking changes in code"},
            {"word": "GITHUB", "hint": "A web-based platform for version control and collaboration"},
            {"word": "LINUX", "hint": "A popular open-source operating system"},
            {"word": "PYCHARM", "hint": "An integrated development environment for Python programming"},
            {"word": "INTEL", "hint": "A leading semiconductor manufacturer"},
            {"word": "MICROSOFT", "hint": "A multinational technology company, developer of Windows"},
            {"word": "APPLE", "hint": "A multinational technology company known for the iPhone"},
            {"word": "GOOGLE", "hint": "A multinational company specializing in internet-related services"},
            {"word": "AMAZON", "hint": "An online marketplace and cloud computing giant"},
            {"word": "FACEBOOK", "hint": "A social media platform that connects people"},
            {"word": "TWITTER", "hint": "A social media platform for microblogging"},
            {"word": "INSTAGRAM", "hint": "A photo and video sharing social networking service"},
            {"word": "DISCORD", "hint": "A voice, video, and text chat platform for gamers"},
            {"word": "WHATSAPP", "hint": "A messaging app for smartphones"},
            {"word": "SNAPCHAT", "hint": "A multimedia messaging app"},
            {"word": "TIKTOK", "hint": "A short-form video platform"},
            {"word": "LINUX", "hint": "An open-source Unix-like operating system"},
            {"word": "ANDROID", "hint": "An operating system for mobile devices"},
            {"word": "IOS", "hint": "An operating system for Apple's mobile devices"},
            {"word": "WINDOWS", "hint": "An operating system developed by Microsoft"},
            {"word": "GITHUB", "hint": "A platform for version control and collaboration"},
            {"word": "ANDROID", "hint": "An open-source mobile operating system"},
            {"word": "MICROPROCESSOR", "hint": "The central processing unit of a computer"},
            {"word": "FIREWALL", "hint": "A network security system that monitors and controls incoming traffic"},
            {"word": "RAM", "hint": "Random Access Memory, temporary storage used by the computer"},
            {"word": "ROBOTICS", "hint": "The technology dealing with robots"},
            {"word": "AUTOMATION", "hint": "The use of technology to perform tasks without human intervention"},
            {"word": "CIRCUIT", "hint": "A path that electricity flows through in electronics"},
            {"word": "COMPUTER", "hint": "An electronic device for storing and processing data"},
            {"word": "SERVER", "hint": "A computer or program that provides services to other computers"},
            {"word": "SWITCH", "hint": "A device used to connect multiple network devices"},
            {"word": "ROUTER", "hint": "A device that forwards data packets between computer networks"},
            {"word": "VIRUS", "hint": "A malicious software program designed to harm or exploit devices"},
            {"word": "TROJAN", "hint": "A type of malicious software that pretends to be legitimate"},
            {"word": "PHISHING", "hint": "Fraudulent attempts to obtain sensitive information via electronic communication"},
            {"word": "SPYWARE", "hint": "Software designed to gather information without the user's consent"},
            {"word": "ADWARE", "hint": "Software that automatically displays advertisements"},
            {"word": "MALWARE", "hint": "Software specifically designed to disrupt or damage computers or networks"},
            {"word": "CLOUD", "hint": "A network of remote servers used for storing and managing data"},
            {"word": "VPN", "hint": "A secure network connection that allows users to send data over public networks"},
            {"word": "URL", "hint": "Uniform Resource Locator, the address of a webpage"},
            {"word": "HTTPS", "hint": "HyperText Transfer Protocol Secure, used for secure communication over a computer network"},
            {"word": "DATABASE", "hint": "A structured collection of data"},
            {"word": "SQL", "hint": "Structured Query Language, used to manage databases"},
            {"word": "JSON", "hint": "JavaScript Object Notation, a lightweight data-interchange format"},
            {"word": "XML", "hint": "Extensible Markup Language, used to encode documents in a format readable by humans and machines"},
            {"word": "SEO", "hint": "Search Engine Optimization, the process of improving a website's visibility"},
            {"word": "PANDAS", "hint": "A Python library used for data manipulation and analysis"},
            {"word": "MATPLOTLIB", "hint": "A Python library used for creating static, animated, and interactive visualizations"},
            {"word": "NUMPY", "hint": "A Python library for numerical computing"},
            {"word": "SCIENCE", "hint": "Systematic enterprise that builds and organizes knowledge in the form of testable explanations and predictions"},
            {"word": "CHEMISTRY", "hint": "The study of the properties and behavior of matter"}
        ]

        random.shuffle(self.words_with_hints)

        # Game state
        self.score = 0
        self.word_data = None
        self.guessed_letters = set()
        self.attempts_left = 6  # Max attempts
        self.display_word = []
        
        # Create UI elements
        self.create_widgets()
        self.next_word()

    def create_widgets(self):
        """ Create the UI elements for the game. """
        # Title label
        self.title_label = tk.Label(self.root, text="Hangman", font=("Roboto", 30, "bold"), fg="white", bg="#2d2d2d")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Hint label
        self.hint_label = tk.Label(self.root, text="", font=("Roboto", 16), fg="white", bg="#2d2d2d")
        self.hint_label.grid(row=1, column=0, columnspan=2, pady=20)

        # Display the word (initially with underscores)
        self.word_label = tk.Label(self.root, text="", font=("Roboto", 20), fg="white", bg="#2d2d2d")
        self.word_label.grid(row=2, column=0, columnspan=2, pady=20)

        # Input field for the user to guess a letter
        self.guess_entry = tk.Entry(self.root, font=("Roboto", 18), width=5, justify="center", bd=2, relief="flat", fg="black")
        self.guess_entry.grid(row=3, column=0, pady=20)

        # Submit button for the user's guess
        self.guess_button = tk.Button(self.root, text="Guess", font=("Roboto", 16), command=self.process_guess, fg="white", bg="#4cd964", relief="flat", bd=2)
        self.guess_button.grid(row=3, column=1, padx=10)

        # Pass Word button
        self.pass_button = tk.Button(self.root, text="Pass Word", font=("Roboto", 16), command=self.next_word, fg="white", bg="#f0a500", relief="flat", bd=2)
        self.pass_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Label for the attempts remaining
        self.attempts_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", font=("Roboto", 18), fg="white", bg="#2d2d2d")
        self.attempts_label.grid(row=5, column=0, columnspan=2, pady=20)

        # Score label
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Roboto", 18), fg="white", bg="#2d2d2d")
        self.score_label.grid(row=6, column=0, columnspan=2, pady=20)

        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", font=("Roboto", 16), command=self.quit_game, fg="white", bg="#e74c3c", relief="flat", bd=2)
        self.quit_button.grid(row=7, column=0, columnspan=2, pady=20)

    def next_word(self):
        """ Set up the next word to guess. """
        if len(self.words_with_hints) == 0:
            messagebox.showinfo("Game Over", f"Your final score is {self.score}!")
            self.quit_game()
            return
        
        # Pick a random word from the list
        self.word_data = self.words_with_hints.pop()
        self.word_to_guess = self.word_data["word"]
        self.hint_label.config(text=f"Hint: {self.word_data['hint']}")
        
        # Initialize the game state
        self.guessed_letters = set()
        self.attempts_left = 6
        self.display_word = ["_"] * len(self.word_to_guess)
        self.word_label.config(text=" ".join(self.display_word))
        self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")

    def process_guess(self):
        """ Process the user's guess. """
        guess = self.guess_entry.get().upper()

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        # Check if the letter is in the word
        if guess in self.word_to_guess:
            for index, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.display_word[index] = guess
            self.word_label.config(text=" ".join(self.display_word))
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")

        # Check if the game is over
        if self.attempts_left == 0:
            self.end_game("You Lost! The word was: " + self.word_to_guess)
        elif "_" not in self.display_word:
            self.score += len(self.word_to_guess)  # Award points based on word length
            self.score_label.config(text=f"Score: {self.score}")
            self.end_game("You Won!")

        # Clear the input field
        self.guess_entry.delete(0, tk.END)

    def end_game(self, message):
        """ End the game with a message. """
        messagebox.showinfo("Game Over", message)
        self.next_word()  # Go to the next word after a game ends

    def quit_game(self):
        """ Exit the game. """
        self.root.quit()  # Close the window

# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
