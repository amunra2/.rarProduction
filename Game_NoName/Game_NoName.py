from random import randint
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

#from math import abs

win = tk.Tk()
#win["bg"] = "orange"
win.title("Game_NoName vers 0.6.0")
win.geometry("1300x1000")

# Variables (???)
points = []
used_fields = []

red_fields = []
purple_fields = []

second = 0 # For second step
color_flag = True
steps = 50

square_first_player = 0
square_second_player = 0

def rand_num():
    global points

    if len(points) >= 0 and len(points) < 2:
        num = randint(1, 4)
        points.append(num)
        res = tk.Label(win, text = f"{num}", font=("Arial Bold", 18))
        res.place(x = 1130, y = 150)

        if len(points) == 2:
            res = tk.Label(win, text = f"{points[0], points[1]}", font=("Arial Bold", 18))
            res.place(x = 1110, y = 300)
    else:
        showwarning("Stop", "Only 2 numbers")


def skip_turn():
    global points, color_flag, steps, square_first_player, square_second_player
    points.clear()
    
    if color_flag:
        color_flag = False
    else:
        color_flag = True

    if len(used_fields) == 400 or steps == 0:
        winner(square_first_player, square_second_player)
    else:
        steps -= 1
        text = tk.Label(win, text = f"Steps left: {steps}", font=("Arial Bold", 18))
        text.place(x = 1050, y = 700)


def draw_field():

    test = 1000
    while test > 0:
        game.create_line(test, 0, test, 1000, width = 2, fill = "blue")
        game.create_line(0, test, 1000, test, width = 2, fill = "blue")
        test -= 50

    game.create_line(50, 0, 50, 50, width = 5, fill = "red")
    game.create_line(0, 50, 50, 50, width = 5, fill = "red")

    game.create_line(950, 50, 1000, 50, width = 5, fill = "red")
    game.create_line(950, 50, 950, 0, width = 5, fill = "red")

    game.create_line(50, 950, 0, 950, width = 5, fill = "red")
    game.create_line(50, 950, 50, 1000, width = 5, fill = "red")

    game.create_line(950, 950, 1000, 950, width = 5, fill = "red")
    game.create_line(950, 950, 950, 1000, width = 5, fill = "red")


def clear_canvas():
    global second, color_flag, steps
    points.clear()
    used_fields.clear()
    red_fields.clear()
    purple_fields.clear()
    second = 0
    color_flag = True
    steps = 50
    game.delete("all")
    
    draw_field()


text = tk.Label(win, text="Random number", font=("Arial Bold", 18))
text.place(x = 1050, y = 100)
text = tk.Label(win, text="Your numbers are", font=("Arial Bold", 18))
text.place(x = 1050, y = 250)


num_find = tk.Button(win, text = "Number", command = rand_num, font=("Arial Bold", 18), background = "lightblue")
num_find.place(x = 1080, y = 400)

skip = tk.Button(win, text = "Skip turn", command = skip_turn, font=("Arial Bold", 18), background = "lightblue")
skip.place(x = 1080, y = 500)

clear_field = tk.Button(win, text = "Clear", command = clear_canvas, font=("Arial Bold", 18), background = "lightblue")
clear_field.place(x = 1080, y = 900)

game = tk.Canvas(win, width = 1000, height = 1000, bg = "lightgreen")
game.place(x = 0, y = 0)

draw_field() # draw!


def intersection_check(rect_coords):
    global second
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

    check_mis = first_second_step(cur_fields, used_fields)



    for i in range(len(used_fields)):
        for j in range(len(cur_fields)):
            if used_fields[i] == cur_fields[j]:
                check_mis = -3 # ineresection mistake

    if check_mis == 0: # if not intersection and not problems with first 2 steps - add to use fields
        for j in range(len(cur_fields)):
            used_fields.append(cur_fields[j])

            if color_flag:
                red_fields.append(cur_fields[j])
            else:
                purple_fields.append(cur_fields[j])
    
    #print(used_fields)

    return check_mis


def find_square(rect_coords):
    a_side = abs(rect_coords[0][0] - rect_coords[1][0]) // 50
    b_side = abs(rect_coords[0][1] - rect_coords[1][1]) // 50

    square = a_side * b_side
    print(square)
    return square


