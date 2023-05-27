import tkinter as tk
import random

def update_label():
    number = random.randint(1, 100)
    label.config(text=number)
    window.after(3000, update_label)

window = tk.Tk()
window.geometry("200x100")
window.title("Random Number Generator")

label = tk.Label(window, text="", font=("Arial", 30))  # ここでフォントサイズを30に設定
label.pack(pady=20)

update_label()

window.mainloop()