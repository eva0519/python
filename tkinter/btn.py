from tkinter import *

root = Tk()
root.title("prac")

btn = Button(root, padx=10, pady=10, width=10, height=10, fg="red", bg="blue", text='버튼')
btn.pack()

photo = PhotoImage(file="tkinter/check.png")
btn2 = Button(root, image=photo)
btn2.pack()

def btncmd():
    print('버튼 클릭')

btn3 = Button(root, text="동작하는 버튼", command=btncmd)
btn3.pack()

root.mainloop()