def click_point(event):
    global points, color_flag, steps, square_first_player, square_second_player

    if color_flag:
        color = 'red'
    else:
        color = 'purple'

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
                check_mis = intersection_check(rect_coords)
                if check_mis == 0:
                    game.create_rectangle(rect_coords[0][0], rect_coords[0][1], rect_coords[1][0], rect_coords[1][1], width=2, fill = color)
                    points.clear()

                    if color_flag: # square check
                        square_first_player += square
                    else:
                        square_second_player += square

                    if len(used_fields) == 400 or steps == 0: # check win
                        winner(square_first_player, square_second_player)
                    else:
                        steps -= 1
                        text = tk.Label(win, text = f"Steps left: {steps}", font=("Arial Bold", 18))
                        text.place(x = 1050, y = 700)

                    if color_flag: # cheange color
                        color_flag = False
                    else:
                        color_flag = True
                elif check_mis == -1:
                    showwarning("Error", "First step only in the corner")
                elif check_mis == -2:
                    showwarning("Error", "Second step only in the opposite corner")                    
                elif check_mis == -3:
                    showwarning("Error", "Intersection of the fields")
                elif check_mis == -4:
                    showwarning("Error", "Fileds must be connected")
            else:
                showwarning("Error", "Unright square")
    
            rect_coords.clear()
    else:
        showinfo("Error", "Not enough points")


    #game.create_oval(x - R, y - R, x + R, y + R, width=1.5, fill = 'pink')


def first_second_step(cur_fields, used_fields): #0 0     950 0      0 950    950 950
    global second, color_flag

    if len(used_fields) != 0 and second == 2:
        if connection_blocks(cur_fields, red_fields, purple_fields, color_flag):
            return -4
        else:
            return 0 # not 1st and not 2nd step
    else:
        left_up = [0, 0]
        right_up = [950, 0]
        left_down = [0, 950]
        right_down = [950, 950]

        if second == 0: # not 2nd step
            print(left_up not in cur_fields)

            if (left_up not in cur_fields) and (right_up not in cur_fields) and (left_down not in cur_fields) and (right_down not in cur_fields):
                print(cur_fields)
                return -1 # unright input of the figure
            else:
                second = 1
                return 0 # ok first step
        else:
            check = 0 # ok 2nd step

            if left_up in used_fields and right_down not in cur_fields:
                check = -2 # unright second step
            elif right_up in used_fields and left_down not in cur_fields:
                check = -2 # unright second step
            elif left_down in used_fields and right_up not in cur_fields:
                check = -2 # unright second step
            elif right_down in used_fields and left_up not in cur_fields:
                check = -2 # unright second step

            if check == 0:
                second = 2 # ok 2nd step
            return check


def connection_blocks(cur_fields, red_fields, purple_fields, color_flag):
    # global 
    connection = True

    print("cur_fields")
    print(cur_fields)

    if color_flag:
        arr = red_fields
        print(red_fields)
    else:
        arr = purple_fields
        print(purple_fields)
        print(arr)

    for i in range(len(cur_fields)):
        for j in range(len(arr)):
            
            x_dif = abs(arr[j][0] - cur_fields[i][0])
            y_dif = abs(arr[j][1] - cur_fields[i][1])

            if ((x_dif == 0) and (y_dif == 50)) or ((y_dif == 0) and (x_dif == 50)):
                print("Yessssssssssssssssssssssssssssssssssssssssssssssssssssssss")
                connection = False
                return connection
                
    return connection


def winner(square_first_player, square_second_player):
    
    if square_first_player > square_second_player:
        text = "First player has won! His square is bigger"
    elif square_first_player < square_second_player:
        text = "Second player has won! His square is bigger"
    else:
        text = "Draw!"

    showinfo("Congrats!", text)
    clear_canvas()


rect_coords = []
game.bind('<1>', click_point)
win.mainloop() #20x20












