import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, background="black")
    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="こうかとん")

    key = ""  #現在押されているキーを表す
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()
