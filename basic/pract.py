from random import randint, shuffle, sample
import time
import pyautogui

# 와일드카드* 를 통해 모듈의 모든 기능을 import 하는 것은 pep8에서 권장하고 있지 않다.
# 메모리 상에 쓰지도않는 기능을 적재시킬 필요는 없으므로 필요한 것만 import하여 사용하자.

screenWidth, screenHeight = pyautogui.size()
print("{0}, {1}".format(screenWidth, screenHeight))
mouseX, mouseY = pyautogui.position()
print("{0}, {1}".format(mouseX, mouseY))

time.sleep(1)
pyautogui.click(x=42, y=43)
time.sleep(1)
pyautogui.click(x=38, y=139)
time.sleep(1)
pyautogui.click(x=39, y=226)
time.sleep(1)
pyautogui.click(x=39, y=321)

print(randint(4, 28))
stringNop = "Python is Not Amazing"
print(stringNop.lower())
print(stringNop.upper())
print(stringNop[0].islower())  # false
print(len(stringNop))
print(stringNop.replace("Python", "Java"))
# stringNop[0:3]  # 0,1,2 번째 인덱스만 잘라옴. :4 처음부터 3번째까지, 4: 4번째부터 끝까지, -1~ 마지막부터 순서대로
index = stringNop.index("n")
print(index)
index = stringNop.index("n", index + 1)  # n 이후 오는 n의 인덱스번호
print(index)
print(stringNop.count("n"))  # n의 총갯수
print(stringNop.find("n"))
# index와 같으나 존재하지 않는 값을 찾을 경우 -1을 반환한다. index는 value error를 띄움.
# 조건문과 쓸때는 find를 쓰는게 조건식을 만들기 좋음.
print("decimal? determine? %d" % 18)
print("string array %s" % "wow")
print("string array %s %s two" % ("3", "5"))
print("character %c only one word" % "a")
print("{},{}".format("a", "b"))
print("{one},{two} how".format(one="4", two=5))
# print(one)  # 해도 안나옴. .format 내부 스코프로 임시 적용된 변수므로 저장되지 않는다.

# python 3.6 이상 --------
age = 30
wordto = "howhow"
print(f"{age}! {wordto}!")
# -------------------------

print("백문이 불여일견\n백견이 불여일타")
print('너어무 "졸"려요')
# 탈출문자 \"내용\" dark syntax 교정 플러그인 때문에 저절로 작은 따옴표로 바뀐다.
# \' , \" 문장내에서 따옴표
# \\ 문장내에서 \ 한개로 변환
# \n 줄바꿈, \r 컨서를 맨앞으로 이동
print("Red Apple\rPine")
# \b 백스페이스
print("Redd\bApple")
# \t 탭
print("Red\tApple")

stArray = "http://naver.com"
reArray = stArray.replace("http://", "")
slArray = reArray[: reArray.find(".")]
# print funtion에는 str type 밖에 오지못하므로 typecasting이 필요하다.
print(slArray[0:3] + str(len(slArray)) + str(slArray.count("e")) + "!")


# Array
subway = ["유재석", "조세호", "박명수"]
print(subway)
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway)
print(subway.pop(1))
print(subway)
print(subway.count("유재석"))

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

mix_list = ["조세호", 20, True]
print(mix_list)

num_list = [3, 2, 1, 6, 5]
num_list.extend(mix_list)
print(num_list)

num_list.append([4, 7])
print(num_list)
num_list.insert(7, [13, 14])
print(num_list)
# append, insert는 배열로 추가시 리스트 형태 그대로 추가된다.


# dictionary
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet.get(100))
# print(cabinet[5]) 배열을 이용해 존재하지 않는 키값을 찾아오려하면 에러가 나면서 이후 코드가 실행되지 않는다.
print(cabinet.get(5, "사용 가능한 key 입니다."))
print("hi")
# .get을 사용할 경우에는 이후 코드까지 실행이 가능하다. 두번째 인자를 주지않을 경우 NONE을 출력한다.
print(3 in cabinet)  # True
print(5 in cabinet)
print(100 in cabinet)

cabinet = {"A-3": "유재석", "F-100": "김태호"}
print(cabinet["F-100"])
print(cabinet.get("A-3"))
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)
del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()
print(cabinet)


# Tuple (배열보다 속도가 빠르므로 변경되지 않는 리스트를 사용할때 유용하다)
menu = ("dongatz", "cheesegatz")
print(menu[0])
print(menu[1])

# menu.add("fishgatz") 튜플은 값 추가 변경이 불가능하다.

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)


# Set
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"m.u", "k.t", "y.h"}
python = set(["m.u", "p.m"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합  중복을 제거한다. 순서 없음
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# Xor
print(java ^ python)

python.add("k.t")
java.remove("k.t")


# 자료구조의 변경
menu = {"coffe", "milk", "juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

lst = range(1, 21)  # 1부터 20까지 숫자를 생성
print(type(lst))  # class range type이 나오므로 list형으로 변환해야 한다.
lst = list(lst)
print(type(lst))
print(lst)
shuffle(lst)
print(lst)
# print(
#     "-- public order--\nchiken bonus : "
#     + str(lst[0])
#     + "\ncoffee bonus : "
#     + str(sample(lst, 3))
#     + "\n-- congraturation! --"
# )

winner = sample(lst, 4)
print(winner)
chiken_one = winner[0]
coffee_one = winner[1:]
print("-- public order--")
print("chiken bonus : {0}".format(chiken_one))
print("coffee bonus : {0}".format(coffee_one))
print("-- congraturation!--")


# 조건문
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))  # input은 항상 string으로 값을 받기에 int로 형변환 해줘야한다.
if temp >= 30:
    print("너무 더워요 나가지 마")
elif 10 <= temp & temp < 30:  # temp and temp
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
