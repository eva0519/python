from tkinter import *

root = Tk()
root.title('label')

root.geometry("300x300+100+100")

label1 = Label(root, text="label hi")
label1.place(x=30, y=30)

root.mainloop()
