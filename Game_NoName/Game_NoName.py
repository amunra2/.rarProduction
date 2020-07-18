from random import randint
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

#from math import abs

win = tk.Tk()
#win["bg"] = "orange"
win.title("Game_NoName vers 0.2")
win.geometry("1000x600")

points = []

def rand_num():
    global points

    if len(points) >= 0 and len(points) < 2:
        num = randint(1, 6)
        points.append(num)
        res = tk.Label(win, text = f"{num}", font=("Arial Bold", 18))
        res.place(x = 830, y = 150)

        if len(points) == 2:
            res = tk.Label(win, text = f"{points[0], points[1]}", font=("Arial Bold", 18))
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


used_fields = []

def intersection_check(rect_coords):
    cur_fields = []
    # x = abs(rect_coords[0][0] - rect_coords[1][0]) // 50
    # y = abs(rect_coords[0][1] - rect_coords[1][1]) // 50
    print(rect_coords[0][0], rect_coords[0][1], rect_coords[1][0], rect_coords[1][1])
    x_max = rect_coords[0][0]
    x_min = rect_coords[1][0]

    if x_min >= x_max:
        temp = x_max
        x_max = x_min
        x_min = temp

    y_max = rect_coords[0][1]
    y_min = rect_coords[1][1]

    if y_min >= y_max:
        temp = y_max
        y_max = y_min
        y_min = temp    
    
    temp = y_min

    print(x_min, x_max, y_min, y_max)
    while x_min < x_max:
        while temp < y_max:
            cur_fields.append([x_min, temp])
            temp += 50
            print(x_min, temp)
        x_min += 50
        temp = y_min

    flag = True

    for i in range(len(used_fields)):
        for j in range(len(cur_fields)):
            if used_fields[i] == cur_fields[j]:
                flag = False

    if flag:
        for j in range(len(cur_fields)):
            used_fields.append(cur_fields[j])
    
    print(used_fields)

    return flag


def find_square(rect_coords):
    a_side = abs(rect_coords[0][0] - rect_coords[1][0]) // 50
    b_side = abs(rect_coords[0][1] - rect_coords[1][1]) // 50

    square = a_side * b_side
    print(square)
    return square


def click_point(event):
    global points

    if len(points) == 2:
        square = points[0] * points[1]

        x = int(event.x)
        y = int(event.y)

        if len(rect_coords) == 0:
            x = (x // 50) * 50
            y = (y // 50) * 50
            rect_coords.append([x, y])
        elif len(rect_coords) == 1:
            x = (x // 50) * 50
            y = (y // 50) * 50

            if x >= rect_coords[0][0] and y >= rect_coords[0][1]:
                x += 50
                y += 50
            elif x > rect_coords[0][0] and y < rect_coords[0][1]:
                x += 50
                rect_coords[0][1] += 50
            elif x < rect_coords[0][0] and y > rect_coords[0][1]:
                rect_coords[0][0] += 50
                y += 50
            else:
                rect_coords[0][0] += 50
                rect_coords[0][1] += 50
            rect_coords.append([x, y])
        print(x, y)

        if len(rect_coords) == 2:
            cur_square = find_square(rect_coords)
            
            if (cur_square == square):
                if intersection_check(rect_coords):
                    game.create_rectangle(rect_coords[0][0], rect_coords[0][1], rect_coords[1][0], rect_coords[1][1], width=1.5, fill = 'green')
                    points.clear()
                    
                else:
                    showwarning("Error", "Intersection of the fields")
            else:
                showwarning("Error", "Unright square")
    
            rect_coords.clear()
    else:
        showinfo("Error", "Not enough points")


    #game.create_oval(x - R, y - R, x + R, y + R, width=1.5, fill = 'pink')

rect_coords = []
game.bind('<1>', click_point)
win.mainloop() #12x14