#Event Handeling - Tkinter provides a mechanism to let the programmer deal with events. For each widget, it's possible to bind Python functions and methods to an event. If the defined event occurs in the widget, the "handler" function is called with an event object. describing the event.

from tkinter import *
def click(event):
    print(f"I have clicked {event.x}, {event.y}")

root = Tk()
root.geometry("800x500")
root.title("Event Handeling")

widget = Button(root, text='Click Here')
widget.pack()

widget.bind('<Button-1>',click)
widget.bind('<Double-Button-1>', quit)

root.mainloop()