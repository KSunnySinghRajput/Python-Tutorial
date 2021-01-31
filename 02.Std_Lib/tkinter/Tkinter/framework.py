from tkinter import *  
def ScalPrint(val):
        print(val)   #val is Str
def sunny():
        print("hello")
def mainpanel():    #mainframe(top)
        top = Tk()      #create object
        top.state('zoomed')           
        top.title("First Frame")     #Title Name In Upper Title bar
        top.geometry("720x480")      #SIZE Frame
        BgColor="orange"
        top.configure(bg=BgColor) 
        #-->top.iconbitmap(r'C:\Users\KunwarSunnySingh\Desktop\ProjectPython\Tkinter\Fb.icon')
#pack(Label-photo)
        #photo = PhotoImage(file='02.png')
        #labelphoto =Label(top,image=photo)
        #labelphoto.pack()
        
#pack(Label-text)
        #text = Label(top,text='------Fill Detail-----')
        #text.pack()                     #pack Label In Frame
            
#pack(command button)
        #btn= Button(top,text="print",command=sunny)
        #btn.pack()
#pack(Scale)
        #scal =Scale(top,from_=1,to=100,orient=HORIZONTAL,command=ScalPrint)
        #scal.set(4)
        #scal.pack()
#pack(Frame)
        fr=Frame(top)
        fr.pack()

#canvas = Canvas(top)
#canvas.create_line(10, 10, 200, 50)
#canvas.place(x=580,y=10)

# menubutton = Menubutton(top, text = "Language", relief = FLAT)  

#menubutton.menu = Menu(menubutton)  
#menubutton["menu"]=menubutton.menu  
#menubutton.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
#menubutton.menu.add_checkbutton(label = "English", variable = IntVar())  
#menubutton.pack()
        top.mainloop()
def main():
        mainpanel()
        
if __name__ == '__main__':
        main()
