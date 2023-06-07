# ****************************************************************分割线****************************************************************
# todo torch

import torch

# 读取pth文件
data = torch.load("C:/Users/Administrator/Desktop/test.pth")
print(data["model"])  # 模型
print(data["iteration"])  # 迭代次数，即epochs
print(data["optimizer"])
print(data["learning_rate"])
print(torch.cuda.device_count())  # 可用GPU
