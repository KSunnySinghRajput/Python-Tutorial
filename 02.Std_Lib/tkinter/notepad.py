from tkinter import *
notepad_root = Tk()

#GEOMETRY("WIDTHxHEIGHT")
notepad_root.geometry("850x500")

#MINSIZE(WIDTH,HEIGHT)
notepad_root.minsize(200,100)

#MAXSIZE(WIDTH,HEIGHT)
notepad_root.maxsize(1200,900)

#INSERT_LABEL
lebel = Label(text="This Is My First GUI")
lebel.pack()

#INSERT_PHOTO
photo = PhotoImage(file="American-Actress.png")
image_label = Label(image=photo)
image_label.pack()

notepad_root.mainloop()
