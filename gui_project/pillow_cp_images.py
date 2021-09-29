import time
from PIL import ImageGrab
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

root = Tk()
root.title('image transformer')
root.geometry('+800+400')
root.resizable(True,True)

# delay 설정 V
# 저장 간격 설정
# 저장 이름 설정
# 저장 경로 설정

def image_ct():

    # capture delay
    if delay_combobox.get() == '즉시 시작':
        pass
    else:
        for i in range(int(delay_combobox.get()), 0, -1):
            text.set('{}'.format(i))
            btn.update()
            time.sleep(1)

    text.set('캡쳐 중...')
    btn.update()

    # 이미지 저장시간 간격 설정
    for i in range(1,7):
        img = ImageGrab.grab()
        img.save('KYTimage{}.png'.format(i))
        time.sleep(1) # 1초 간격 6장

    text.set('캡쳐 완료')
    btn.update()
    time.sleep(3)
    text.set('캡쳐 시작')


# 스트리밍 정의
def streaming_save():
    pass

# delay frame
delay_frame = LabelFrame(root, width=10, text='캡쳐 대기 시간(Sec)')
delay_frame.pack(fill='x')

# img_catch_delay input combobox
delay_values = []
for i in range (0, 31):
    if i > 0:
        delay_values.insert(i, i)
    else:
        delay_values.append('즉시 시작')

delay_combobox = ttk.Combobox(delay_frame, height=10, values=delay_values, state="readonly")
delay_combobox.current(0)
delay_combobox.pack(pady=10)

print(delay_values)

# def btncmd():
#     print(delay_combobox.get())

# Button(delay_frame, command=btncmd, text='(test) 시간 가져오기 버튼').pack(pady=10)

# 버튼 / 텍스트 바인딩
text = StringVar()  
text.set('캡쳐 시작')
btn = Button(root, textvariable=text, command=image_ct, width=30)
btn.pack(fill=BOTH, pady=5, padx=5, expand=True) # expand 를 통해 세로 확장 가능

# 이미지 병합 & 스트리밍 기능
text_gif = StringVar()
text_gif.set('움짤 작성')
btn_gif = Button(root, textvariable=text_gif, command=streaming_save)
btn_gif.pack(fill=BOTH, pady=5, padx=5, expand=True)

root.mainloop()
