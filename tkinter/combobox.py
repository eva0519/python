import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('frame')
root.geometry("640x480+800+400")
root.resizable(False, False)

values = [str(i) + "일" for i in range(1,31)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일')

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # readonly 읽기 전용
readonly_combobox.current(0) # 0 번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="결제", command=btncmd)
btn.pack()

root.mainloop()
