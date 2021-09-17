from openpyxl import Workbook
from openpyxl import load_workbook

# write_wb = Workbook()
# # 워크북 인스턴스 생성
# # write_wb.save("test.xlsx")

# write_ws = write_wb.create_sheet("sheet1")

# write_ws = write_wb.active
# write_ws["a1"] = "1 row a column"

# write_ws.append([1, 2, 3])

# write_ws.cell(5, 5, "5row 5column")

# write_wb.save("D:/horolro/testpytoex.xlsx")

load_wb = load_workbook("D:/horolro/test_output.xlsx", data_only=True)
# data_only=True 값으로 받아오기.

load_ws = load_wb["RFID"]

print(load_ws["C5"].value)
# 배열 주소 사용
print(load_ws.cell(3, 2).value)
# 모듈 내 함수 사용

get_cells = load_ws["B3":"B6"]
for row in get_cells:
    for cell in row:
        print(cell.value)
