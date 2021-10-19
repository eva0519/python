import os
import time
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Image Merge Tool")

root.geometry("+550+200")

# 병합 이미지 선택 함수 정의
def file_open():
    files = filedialog.askopenfilenames(
        title="병합시킬 이미지를 선택해주세요.",
        filetype=(("모든 파일", "*.*"), ("PNG 파일", "*.png"), ("JPG 파일", "*.jpg"), ("BMP 파일", "*.bmp"), ("GIF 파일", "*.gif")),
        initialdir=r"D:\목포어린이도서관[전산]\2021년\4. 홈페이지\2021독서의달",
    )
    for file in files:
        list_file.insert(END, file)


# 선택 이미지 삭제 함수 정의
def file_selected_del():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로 설정 함수 정의
def save_file_path():
    save_path = filedialog.askdirectory()

    # 취소시 undefine 이나 Null 값이 아닌 str type ("") 을 return 하기 때문에 다른 조건식을 사용한 예외처리가 필요.
    if len(save_path) == 0:
        return

    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, save_path)


# 병합 프로세스
def image_merge():
    # list 이미지로부터 정보 추출
    images = [Image.open(x) for x in list_file.get(0, END)] # class 'PIL.JpegImagePlugin.JpegImageFile' 타입으로 배열 저장
    images_width = [x.size[0] for x in images]
    images_height = [x.size[1] for x in images]

    print("이미지 가로 해상도 : ", images_width)
    print("이미지 세로 해상도 : ", images_height)

    # canvas 준비
    width_max, height_total = max(images_width), sum(images_height)
    print('이미지 가로 최대 값 : ', width_max, '\n이미지 세로 통합 값 : ', height_total)

    result_img = Image.new('RGB', (width_max, height_total), (255, 255, 255))
    y_offset = 0
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]  # 각 이미지 height value 꺼내와서 offset 변수 증감

        # progressbar sync
        time.sleep(0.1)  # 동기화 확인용 나중에 삭제
        progress = ((idx + 1) / len(images)) * 100  # (1,2,3... / 이미지 갯수) * 100 
        p_var.set(progress)
        progressbar.update()

    dest_path = os.path.join(txt_dest_path.get(), 'mergeImage.jpg')
    result_img.save(dest_path)
    msgbox.showinfo(title='성공', message='이미지 병합이 완료되었습니다.')

# 예외처리 : 이미지 미선택, 저장 경로 미설정
def start():
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    if list_file.size() == 0:
        msgbox.showwarning(title='경고', message="병합시킬 이미지가 존재하지 않습니다.")
        msgbox.showinfo(message="이미지 병합이 중단되었습니다.")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning(title='경고', message="저장 경로가 설정되어있지 않습니다.")
        msgbox.showinfo(title='알림', message="이미지 병합이 중단되었습니다.")
        return

    print("이미지 병합을 시작합니다.")

    image_merge()


# 미리보기 (다중 선택으로 인한 오류 발생시 예외처리)
def file_preview():
    try:
        img = Image.open(list_file.selection_get())
        img.show()
        # print(type(img)) 변수 타입 class 'PIL.JpegImagePlugin.JpegImageFile'
    except:
        msgbox.showerror(title='실패', message='한개의 이미지만 선택해주세요.')
        return


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=file_open)
btn_add_file.pack(side="left")

btn_image_preview = Button(file_frame, padx=5, pady=5, width=12, text="이미지 미리보기", command=file_preview)
btn_image_preview.pack(side="left", padx=5)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=file_selected_del)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)  # ipady 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=save_file_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 넓이 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 넓이 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progressbar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
