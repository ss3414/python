# ****************************************************************分割线****************************************************************
# todo 段落

# from docx import Document
# from docx.enum.text import WD_BREAK
#
# doc = Document()
# doc.add_paragraph("第一页")
# doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
# doc.add_paragraph().add_run("第二页")
# doc.save("C:/Users/Administrator/Desktop/test.docx")

# ************************************************************半分割线******************************
# todo 创建表格

# from docx import Document
#
# doc = Document()
#
# # 创建表格
# table = doc.add_table(rows=3, cols=3)
# # 填充数据
# for i in range(3):
#     for j in range(3):
#         cell = table.cell(i, j)
#         cell.text = f"行{i + 1}-列{j + 1}"
#
# doc.save("C:/Users/Administrator/Desktop/test.docx")

# ************************************************************半分割线******************************
# todo 复制表格

# from copy import deepcopy
#
# from docx import Document
#
# demo_doc = Document("C:/Users/Administrator/Desktop/demo.docx")
# demo_table = demo_doc.tables[0]
#
# new_table = deepcopy(demo_table)
# new_doc = Document()
# paragraph = new_doc.add_paragraph()
# paragraph._p.addnext(new_table._element)
#
# new_doc.save("C:/Users/Administrator/Desktop/test.docx")
