import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
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

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 + 50
    
    key = ""  #現在押されているキーを表す
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canv, maze_list)
    main_proc()
    
    canv.create_image(cx, cy, image=tori, tag="こうかとん")

    root.mainloop()