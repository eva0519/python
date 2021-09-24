import time
from PIL import ImageGrab
from tkinter import *

root = Tk()
root.title('이미지 연속 캡쳐 프로그램')
root.geometry('100x100+800+400')

def image_ct():

    # 버튼 클릭 후 대기시간 5초
    for i in range(5, 0, -1):
        text.set('{}'.format(i))
        btn.update()
        time.sleep(1)

    text.set('캡쳐 중...')
    btn.update()

    # 이미지 저장시간 간격 설정
    for i in range(1,7):
        img = ImageGrab.grab()
        img.save('image{}.png'.format(i))
        time.sleep(1) # 1초 간격 6장

    text.set('캡쳐 완료')
    btn.update()
    time.sleep(3)
    text.set('캡쳐 시작')

# 버튼 / 텍스트 바인딩
text = StringVar()  
text.set('캡쳐 시작')
btn = Button(root, textvariable=text, command=image_ct, width=100, height=100)
btn.pack()

root.mainloop()
