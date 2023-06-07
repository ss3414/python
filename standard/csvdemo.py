# ****************************************************************分割线****************************************************************
# todo csv

import csv

with open("C:/Users/Administrator/Desktop/test.csv", "r", encoding="UTF-8") as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)
