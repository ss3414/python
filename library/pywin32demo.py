# ****************************************************************分割线****************************************************************
# todo xls转xlsx

import win32com.client

file = "C:\\Users\\Administrator\\Desktop\\test.xls"  # 必须使用\\分隔符
excel = win32com.client.gencache.EnsureDispatch("Excel.Application")

workbook = excel.Workbooks.Open(file)
workbook.SaveAs(file + "x", FileFormat=51)  # 51xlsx，56xls
excel.Application.Quit()
