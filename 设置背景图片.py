import tkinter as tk
from PIL import Image, ImageTk


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


root = tk.Tk()
im = get_image("1.jpg", 800, 600)
canvas_root = tk.Canvas(root, width=800, height=600)
canvas_root.create_image(400, 300, image=im)
canvas_root.pack()

tk.mainloop()
