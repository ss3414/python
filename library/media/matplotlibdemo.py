# ****************************************************************分割线****************************************************************
# todo matplotlib

import librosa
import matplotlib
import matplotlib.pyplot as plot
import numpy
from scipy.fft import fft

plot.figure(dpi=600)  # 分辨率
matplotlib.rc("font", family="SimHei")  # 显示中文
matplotlib.rcParams["axes.unicode_minus"] = False  # 显示符号

# 时域波形图
def test():
    wav, sr = librosa.load("../untitled/test.wav", sr=22050)
    time = numpy.arange(0, len(wav)) * (1.0 / sr)

    plot.plot(time, wav)
    plot.title("时域波形图")
    plot.xlabel("时长（秒）")
    plot.ylabel("振幅")
    plot.show()

# 频域谱线图
def test2():
    wav, sr = librosa.load("../untitled/test.wav", sr=22050)
    magnitude = numpy.absolute(fft(wav))  # 对fft结果取模，得到幅度magnitude
    frequency = numpy.linspace(0, sr, len(magnitude))  # 频率

    plot.plot(frequency[:40000], magnitude[:40000])  # 限定[:40000]
    plot.title("频域谱线图")
    plot.xlabel("频率（赫兹）")
    plot.ylabel("幅度")
    plot.savefig("C:/Users/Administrator/Desktop/test.jpg", dpi=600)  # 保存图片

# 对数谱图
def test3():
    wav, sr = librosa.load("../untitled/test.wav", sr=22050)
    spectrogram = librosa.amplitude_to_db(librosa.stft(wav))

    librosa.display.specshow(spectrogram, y_axis="log")
    plot.colorbar(format="%+2.0f dB")
    plot.title("对数谱图")
    plot.xlabel("时长（秒）")
    plot.ylabel("频率（赫兹）")
    plot.show()

if __name__ == "__main__":
    # test()
    # test2()
    test3()
