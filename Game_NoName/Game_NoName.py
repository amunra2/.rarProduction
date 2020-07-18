from random import randint
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

win = tk.Tk()
#win["bg"] = "orange"
win.title("Game_NoName")
win.geometry("1000x600")

coords = []

def rand_num():
    global coords

    if len(coords) >= 0 and len(coords) < 2:
        num = randint(1, 6)
        coords.append(num)
        res = tk.Label(win, text = f"{num}", font=("Arial Bold", 18))
        res.place(x = 830, y = 150)

        if len(coords) == 2:
            res = tk.Label(win, text = f"{coords[0], coords[1]}", font=("Arial Bold", 18))
            res.place(x = 810, y = 300)
    else:
        showwarning("Stop", "Only 2 numbers")

text = tk.Label(win, text="Random number", font=("Arial Bold", 18))
text.place(x = 750, y = 100)
text = tk.Label(win, text="Your numbers are", font=("Arial Bold", 18))
text.place(x = 750, y = 250)

num_find = tk.Button(win, text = "Number", command = rand_num, font=("Arial Bold", 18), background = "lightblue")
num_find.place(x = 780, y = 400)


game = tk.Canvas(win, width = 700, height = 600, bg = "orange")
game.place(x = 0, y = 0)

test = 700
while test > 0:
    game.create_line(test, 0, test, 600, width = 2, fill = "blue")
    game.create_line(0, test, 700, test, width = 2, fill = "blue")
    test -= 50

test = 50
while test > 0:
    game.create_line(test, 50, test, 100, width = 2, fill = "blue")
    test -= 1

def click_point(event):
    x = int(event.x)
    y = int(event.y)
    R = 3
    x = (x // 50) * 50
    y = (y // 50) * 50
    print(x, y)

    game.create_rectangle(x, y, x + 50, y + 50, width=1.5, fill = 'green')
    game.create_oval(x - R, y - R, x + R, y + R, width=1.5, fill = 'pink')


game.bind('<1>', click_point)
win.mainloop() #12x14