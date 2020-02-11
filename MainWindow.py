from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization.
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        super().__init__(master)  

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)


        # create a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the "file" tab object
        file = Menu(menu)

        # adds a command to the menu option like exit in Explorer.
        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="Save")

        # add "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # add "edit" tab object
        # add a "Undo" label without command
        # add "edit" to our menu
        edit = Menu(menu, activebackground="red")
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)

        tree = Treeview(self.master)
        tree["columns"]=("one","two","three")
        tree.column("#0", width=270, minwidth=270, stretch=NO)
        tree.column("one", width=150, minwidth=150, stretch=NO)
        tree.column("two", width=400, minwidth=200)
        tree.column("three", width=80, minwidth=50, stretch=NO)

        tree.heading("#0",text="Name",anchor=W)
        tree.heading("one", text="Date modified",anchor=W)
        tree.heading("two", text="Type",anchor=W)
        tree.heading("three", text="Size",anchor=W)

        # Level 1
        folder1=tree.insert("", 1, text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
        tree.insert("", 2, text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
        # Level 2
        tree.insert(folder1, "end", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
        tree.insert(folder1, "end", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
        tree.insert(folder1, "end", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))
        
        # tree.place(x=20,y=20)

        tree.pack(side=TOP,fill=X)


    def showImg(self):
        load=Image.open("./assets/images/tenor.gif")
        render=ImageTk.PhotoImage(load)

        img=Label(self, image=render)
        img.image=render
        img.place(x=100, y=0)

    def showText(self):
        text = Label(self,text="Hi, there!")
        text.pack()
       

    def client_exit(self):
        exit()
        # newButton = Button(self, text="Second")
        # newButton.place(x=100, y=100)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("1000x1000")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  



# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()