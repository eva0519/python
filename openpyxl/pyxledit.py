from openpyxl import Workbook

wb = Workbook()  # load_workbook 과 동일한 타입의 인스턴스를 가진다.
ws = wb.active # 항상 최소 하나의 시트를 가지고 생성, 첫 시트가 활성화된 채로 만들어짐. active를 사용하여 첫 시트를 얻음.

ws1 = wb.create_sheet("mysheet") # insert at the end
ws2 = wb.create_sheet("mysheet", 0) # insert at first position
ws3 = wb.create_sheet("mysheet", -1) # insert at second position from the end

ws.title = 'mysheet' # sheet name edit

# copy
wscopy = wb.copy_worksheet(ws) # workbook 열려있는 경우 복사가 불가능
