import time
from random import randint
from tkinter import *
import pyautogui as pg

root = Tk()
root.title("Image Merge Tool")

SCREENWIDTH, SCREENHEIGHT = pg.size()

APPWIDTH = 640
APPHEIGHT = 480
app_x_pos = int((SCREENWIDTH / 2) - (APPWIDTH / 2))
app_y_pos = int((SCREENHEIGHT / 2) - (APPHEIGHT / 1.5))

root.geometry(("{0}x{1}+{2}+{3}").format(APPWIDTH, APPHEIGHT, app_x_pos, app_y_pos))

"""
dynamic screen size
"""

root.resizable(False, False)  # x, y

"""
window cunstomizable size option
"""

lb_select_file = Label(root, text="병합시킬 이미지를 선택하세요")
lb_select_file.place(x=20, y=25)

pathImages = PhotoImage(file="img/")

image_listbox = Listbox(root, selectedmode="extended", height=0)
listbox.insert(END, pathImages)
image_listbox.place(x=20, y=35)

selected_image = image_listbox.curselection()

def btncmd():
    print('선택 항목' : selected_image)

lb_total = LAbel(root, text=selected_image.size(), " / ", image_listbox.size())

entry = Entry(root, fg="gray19", bg="snow", width=int(APPWIDTH * 0.1))
gray_text = "path/"
entry.insert(0, gray_text)
entry.place(x=20, y=325)

lb_ver = Label(root, text="Ver 0.00")
lb_ver.place(x=(APPWIDTH * 0.9), y=(APPHEIGHT - 25))

def mergebtn():
    pass

merge_btn = Button(text="병합", padx=5, pady=5, bg="gray19", fg="gray100", commend=mergebtn)
merge_btn.place(x=APPWIDTH * 0.85, y=315)

root.mainloop()
