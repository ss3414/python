# ****************************************************************分割线****************************************************************
# todo librosa

import librosa

path = "../untitled/test.wav"
print(librosa.get_duration(filename=path))  # 读取时长
print(librosa.get_samplerate(path))  # 读取采样率
