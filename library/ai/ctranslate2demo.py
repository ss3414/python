# ****************************************************************分割线****************************************************************
# todo ctranslate2

import ctranslate2
import numpy
import pysbd
import sentencepiece
import tqdm

model_path = "C:/m2m100_ct2_418m"  # 快
# model_path = "C:/m2m100_ct2_12b"  # 慢但是更准
translator = ctranslate2.Translator(
    model_path=model_path,
    device="cpu",
    inter_threads=4,
    # intra_threads=int(os.cpu_count() / 2),  # 多线程
    intra_threads=6,  # 多线程
)
processor = sentencepiece.SentencePieceProcessor()
processor.Load(f"{model_path}/sentencepiece.model")

# 分割片段
def segment(lines, language):
    sentences, breaks = [], []
    for line in lines:
        if line == "\n":
            breaks.append("\n")
        else:
            segmenter = pysbd.Segmenter(language=language, clean=True)
            sentence = segmenter.segment(line)
            breaks.extend(list(range(len(sentences), len(sentences) + len(sentence))))
            breaks.append("\n")
            sentences.extend(sentence)
    breaks = breaks[:-1]
    return sentences, breaks

# 合并片段
def combine(translations, breaks):
    output = []
    for i in breaks:
        if i == "\n":
            output.append("\n")
        else:
            output.append(translations[i] + " ")
    text = "".join(output)
    return text

# M2M翻译
def translate(lines, source_language, target_language):
    sentences, breaks = segment(lines, source_language)

    n = round((len(sentences) / 8) + 0.5)
    splits = numpy.array_split(numpy.array(sentences), n)
    splits = [split.tolist() for split in splits]

    translations = []
    for split in tqdm.tqdm(splits):
        source_prefix = f"__{source_language}__"
        target_prefix = [[f"__{target_language}__"]] * len(split)

        tokens = processor.EncodeAsPieces(split)
        tokens = [[source_prefix] + token for token in tokens]

        results = translator.translate_batch(
            source=tokens,  # 分词后输入
            target_prefix=target_prefix,
            max_batch_size=2048,
            batch_type="tokens",
            beam_size=3,
            repetition_penalty=1.2,
            replace_unknowns=True,
            # use_vmap=True,  # fixme 词汇直接映射，不用翻译
        )

        # 合并翻译结果
        translation = [
            " ".join(result.hypotheses[0])
                .replace(" ", "")
                .replace("▁", " ")[7:]
                .strip()
            for result in results
        ]
        translations.extend(translation)
    return combine(translations, breaks)

if __name__ == "__main__":
    article = '''
    文は、「主語・修飾語・述語」の語順で構成される。修飾語は被修飾語の前に位置する。また、名詞の格を示すためには、語順や語尾を変化させるのでなく、文法的な機能を示す機能語（助詞）を後ろに付け加える（膠着させる）。これらのことから、言語類型論上は、語順の点ではSOV型の言語に、形態の点では膠着語に分類される（「文法」の節参照）。
    語彙は、古来の大和言葉（和語）のほか、漢語（字音語）、外来語、および、それらの混ざった混種語に分けられる。字音語（漢字の音読みに由来する語の意、一般に「漢語」と称する）は現代の語彙の一部分を占めている。また、「絵/画（ゑ）」など、もともと音であるが和語と認識されているものもある。さらに近代以降には西洋由来の語を中心とする外来語が増大している（「語種」の節参照）。
    '''
    text = translate(article.splitlines(), "ja", "zh")
    print(text)
