# ****************************************************************分割线****************************************************************
# todo sentencepiece

import sentencepiece

model_path = "C:/m2m100_ct2_12b"
processor = sentencepiece.SentencePieceProcessor()
processor.Load(f"{model_path}/sentencepiece.model")
tokens = processor.EncodeAsPieces("グリーンハイツの前。")
print(tokens)
