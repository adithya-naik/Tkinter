from tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side= BOTTOM)
but1 = Button(root,text="YES",fg="red",bg="yellow")
but1.pack()
but2 = Button(root,text="YES",fg="red",bg="yellow")
but2.pack(fill=X)
but3 = Button(root,text="YES",fg="red",bg="yellow")
but3.pack(fill=X)
root.mainloop()