import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random

class DiceSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Dice Simulator")

        self.result_label = Label(master, text="", font=("Helvetica", 48))
        self.result_label.pack(pady=20)

        self.roll_button = Button(master, text="Rzuć kostką", command=self.roll_dice)
        self.roll_button.pack()

        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f'dice_images/dice_{i}.png')) for i in range(1, 7)
        ]

        self.image_label = None

    def roll_dice(self):
        result = random.randint(1, 6)
        self.result_label.config(text=str(result))
        self.hide_dice_image()
        self.show_dice_image(result)

    def show_dice_image(self, result):
        image = self.dice_images[result - 1]
        self.image_label = Label(self.master, image=image)
        self.image_label.image = image
        self.image_label.pack()

    def hide_dice_image(self):
        if self.image_label:
            self.image_label.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()