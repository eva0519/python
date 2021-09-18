from tkinter import *

root = Tk()
root.title('label')

root.geometry("300x300+100+100")

label1 = Label(root, text="label hi")
label1.pack()
# label1.place(x=30, y=30)

photo = PhotoImage(file="tkinter/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="bye")

    global photo2 # garbage collection 때문에 전역변수로 선언해줘야함. 밖으로 빼던가.
    photo2 = PhotoImage(file="tkinter/xxx.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
