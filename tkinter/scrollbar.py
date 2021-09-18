from tkinter import *
from typing import List

root = Tk()
root.title('frame')
root.geometry("640x480+800+400")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1,32): # 1 ~ 31 일
    listbox.insert(END, str(i) + '일')

listbox.pack(side='left')

# 스크롤바와 리스트박스를 서로 매핑해줘야 정상적으로 동작함
scrollbar.config(command=listbox.yview)

root.mainloop()
