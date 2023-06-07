# ****************************************************************分割线****************************************************************
# todo jieba

import jieba.posseg

test = "我到河北省来"

# segs = jieba.cut(test)  # 默认精确模式
# print("/".join(segs))

# segs = jieba.cut(test, cut_all=True)  # 全模式
# print("/".join(segs))

data = {
    "a": "形容词",
    "ad": "副形词",
    "ag": "形容词性语素",
    "an": "名形词",
    "b": "区别词",
    "c": "连词",
    "d": "副词",
    "df": "df",
    "dg": "副语素",
    "e": "叹词",
    "f": "方位词",
    "g": "语素",
    "h": "前接成分",
    "i": "成语",
    "j": "简称略语",
    "k": "后接成分",
    "l": "习用语",
    "m": "数词",
    "mg": "mg",
    "mq": "数量词",
    "n": "名词",
    "ng": "名词性语素",
    "nr": "人名",
    "nrfg": "nrfg",
    "nrt": "nrt",
    "ns": "地名",
    "nt": "机构团体",
    "nz": "其他专名",
    "o": "拟声词",
    "p": "介词",
    "q": "量词",
    "r": "代词",
    "rg": "代词性语素",
    "rr": "人称代词",
    "rz": "指示代词",
    "s": "处所词",
    "t": "时间词",
    "tg": "时语素",
    "u": "助词",
    "ud": "结构助词（得）",
    "ug": "时态助词",
    "uj": "结构助词（的）",
    "ul": "时态助词（了）",
    "uv": "结构助词（地）",
    "uz": "时态助词（着）",
    "v": "动词",
    "vd": "副动词",
    "vg": "动词性语素",
    "vi": "不及物动词",
    "vn": "名动词",
    "vq": "vq",
    "x": "非语素字",
    "y": "语气词",
    "z": "状态词",
    "zg": "zg"
}
segs = jieba.posseg.cut(test)  # 词性
for seg in segs:
    flag = seg.flag
    print(f"{seg.word}:{data[flag]}")

# ************************************************************半分割线******************************
# todo 统计词频

# from collections import Counter
#
# import jieba
#
# with open("C:/Users/Administrator/IdeaProjects(2)/document/program/project.txt", "r", encoding="UTF-8") as f:
#     content = f.read()
# segs = jieba.cut(content)
# counter = Counter()
# for seg in segs:
#     if len(seg) > 1 and seg != "\r\n":
#         counter[seg] += 1
# for (k, v) in counter.most_common(100):
#     print("{k}:{v}".format(k=k, v=v))
