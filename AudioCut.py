from pydub import AudioSegment
import os
file_dir="E:/原唱/test"

# 操作函数
def get_wav_make(dataDir):
    sound = AudioSegment.from_wav(dataDir)
    duration = sound.duration_seconds * 1000  # 音频时长（ms）
    begin = 0
    end = int(duration / 2)
    cut_wav = sound[begin:end]  # 以毫秒为单位截取[begin, end]区间的音频
    cut_wav.export(filePath + 'test.wav', format='wav')  # 存储新的wav文件
    print("1")


for root, dirs, files in os.walk(file_dir, topdown=False):
    #print(root)     # 当前目录路径
    #print(dirs)     # 当前目录下所有子目录
    print(files)        # 当前路径下所有非目录子文件
    filePath = file_dir+'/'

    for file in files:
        filename=file_dir+"/"+file
        print(filename)
        sound = AudioSegment.from_wav(filename)
        duration = sound.duration_seconds  # 音频时长（ms）
        cut_number=duration/10   #得出需要多少10秒
        Name = os.path.splitext(file)[0]
        for i in range(int(cut_number-1)):
            begin = 1000*i*10
            end = 1000*(i+1)*10
            cut_wav = sound[begin:end]  # 以毫秒为单位截取[begin, end]区间的音频
            cut_wav.export("testdata/0cuttest/"+Name + '-'+str(i+1)+'.wav', format='wav')  # 存储新的wav文件



'''sound = AudioSegment.from_wav("testdata/一千年以后.wav")
duration = sound.duration_seconds  # 音频时长（s）

cut_number=duration//10   #得出需要多少10秒
filePath = file_dir+'/'

for i in range(int(cut_number)):

    begin = 1000*i
    end = 1000*(i+1)
    cut_wav = sound[begin:end]  # 以毫秒为单位截取[begin, end]区间的音频
    cut_wav.export(filePath +'一千年以后'+ '-'+str(i+1)+'.wav', format='wav')  # 存储新的wav文件'''