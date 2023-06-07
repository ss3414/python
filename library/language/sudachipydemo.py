# ****************************************************************分割线****************************************************************
# todo sudachipy

from sudachipy import dictionary
from sudachipy import tokenizer

# tokenizer_obj = dictionary.Dictionary().create()  # sudachidict_core
tokenizer_obj = dictionary.Dictionary(dict="full").create()  # sudachidict_full
mode = tokenizer.Tokenizer.SplitMode.B

# # 3种模式
# mode1 = tokenizer.Tokenizer.SplitMode.A
# result1 = [m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode1)]
# print(result1)  # 国家+公務+員
#
# mode2 = tokenizer.Tokenizer.SplitMode.B
# result2 = [m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode2)]
# print(result2)  # 国家+公務員
#
# mode3 = tokenizer.Tokenizer.SplitMode.C
# result3 = [m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode3)]
# print(result3)  # 国家公務員

# # 词素
# m = tokenizer_obj.tokenize("食べ", mode)[0]
# print(m.surface())
# print(m.dictionary_form())
# print(m.reading_form())
# print(m.part_of_speech())

# # 规范化
# print(tokenizer_obj.tokenize("附属", mode)[0].normalized_form())
# print(tokenizer_obj.tokenize("SUMMER", mode)[0].normalized_form())
# print(tokenizer_obj.tokenize("シュミレーション", mode)[0].normalized_form())
