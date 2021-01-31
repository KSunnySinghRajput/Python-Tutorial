#Canvas - In Tkinter, Canvas class is used to create different shapes with the help of some functions which are defined under Canvas class. Any shape that Canvas class creates requires a canvas, so before creating any shapes a Canvas object is required and needs to be packed to the main window.

from tkinter import *
root=Tk()
root.title("Canvas Widgets")
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

widget = Canvas(root, width=canvas_width, height=canvas_height)
widget.pack()
z
#The line goes from the point x1, y1 to x2, y2
widget.create_line(0,0,800,400, fill="blue")
widget.create_rectangle(100, 100, 700, 300, fill="red")
widget.create_oval(100,100,700,300, fill="yellow")

root.mainloop()