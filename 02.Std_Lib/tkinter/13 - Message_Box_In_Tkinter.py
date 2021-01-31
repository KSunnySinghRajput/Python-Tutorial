from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Menus and Submenus")
root.geometry("800x500")

menu_bar = Menu(root)

sub_menu1 = Menu(menu_bar, tearoff=0)
sub_menu1.add_command(label="New")
sub_menu1.add_command(label="Open")
sub_menu1.add_command(label="Save")
sub_menu1.add_command(label="Save As")
sub_menu1.add_separator()
sub_menu1.add_command(label="Page Setup")
sub_menu1.add_command(label="Print")
sub_menu1.add_separator()
sub_menu1.add_command(label="Exit")
root.config(menu=menu_bar)
menu_bar.add_cascade(label="File", menu=sub_menu1)

sub_menu2 = Menu(menu_bar, tearoff=0)
sub_menu2.add_command(label="Undo")
sub_menu2.add_separator()
sub_menu2.add_command(label="Cut")
sub_menu2.add_command(label="Copy")
sub_menu2.add_command(label="Paste")
sub_menu2.add_command(label="Delete")
sub_menu2.add_separator()
sub_menu2.add_command(label="Find")
sub_menu2.add_command(label="Find Next")
sub_menu2.add_command(label="Replace")
sub_menu2.add_command(label="Go To")
sub_menu2.add_separator()
sub_menu2.add_command(label="Select All")
sub_menu2.add_command(label="Date/Time")
root.config(menu=menu_bar)
menu_bar.add_cascade(label="Edit", menu=sub_menu2)

def help():
    print("How Can I Help You?")
    tmsg.showinfo("Help", "We will Help You")
    # You can Also Show The Return Value of .showinfo Class
    # r = tmsg.showinfo("Help", "We will Help You")
    # print(r)

def feedback():
    print("Please Give Us Feedback")
    tmsg.askyesno("Rate Us", "Please Give Us Feedback")
    # You can Also Show The Return Value of .askyesno Class
    # r = tmsg.askyesno("Feedback", "Please Give Us Feedback")
    # print(r)

def rate():
    print("Please Rate Us")
    r = tmsg.askquestion("Rate Us", "Are You Satisfied With Our Service")
    # You can Also Show The Return Value of .askquestion Class
    # r = tmsg.askquestion("Rate Us", "Are You Satisfied With Our Service")
    # print(r)
    if r == "yes":
        msg = "Thank You, Plesae write some valuable comment about us"
    else:
        msg = "Please Give Us Some Suggestions to Improve"
    tmsg.showinfo("User Experience",msg)

sub_menu3 = Menu(menu_bar, tearoff=0)
sub_menu3.add_command(label="Need Help", command=help)
sub_menu3.add_command(label="Feedback", command=feedback)
sub_menu3.add_command(label="Rate Us", command=rate)
root.config(menu=menu_bar)
menu_bar.add_cascade(label="Help", menu=sub_menu3)
root.mainloop()