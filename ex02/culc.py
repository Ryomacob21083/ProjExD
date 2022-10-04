from ast import operator
import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    if num == "×":
        num = "*"
    if num == "÷":
        num = "/"
    entry.insert(tk.END, num)


def click_equal(event):
    eqn = entry.get()
    #if "×" in str(eqn):
    #    str(eqn).replace("×", "*")
    #if "÷" in str(eqn):
    #    eqn = 5
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def click_clear(event):
    entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("500x600")

entry = tk.Entry(root, width = 10, font = (", 40"), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)

c1 = 0
r1 = 1
numbers = list(range(9, -1, -1))
decimal_point = ["."]
for i, num in enumerate(numbers + decimal_point, 1):
    btn = tk.Button(root, text = f"{num}", font = ("", 30), bg = "red", width = 4, height = 2)
    btn.bind("<1>", click_number)
    btn.grid(row = r1, column = c1)
    c1 += 1

    if i%3 == 0:
        r1 += 1
        c1 = 0

btn = tk.Button(root, text = f"C", font = ("", 30), width = 4, height = 2)
btn.bind("<1>", click_clear)
btn.grid(row = 0, column = 4)


c2 = 4
r2 = 1
operators = ["+", "-", "×", "÷"]
for i in operators:
    btn = tk.Button(root, text = f"{i}", font = ("", 30), bg = "yellow", width = 4, height = 2)
    btn.bind("<1>", click_number)
    btn.grid(row = r2, column = c2)
    r2 += 1


btn = tk.Button(root, text = f"=", font = ("", 30), bg = "blue", width = 4, height = 2)
btn.bind("<1>", click_equal)
btn.grid(row = r1, column = c1)

root.mainloop()