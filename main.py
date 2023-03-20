import tkinter as tk
import tkinter.messagebox as messagebox
from screen import Screen
from numberMatrix import NumberMatrix
from PIL import ImageTk, Image


class GuessNumberGame:
    def __init__(self):
        self.number_matrix = None
        self.question_label = None
        self.result_label = None
        self.start_button = None

    def start_game(self, n):
        start_button.pack_forget()
        self.number_matrix = NumberMatrix(n)
        self.question_label.config(text="")
        self.result_label.config(text="")

        number = 0
        for i in range(min(self.number_matrix.m, 10)):
            number += self.ask_question(i)

        # Clear the result_label widget before showing the wine image
        for widget in self.result_label.winfo_children():
            widget.destroy()

        # present slavers status
        Screen.show_puzzle_solution(self, number)

        # unhide start button
        start_button.config(text="Play again")
        start_button.pack()

    def ask_question(self, i):
        # Clear the result_label widget before drawing the new labels and images
        for widget in self.result_label.winfo_children():
            widget.destroy()
        NumberMatrix.get_numbers_in_matrix(self.number_matrix, self.result_label, i)

        # Update GUI
        root.update()
        # root.update_idletasks()

        answer = messagebox.askquestion("Question", f"Is your wine bottle in set {i + 1}?", icon="question")
        if answer == "yes":
            return 2 ** i
        else:
            return 0


if __name__ == '__main__':
    game = GuessNumberGame()

    # GUI setup
    root = tk.Tk()
    root.geometry("1050x700")
    root.title("Thousand Wines One Poison Puzzle")

    # Set background image
    background_image = tk.PhotoImage(file="Game_Background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Resize header image
    header_image = Image.open("title.png")
    header_image = header_image.resize((int(header_image.width/3), int(header_image.height/2)))
    header_image = ImageTk.PhotoImage(header_image)

    header_label = tk.Label(root, image=header_image, pady=20, bg="#e0e0e0")
    header_label.pack()

    game.question_label = tk.Label(root, text="Think of a number between 1-1000", font=("Helvetica", 14), pady=20, padx=70, bg="#e0e0e0")
    game.question_label.pack()

    game.result_label = tk.Label(root, text="", font=("Helvetica", 14), pady=20, padx=70, bg="#e0e0e0")
    game.result_label.pack()

    button_frame = tk.Frame(root, bg="#e0e0e0")
    button_frame.pack(pady=20)

    start_button = tk.Button(button_frame, text="Start Game", font=("Helvetica", 14), bg="#e0e0e0",
                             command=lambda: game.start_game(1000))
    start_button.pack(side="left", padx=20)

    exit_button = tk.Button(button_frame, text="Exit", font=("Helvetica", 14), bg="#e0e0e0", command=root.quit)
    exit_button.pack(side="right", padx=20)

    root.mainloop()

