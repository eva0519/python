from openpyxl import load_workbook

wb = load_workbook("D:/horolro/openpyxl/testxl.xlsx")
# print(wb)

# print(wb.sheetnames)

# print(wb.get_sheet_names())  # 더 이상 사용되지 않는 함수 : DeprecationWarning: Call to deprecated function get_sheet_names

# print(wb['Sheet1'])
# print(wb['Sheet2'])

# a = wb.get_sheet_by_name('Sheet1') # 더 이상 사용되지 않는 함수 : DeprecationWarning: Call to deprecated function get_sheet_names
# print(a)

# ws = wb['Sheet1']
# print(ws)
# sheet 이름을 모를 때
# ws = wb[wb.sheetnames[0]]
# print(ws)

ws = wb[wb.sheetnames[0]]

# 셀에서 데이터값 불러오기 (value 가 존재하지 않을 경우 None (=0)을 리턴)
# print(ws['A1'].value)
# print(ws.cell(row=1, column=2).value)

get_data = ws['A1':'C2']
print(get_data)  # tuple

for row in get_data:
    for cell in row:
        print(cell.value, end=' ')
    print()

# column 단위로 끊어 tuple 형식으로 저장되어 있기에 2차원 배열을 써서 불러온다.    

print(ws.max_row) # 2
print(ws.max_column) # 3
print(ws.dimensions) # A1:C2
