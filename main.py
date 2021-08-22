import tkinter as tk
from PIL import Image, ImageTk


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


def bt1_click():
    pass


def bt2_click():
    pass


win = tk.Tk()
win.title("通用电流计算器")
win.geometry("700x500")
win.attributes("-toolwindow", 2)
win.resizable(0, 0)
im = get_image("1.png", 700, 500)
canvas_win = tk.Canvas(win, width=700, height=500)
canvas_win.create_image(350, 250, image=im)
canvas_win.pack()

lb_welcome = tk.Label(win, text="欢迎使用通用电流计算器！", bg="black", fg="white", font=('宋体', 30, 'bold'))
lb_welcome.place(x=100, y=30, width=500)

lb_hint = tk.Label(win, text="请选择您要计算的电路拓扑：", bg="black", fg="white", font=('宋体', 15, 'bold'))
lb_hint.place(x=100, y=90)

photo1 = get_image("loop1.png", 210, 150)
lb1 = tk.Label(win, bg="DodgerBlue2", compound='center', image=photo1)
lb1.place(x=80, y=170, width=220, height=160)

photo2 = get_image("loop2.png", 210, 150)
lb1 = tk.Label(win, bg="DodgerBlue2", compound='center', image=photo2)
lb1.place(x=410, y=170, width=220, height=160)

bt01 = get_image("bt1.png", 87, 60)
bt1 = tk.Button(win, image=bt01, command=bt1_click)
bt1.place(x=135, y=380)

bt02 = get_image("bt2.png", 87, 60)
bt2 = tk.Button(win, image=bt02, command=bt2_click)
bt2.place(x=472, y=380)

win.mainloop()
