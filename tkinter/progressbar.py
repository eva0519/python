
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('frame')
root.geometry("640x480+800+400")
root.resizable(False, False)

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.pack()
# progressbar.start(10) # 10ms 마다 움직임

# def btncmd():
#     progressbar.stop() # 작동 중지

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):  # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기
        p_var2.set(i)  # progress bar 의 값 설정
        progressbar2.update()  # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
