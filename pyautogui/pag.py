import pyautogui as pg

# position = pyautogui.position()
# print(position)

# 좌표 객체 인스턴스 생성

# print(pyautogui.size())

# print(position.x)
# print(position.y)
# print("{0}, {1}".format(position.x, position.y))

# pyautogui.moveTo(500, 500)
# pyautogui.moveTo(800, 800, 2)  # 2초에 걸쳐 이동
# pyautogui.moveRel(-200, -200, 1)  # 현재 위치에서 x-200, y-200 만큼 이동

# pyautogui.click()
# pyautogui.moveTo(716, 330)
# pyautogui.click(clicks=2, interval=0.05)  # 2초간격 2번클릭
# pyautogui.doubleClick()
# pyautogui.sleep(2)
# pyautogui.click(button="right")
# pyautogui.scroll(1000)

button5location = pg.locateOnScreen("d:/horolro/img/5.png")
print(button5location)

# PyAutoGui 는 듀얼 모니터일 경우 주 모니터만을 처리한다.
# locateOnScreen 함수의 confidence 인자를 사용하기 위해선 opencv_python가 필요하다
# grayscale 인자를 사용해서 hover css 기능이 있는 버튼 등에 대처하자.
# 예외처리를 하는 게 더 확실하긴 함.

point = pg.center(button5location)  # box 객체의 중앙 좌표를 리턴
print(point)

pg.click(point)

import matplotlib.pyplot as plt
import numpy as np
import cv2

print(cv2.__version__)
