import tkinter as tk

def kocka(canvas):
    canvas.create_rectangle(100, 100, 300, 300, fill="lightblue", outline="black", width=3)

def sziv(canvas):
    canvas.create_oval(100, 100, 200, 200, fill="red")
    canvas.create_oval(200, 100, 300, 200, fill="red")
    canvas.create_polygon(100, 150, 200, 300, 300, 150, fill="red")

def rombusz(canvas):
    canvas.create_polygon(200, 100, 300, 200, 200, 300, 100, 200, fill="orange", outline="black", width=3)

def haromszog(canvas):
    canvas.create_polygon(100, 300, 300, 300, 200, 100, fill="green", outline="black", width=3)
