from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("RadioButton")
root.geometry("400x300")
def value():
    print(f"You choose {var.get()}")
    tmsg.showinfo("Value", f"You have place order for {var.get()}")
Label(root, text="What you want to purchase",font="Lucida 14 bold").pack()
# var=IntVar()
var=StringVar()
var.set(1)
radio = Radiobutton(root, text="Apple", variable=var, value="Apple").pack(anchor='w')
radio = Radiobutton(root, text="Banana", variable=var, value="Banana").pack(anchor='w')
radio = Radiobutton(root, text="Orange", variable=var, value="Orange").pack(anchor='w')
radio = Radiobutton(root, text="Mango", variable=var, value="Mango").pack(anchor='w')
Button(root, text="Submit", command=value).pack()
root.mainloop()