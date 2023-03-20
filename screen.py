import tkinter as tk
from PIL import ImageTk, Image


class Screen:
    def __init__(self):
        self.number_matrix = None
        self.result_label = None
        self.question_label = None

    def show_matrix_on_screen(self, matrix):
        img = Image.open("wine.png")
        img = img.resize((15, 15))
        photo_img = ImageTk.PhotoImage(img)  # read the image file only once

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    # create Label object with the image
                    image_label = tk.Label(self, image=photo_img, bg="#e0e0e0")
                    image_label.image = photo_img  # keep a reference to the PhotoImage object
                    image_label.grid(row=i, column=j * 2)  # position the Label object

                    # create Label object for the number
                    number_label = tk.Label(self, text=str(matrix[i][j]), font=("Helvetica", 12), bg="#e0e0e0")
                    number_label.grid(row=i, column=j * 2 + 1)  # position the Label object next to the image

    def show_puzzle_solution(self, number):
        # Present puzzle solution
        self.question_label.config(
            text=f"{min(self.number_matrix.m, 10)} questions were asked. Wine bottle n.{number} were poisoned.")

        # Convert number to binary and put it into an array
        binary_array = [int(x) for x in bin(number)[2:].zfill(8)]

        # position the Label object in the center of the screen
        self.result_label.grid_rowconfigure(0, weight=1)  # configure row 0 to expand vertically
        self.result_label.grid_columnconfigure(0, weight=1)  # configure column 0 to expand horizontally

        # Load and resize slave and wine images
        slave_img = Image.open("Slave.png").resize((100, 200))
        poisoned_slave_img = Image.open("Poisoned_Slave.png").resize((100, 200))
        poisoned_wine_img = Image.open("Poison_Wine.png").resize((35, 60))

        # Create labels for each slave and wine image and add them to the result label
        num_slaves_killed = 0
        for i, binary_digit in enumerate(binary_array):
            if binary_digit == 1:
                # Add poison_wine label above poisoned_slave label
                wine_photo_img = ImageTk.PhotoImage(poisoned_wine_img)
                wine_label = tk.Label(self.result_label, image=wine_photo_img, bg="#e0e0e0")
                wine_label.image = wine_photo_img
                wine_label.grid(row=3, column=i, sticky="NSEW")

                img = poisoned_slave_img
                num_slaves_killed += 1
            else:
                img = slave_img

            photo_img = ImageTk.PhotoImage(img)
            label = tk.Label(self.result_label, image=photo_img, bg="#e0e0e0")
            label.image = photo_img
            label.grid(row=4, column=i, sticky="NSEW")  # position in the middle row

            self.result_label.grid_rowconfigure(0, weight=1)  # configure top row to expand vertically
            self.result_label.grid_rowconfigure(2, weight=1)  # configure bottom row to expand vertically
            self.result_label.grid_rowconfigure(3, weight=1)  # configure new row to expand vertically
            self.result_label.grid_columnconfigure(i, weight=1)  # configure column to expand horizontally

        # Add label for number of slaves killed
        if num_slaves_killed == 1:
            temp = str(num_slaves_killed) + " slave was killed"
        else:
            temp = str(num_slaves_killed) + " slaves were killed"
        num_slaves_killed_label = tk.Label(self.result_label, text=temp)
        num_slaves_killed_label.grid(row=5, columnspan=len(binary_array), pady=10)
