import tkinter as tk
import maze_maker as mm
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def change_photo(): #画像の切り替え
    global index
    canv.delete("こうかとん")
    index =(index+1)%len(bards)
    canv.create_image(cx, cy, image=bards[index], tag="こうかとん")

def main_proc():
    global mx, my, cx, cy, index
    if key == "Up":
        my -= 1
        change_photo() 
    if key == "Down":
        my += 1
        change_photo()
    if key == "Left":
        mx -= 1
        change_photo()
    if key == "Right":
        mx += 1
        change_photo()
    if maze_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("こうかとん", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, background="black")
    canv.pack()

    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 + 50
    index = 0
    
    key = ""  #現在押されているキーを表す
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canv, maze_list)

    bards = [tk.PhotoImage(file="ex03/fig/1.png"), #画像のリスト
             tk.PhotoImage(file="ex03/fig/2.png"),
             tk.PhotoImage(file="ex03/fig/3.png"),
             tk.PhotoImage(file="ex03/fig/4.png"),
             tk.PhotoImage(file="ex03/fig/5.png"),
             tk.PhotoImage(file="ex03/fig/6.png"),
             tk.PhotoImage(file="ex03/fig/7.png"),
             tk.PhotoImage(file="ex03/fig/8.png"),
             tk.PhotoImage(file="ex03/fig/9.png")]
    canv.create_image(cx, cy, image=bards[index], tag="こうかとん")
    main_proc()
    root.mainloop()