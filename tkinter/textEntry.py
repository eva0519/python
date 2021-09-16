from tkinter import *

root = Tk()
root.title = 'text/entry'
root.geometry("640x480+900+400")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, '글자를 입력하세요')

e = Entry(root, width=30)
e.pack()
e.insert(0, '한줄만 입력해요')

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # get 첫번째 인자 1 : 첫번째 라인, 0 : column 시작 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()