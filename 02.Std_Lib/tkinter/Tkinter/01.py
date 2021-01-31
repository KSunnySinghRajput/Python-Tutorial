from tkinter import *
from tkinter import ttk
root = Tk()
s = ttk.Scrollbar( root , orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=s.set)
root.mainloop()