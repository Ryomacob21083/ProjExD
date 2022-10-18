import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, background="black")
    canv.pack()

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="こうかとん")
    root.mainloop()
