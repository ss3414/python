# ****************************************************************分割线****************************************************************
# todo pyaudio

# import wave

# import pyaudio
# from tqdm import tqdm

# def play(file):
#     chunk = 1024
#     wave_file = wave.open(file, "rb")
#     player = pyaudio.PyAudio()

#     stream = player.open(format=player.get_format_from_width(wave_file.getsampwidth()), channels=wave_file.getnchannels(), rate=wave_file.getframerate(), output=True)
#     data = wave_file.readframes(chunk)

#     datas = []
#     while len(data) > 0:
#         data = wave_file.readframes(chunk)
#         datas.append(data)
#     for i in tqdm(datas):
#         stream.write(i)

#     stream.stop_stream()
#     stream.close()

#     player.terminate()

# play("C:/Users/Administrator/Desktop/test.wav")

# ************************************************************半分割线******************************
# todo 多线程播放

# import threading
# import time
# import wave
#
# import pyaudio
#
# class AudioThread(threading.Thread):
#     def __init__(self, file):
#         super().__init__()
#         self.wave_file = wave.open(file, "rb")
#         self.player = pyaudio.PyAudio()
#         self.stream = self.player.open(format=self.player.get_format_from_width(self.wave_file.getsampwidth()), channels=self.wave_file.getnchannels(), rate=self.wave_file.getframerate(), output=True)
#         self.chunk = 1024
#         self.data = self.wave_file.readframes(self.chunk)
#         self.flag1 = True  # 停止线程的标识
#         self.flag2 = threading.Event()  # 暂停线程的标识
#         self.flag2.set()
#
#     def run(self):
#         while self.flag1 and self.data != "":
#             self.flag2.wait()
#             self.stream.write(self.data)
#             self.data = self.wave_file.readframes(self.chunk)
#
#     # 暂停
#     def pause(self):
#         self.flag2.clear()  # 设置为False，阻塞线程
#
#     # 恢复
#     def resume(self):
#         self.flag2.set()  # 设置为True，停止阻塞
#
#     # 停止
#     def stop(self):
#         self.flag1 = False
#
# if __name__ == "__main__":
#     audio = AudioThread("C:/Users/Administrator/Desktop/test.wav")
#     audio.start()
#     print(audio.is_alive())
#
#     time.sleep(2)
#     audio.pause()
#
#     time.sleep(2)
#     audio.resume()
#
#     time.sleep(2)
#     audio.stop()
#
#     # time.sleep(2)
#     # print(audio.is_alive())

# ************************************************************半分割线******************************
# todo 录制语音

import wave

import pyaudio

def record(file, record_seconds):
    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    chunk = 1024
    player = pyaudio.PyAudio()
    stream = player.open(format=format, channels=channels, rate=rate, frames_per_buffer=chunk, input=True)

    print("recording")
    frames = []
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    player.terminate()
    print("done")

    wave_file = wave.open(file, "wb")
    wave_file.setsampwidth(player.get_sample_size(format))
    wave_file.setnchannels(channels)
    wave_file.setframerate(rate)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()

record("C:/Users/Administrator/Desktop/test.wav", 5)
