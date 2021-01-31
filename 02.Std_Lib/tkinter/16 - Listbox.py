from tkinter import *

def add():
    global i
    lbox.insert(ACTIVE, f"{i}")
    i+=1
i = 0
root = Tk()
root.title("Listbox")
root.geometry("400x300")
lbox = Listbox(root)
lbox.pack()
lbox.insert(END, "First Item")
Button(root,text="Add Items", command=add).pack()

root.mainloop()