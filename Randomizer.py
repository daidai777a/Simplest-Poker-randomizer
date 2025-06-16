import tkinter as tk
import random

# Predefined neon colors for a vibrant look on a dark background
NEON_COLORS = [
    "#39FF14",  # neon green
    "#FF3131",  # neon red
    "#9D00FF",  # neon purple
    "#00FFFF",  # aqua
    "#FFD300",  # bright yellow
]

def update_label():
    """Update the label with a random number and color."""
    number = random.randint(0, 100)
    color = random.choice(NEON_COLORS)
    label.config(text=number, fg=color)
    window.after(5000, update_label)

window = tk.Tk()
window.geometry("300x150")
window.title("Poker Randomizer")
window.configure(bg="black")

label = tk.Label(
    window,
    text="",
    font=("Helvetica", 40, "bold"),
    bg="black",
)
label.pack(expand=True)

update_label()

window.mainloop()
