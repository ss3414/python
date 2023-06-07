# ****************************************************************分割线****************************************************************
# todo 机器翻译汉译英（Helsinki-NLP/opus-mt-zh-en）

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
#
# mode_name = "Helsinki-NLP/opus-mt-zh-en"
# model = AutoModelForSeq2SeqLM.from_pretrained(mode_name)
# tokenizer = AutoTokenizer.from_pretrained(mode_name)
# translation = pipeline("translation_zh_to_en", model=model, tokenizer=tokenizer)
# text = "机器翻译汉语译英语"
# # result = translation(text)
# # print(result)

# ************************************************************半分割线******************************
# todo 日译中（K024/mt5-zh-ja-en-trimmed，基于mt5-base）

# from transformers import T5Tokenizer, MT5ForConditionalGeneration, Text2TextGenerationPipeline
#
# # mode_name = "K024/mt5-zh-ja-en-trimmed"
# mode_name = "C:/K024/mt5-zh-ja-en-trimmed"
# pipe = Text2TextGenerationPipeline(
#     model=MT5ForConditionalGeneration.from_pretrained(mode_name),
#     tokenizer=T5Tokenizer.from_pretrained(mode_name),
#     device=0)  # device默认-1（CPU），大于0为GPU
# text = "文は、「主語・修飾語・述語」の語順で構成される。"
# result = pipe(f"ja2zh: {text}", max_length=100, num_beams=4)
# print(result[0]["generated_text"])

# ************************************************************半分割线******************************
# todo 日译中（larryvrh/mt5-translation-ja_zh，基于mt5-large）

# import re
#
# from transformers import pipeline
#
# pipe = pipeline(model="larryvrh/mt5-translation-ja_zh")
#
# def translate_sentence(sentence):
#     return pipe(f"<-ja2zh-> {sentence}")[0]["translation_text"]
#
# def translate_paragraph(paragraph):
#     sentences = []
#     cursor = 0
#     for i, c in enumerate(paragraph):
#         if c == "。":
#             sentences.append(paragraph[cursor:i + 1])
#             cursor = i + 1
#     if paragraph[-1] != "。":
#         sentences.append(paragraph[cursor:])
#     return "".join(translate_sentence(s) for s in sentences)
#
# def translate_article(article):
#     paragraphs = re.split(r"([\r\n]+)", article)
#     for i, p in enumerate(paragraphs):
#         if len(p.strip()) == 0:
#             continue
#         paragraphs[i] = translate_paragraph(p)
#     return "".join(paragraphs)
#
# article = '''
# 文は、「主語・修飾語・述語」の語順で構成される。修飾語は被修飾語の前に位置する。また、名詞の格を示すためには、語順や語尾を変化させるのでなく、文法的な機能を示す機能語（助詞）を後ろに付け加える（膠着させる）。これらのことから、言語類型論上は、語順の点ではSOV型の言語に、形態の点では膠着語に分類される（「文法」の節参照）。
# 語彙は、古来の大和言葉（和語）のほか、漢語（字音語）、外来語、および、それらの混ざった混種語に分けられる。字音語（漢字の音読みに由来する語の意、一般に「漢語」と称する）は現代の語彙の一部分を占めている。また、「絵/画（ゑ）」など、もともと音であるが和語と認識されているものもある。さらに近代以降には西洋由来の語を中心とする外来語が増大している（「語種」の節参照）。
# '''
#
# print(translate_article(article))

# ************************************************************半分割线******************************
# todo 日译中（facebook/m2m100_418M）

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# mode_name = "facebook/m2m100_418M"
mode_name = "C:/m2m100_418m"
model = M2M100ForConditionalGeneration.from_pretrained(mode_name)
tokenizer = M2M100Tokenizer.from_pretrained(mode_name)

text = "文は、「主語・修飾語・述語」の語順で構成される。"
tokenizer.src_lang = "ja"
print(tokenizer.get_special_tokens_mask())
encoded_text = tokenizer(text, return_tensors="pt")
generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.get_lang_id("zh"))
result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(result[0])
