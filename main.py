# main.py
import tkinter as tk

root = tk.Tk()
root.geometry("200x100")
frame1 = tk.Frame(root, bg="red", width=1100, height=100)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(root, bg="yellow", width=1100, height=600)
frame2.grid(row=1, column=0)
canvas = tk.Canvas(frame2 , bg="white", width=1100, height=600)
canvas.grid(row=0, column=0)
previouspioint = [0, 0]
currentpoint = [0, 0]

def paint(event):
    global previouspioint, currentpoint
    x, y = event.x, event.y
    currentpoint = [x, y]
    if previouspioint != [0, 0]:
        canvas.create_line(previouspioint[0], previouspioint[1], currentpoint[0], currentpoint[1], fill="black")
    previouspioint = currentpoint
    if event.type == "5":
        previouspioint = [0, 0]
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
root.mainloop()

