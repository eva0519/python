import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
print("{0}, {1}".format(screenWidth, screenHeight))

mouseX, mouseY = pyautogui.position()
print("{0}, {1}".format(mouseX, mouseY))

pc_resolution : 1680, 1050
dual_channel_resolution : 3338, 1046

time.sleep(1)
pyautogui.click(x=733, y=36)
time.sleep(1)
pyautogui.click(x=800, y=44)
time.sleep(1)
pyautogui.click(x=871, y=47)
time.sleep(1)
pyautogui.click(x=943, y=47)
time.sleep(1)
pyautogui.click(x=1027, y=45)
pyautogui.click(x=1027, y=45)

import numpy as np  # 다차원 배열을 쉽게 처리할 수 있는 함수를 모아놓은 라이브러리. 산술적처리가 필요한 프로그램에서 필요한 함수를 굉장히 많이 가지고 있다.

x = np.arange(-10, 10, 1)  # A ~ B jump to numbering   \\ 1의 간격으로 나눈 실수 생성. 출력 갯수는 나누는 수에 따라 다르다.
print(x)

# a = np.linspace(-np.pi, np.pi, 100)  # between -PI and PI divide 100  \\100개의 구간으로 나눈 실수 생성. 출력 갯수를 정할 수 있다.
# print(a)

y = 2 * x - 1
print(y)
# [i * 2 - 1 for i in x] 를 써도 되지만 위처럼 해도 같은 결과값이 출력된다.

import matplotlib.pyplot as plt  # matplotlib python에서 그래프 출력이 가능케 해주는 라이브러리

# a = np.linspace(0, 10, 100)
# b = np.exp(-a)
# plt.plot(a, b)
# plt.show()

plt.plot(x, y)
# plt.show()

# x.shape[0]은 x배열의 크기(원소의 개수를)를 나타내는데, 원소 개수는 20개입니다. 대신, len 함수를 사용하여 len(x)로 입력해도 같은 결과를 보입니다.
# arr_size = x.shape[0]
# print(arr_size)  # value = 20
# print(len(x)) # value = 20  문자열은 배열이고 포인터다. len은 문자열의 갯수가 아닌 메모리주소 n값을 기반으로 하기 때문에 리스트 갯수파악에 사용가능하다.

print("x 배열의 원소 개수 : {0}".format(x.shape[0]))
idx = np.arange(x.shape[0])
print("기존 인덱스 : {0}".format(idx))
np.random.shuffle(idx)
print("섞인 인덱스 : {0}".format(idx))

from random import shuffle, sample

x = x[idx]
print("x:", x)
y = y[idx]
print("y:", y)

import math

fac5 = math.factorial(5)
print(fac5)


def factorial_for(n):
    ret = 1
    for i in range(1, n + 1):
        ret = ret * i

    return ret


# define function

def_fac5 = factorial_for(5)
print(def_fac5)

x_new = x.reshape(-1, 1)
# reshape 메소드는 행열의 형태를 변환할 수 있다. arg1은 행의 갯수(여기서는 -1로 기존 배열을 참조함을 의미) arg2는 열의 갯수를 입력한다.
# 20열로 이루어진 일차원 배열을 세로로 긴 이차원 배열로 변환할 것이므로 1열에 -1행의 인자를 입력시킨다.\
print(x_new)
# 출력에서 이차원 배열은 2개의 인자값을 가지게 되므로 메모리상에는 arg2의 인자값이 이차원 배열의 행의 주소를 고정하게된다. ex) 1,1 2,1 3,1 4,1

plt.plot(x_new, y)
# plt.show()

from sklearn.linear_model import LinearRegression

# sklearn 사이킷런. 통계학에 사용되는 툴을 지원하는 라이브러리. LinearRegression은 선형회귀분석을 처리하는데 사용된다.

lr = LinearRegression()
# print(type(lr))

# 사용법
# LinearRegression(fit_intercept=False, n_jobs=-1) 이렇게 정의하면 일차함수식의 y절편인 b값을 계산하지 않는다.
# 첫번째 인자값을 True로 주면 계산하게한다. n_jobs는 CPU 코어를 몇개 사용할지 정하는 것. -1이면 전부 사용. 1이면 1개만 2면 2개만 사용하는 식이다.

lr.fit(x_new, y)
print("기울기: ", lr.coef_)
print("y절편: ", lr.intercept_)

# fit 함수는 y의 예측 오차값이 가장 적은 결과값을 찾아내준다.
