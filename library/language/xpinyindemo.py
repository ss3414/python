# ****************************************************************分割线****************************************************************
# todo xpinyin

from xpinyin import Pinyin

pinyin = Pinyin()
strs = ["中文", "english", "*"]
sorts = []
for i in strs:
    # letter = pinyin.get_pinyin(i)
    # letter = pinyin.get_initial(i[0])
    letter = pinyin.get_initials(i, "")  # 拼音缩写
    sort = {
        "key": letter,
        "value": i
    }
    sorts.append(sort)
sorts.sort(key=lambda k: (k.get("key", 0)))  # 根据key排序
for i in sorts:
    print(i)