# all_fields = [[0, 0], [0, 50], [50, 0], [50, 50], [100, 0], [100, 50], [150, 0], [150, 50], [0, 100], [0, 150], [0, 200], [0, 250], [0, 300],
#     [50, 100], [50, 150], [50, 200], [50, 250], [50, 300], [100, 100], [100, 150], [100, 200], [100, 250], [100, 300], [150, 100], [150, 150],
#     [150, 200], [150, 250], [150, 300], [200, 0], [200, 50], [200, 100], [250, 0], [250, 50], [250, 100], [300, 0], [300, 50], [300, 100], [350, 0],
#     [350, 50], [350, 100], [400, 0], [400, 50], [400, 100], [450, 0], [450, 50], [450, 100], [500, 0], [500, 50], [500, 100], [550, 0], [550, 50],
#     [550, 100], [600, 0], [600, 50], [600, 100], [600, 150], [600, 200], [650, 0], [650, 50], [650, 100], [650, 150], [650, 200], [700, 0],
#     [700, 50], [700, 100], [700, 150], [700, 200], [750, 0], [750, 50], [750, 100], [750, 150], [750, 200], [800, 0], [800, 50], [800, 100],
#     [800, 150], [800, 200], [850, 0], [850, 50], [850, 100], [850, 150], [850, 200], [600, 250], [650, 250], [700, 250], [750, 250], [800, 250],
#     [850, 250], [600, 300], [650, 300], [700, 300], [750, 300], [800, 300], [850, 300], [600, 350], [650, 350], [700, 350], [750, 350], [800, 350],
#     [850, 350], [200, 150], [200, 200], [200, 250], [200, 300], [250, 150], [250, 200], [250, 250], [250, 300], [300, 150], [300, 200], [300, 250],
#     [300, 300], [350, 150], [350, 200], [350, 250], [900, 0], [900, 50], [900, 100], [900, 150], [900, 200], [900, 250], [950, 0], [950, 50],
#     [950, 100], [950, 150], [950, 200], [950, 250], [0, 350], [0, 400], [0, 450], [0, 500], [0, 550], [50, 350], [50, 400], [50, 450], [50, 500],
#     [50, 550], [100, 350], [100, 400], [100, 450], [100, 500], [100, 550], [150, 350], [150, 400], [150, 450], [150, 500], [150, 550], [200, 350],
#     [200, 400], [200, 450], [200, 500], [200, 550], [900, 300], [900, 350], [900, 400], [950, 300], [950, 350], [950, 400], [600, 400],
#     [650, 400], [700, 400], [750, 400], [800, 400], [850, 400], [0, 600], [0, 650], [0, 700], [0, 750], [0, 800], [50, 600], [50, 650],
#     [50, 700], [50, 750], [50, 800], [100, 600], [100, 650], [100, 700], [100, 750], [100, 800], [150, 600], [150, 650], [150, 700],
#     [150, 750], [150, 800], [200, 600], [200, 650], [200, 700], [200, 750], [200, 800], [750, 450], [750, 500], [750, 550], [750, 600],
#     [750, 650], [750, 700], [800, 450], [800, 500], [800, 550], [800, 600], [800, 650], [800, 700], [850, 450], [850, 500], [850, 550],
#     [850, 600], [850, 650], [850, 700], [900, 450], [900, 500], [900, 550], [900, 600], [900, 650], [900, 700], [950, 450], [950, 500],
#     [950, 550], [950, 600], [950, 650], [950, 700], [550, 150], [550, 200], [550, 250], [550, 300], [550, 350], [550, 400], [550, 450], [550, 500],
#     [550, 550], [550, 600], [550, 650], [550, 700], [600, 450], [600, 500], [600, 550], [600, 600], [600, 650], [600, 700], [650, 450],
#     [650, 500], [650, 550], [650, 600], [650, 650], [650, 700], [700, 450], [700, 500], [700, 550], [700, 600], [700, 650],
#     [700, 700], [800, 750], [800, 800], [800, 850], [800, 900], [850, 750], [850, 800], [850, 850], [850, 900], [900, 750],
#     [900, 800], [900, 850], [900, 900], [950, 750], [950, 800], [950, 850], [950, 900], [400, 150], [400, 200], [400, 250],
#     [400, 300], [450, 150], [450, 200], [450, 250], [450, 300], [500, 150], [500, 200], [500, 250], [500, 300], [400, 350],
#     [400, 400], [400, 450], [450, 350], [450, 400], [450, 450], [500, 350], [500, 400], [500, 450], [250, 350], [250, 400],
#     [250, 450], [250, 500], [250, 550], [250, 600], [300, 350], [300, 400], [300, 450], [300, 500], [300, 550], [300, 600],
#     [550, 750], [550, 800], [600, 750], [600, 800], [650, 750], [650, 800], [700, 750], [700, 800], [750, 750], [750, 800],
#     [0, 850], [0, 900], [0, 950], [50, 850], [50, 900], [50, 950], [100, 850], [100, 900], [100, 950], [150, 850], [150, 900],
#     [150, 950], [550, 850], [550, 900], [600, 850], [600, 900], [650, 850], [650, 900], [700, 850], [700, 900], [750, 850],
#     [750, 900], [450, 500], [450, 550], [450, 600], [450, 650], [450, 700], [450, 750], [500, 500], [500, 550], [500, 600],
#     [500, 650], [500, 700], [500, 750], [450, 800], [450, 850], [450, 900], [500, 800], [500, 850], [500, 900], [200, 850],
#     [200, 900], [200, 950], [250, 850], [250, 900], [250, 950], [300, 850], [300, 900], [300, 950], [350, 850], [350, 900],
#     [350, 950], [400, 850], [400, 900], [400, 950], [350, 300], [350, 350], [350, 400], [350, 450], [350, 500], [350, 550],
#     [350, 600], [350, 650], [350, 700], [400, 500], [400, 550], [400, 600], [400, 650], [400, 700], [450, 950], [500, 950],
#     [550, 950], [600, 950], [650, 950], [700, 950], [250, 650], [250, 700], [250, 750], [250, 800], [300, 650], [300, 700],
#     [300, 750], [300, 800], [800, 950], [850, 950], [900, 950], [950, 950], [350, 750], [350, 800], [400, 750], [400, 800], [750, 950]]