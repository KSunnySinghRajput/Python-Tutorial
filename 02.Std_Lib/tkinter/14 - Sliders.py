from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Sliders")
root.geometry("800x500")
def getmoney():
    print(f"The money you will get {slider_v.get()}")
    tmsg.showinfo("Value", f"You have applied for {slider_v.get()}k money")
Label(root, text="Apply for Money").pack()
# slider_h = Scale(root, from_=0, to=100)       #Bydefault - Horizental
# slider_h.pack()
slider_v = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
slider_v.pack()
Button(root, text="Submit", command=getmoney).pack()
root.mainloop()