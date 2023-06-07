# ****************************************************************分割线****************************************************************
# todo copy

import copy

list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
list1.append(4)
print("list1:{list1} list2:{list2}".format(list1=list1,list2=list2))
