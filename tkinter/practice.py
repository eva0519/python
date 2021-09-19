'''
tkinter 를 이용한 메모장 프로그램

[GUI 조건]
1. title : 제목 없음 - Windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태 
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기
'''

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('제목 없음 - Windows 메모장')
root.geometry("640x480+400+100")
root.resizable(True, True)

docFile = "mynote.txt"

def openfile():
    response = msgbox.askyesno(title=None, message="진행 중인 작업 내용이 삭제될 수 있습니다. 진행하시겠습니까?")

    if response == 1:
        if os.path.isfile(docFile): # 있으면 True 없으면 False
            with open(docFile, "r", encoding='utf8') as file:
                txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
                txt.insert(END, file.read()) # 파일 내용을 본문에 입력

        # os.open(docFile, os.O_RDWR|os.O_CREAT) # r/w/d open or create

def savefile():
    with open(docFile, "w", encoding='utf8') as file:
        file.write(txt.get("1.0",END)) # 모든 내용을 가져와서 저장
    
menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=openfile)
menu_file.add_command(label='저장', command=savefile)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)

# 대 메뉴
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바, 텍스트 맵핑
txt_scrollbar = Scrollbar(root)
txt_scrollbar.pack(side='right', fill='y')

txt = Text(root, yscrollcommand=txt_scrollbar.set)
txt.pack(side='left', fill="both", expand = True)
txt_scrollbar.config(command=txt.yview)  # S/T Mapping

root.config(menu=menu)
root.mainloop()
