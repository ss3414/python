# ****************************************************************分割线****************************************************************
# todo 读取xlsx

# openpyxl无法读取xls

# import openpyxl
#
# workbook = openpyxl.load_workbook("C:/Users/Administrator/Desktop/test.xlsx")
# worksheet = workbook["Sheet1"]
# # print(worksheet["A1"].value)
#
# # 遍历Excel 1
# # for row in worksheet.iter_rows():
# #     for cell in row:
# #         if cell.value is None:
# #             print(cell.coordinate, "")
# #         else:
# #             print(cell.coordinate, cell.value)
#
# # 遍历Excel 2
# for i in range(1, worksheet.max_row + 1):
#     for j in range(1, worksheet.max_column + 1):
#         coordinate = worksheet.cell(row=i, column=j).coordinate
#         value = worksheet.cell(row=i, column=j).value
#         if value is None:
#             print(coordinate, "")
#         else:
#             print(coordinate, value)
