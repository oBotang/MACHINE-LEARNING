import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
from pydub import AudioSegment
import pickle
import sklearn


# 操作函数


def extract_S_dB(filename):

    y,sr = librosa.load(filename)
    S = librosa.feature.melspectrogram(y=y,sr=sr)
    #print(S.shape)
    plt.figure(figsize=(10,4))
    S_dB= librosa.power_to_db(S,ref=np.max)
    #print(S_dB.shape)

    #print(S_dB)
    librosa.display.specshow(S_dB,x_axis='time',
                             y_axis='mel',sr=sr,
                             fmax=96000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequencyspectrogram')
    plt.tight_layout()
    plt.show()
    return S_dB
#extract_S_dB('test/背对背拥抱.wav')

def extract_feature(filename):
    x, sr = librosa.load(filename)
    mfccs = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=40)
    norm_mfccs = sklearn.preprocessing.scale(mfccs, axis=1)
    return norm_mfccs
# 测试extract_feature是否正常工作
mfccs = extract_feature('test/背对背拥抱.wav')
print(mfccs.shape)
plt.figure(figsize=(20,5))
librosa.display.specshow(mfccs, sr=22050, x_axis='time',y_axis='mel', cmap='viridis')
plt.colorbar()
plt.show()
print (mfccs.var(axis=1))
print (mfccs.mean(axis=1))





'''y, sr = librosa.load('test/背对背拥抱.wav', sr=16000)
# 提取 mel spectrogram feature
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
logmelspec = librosa.power_to_db(melspec)       # 转换为对数刻度
# 绘制 mel 频谱图
plt.figure()
librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel', cmp="jet")
plt.colorbar(format='%+2.0f dB')        # 右边的色度条
plt.title('Beat wavform')
plt.show()'''
'''

file_dir = "testdata/1cut"
features, labels = np.empty((0, 40, 431)), np.empty(0)
for root, dirs, files in os.walk(file_dir, topdown=False):
    #print(root)     # 当前目录路径
    #print(dirs)     # 当前目录下所有子目录
    print(files)        # 当前路径下所有非目录子文件
    a=0
    for file in files:
        filename=file_dir+"/"+file
        print(filename)
        #get_wav_make(filename)
        mfccs=extract_feature(filename)
        #print(mfccs.shape)
        features = np.append(features, mfccs[None], axis=0)
        a=a+1
        print(str(a)+'/24897')
        labels = np.append(labels,1)

file_dir = "testdata/0cut"

for root, dirs, files in os.walk(file_dir, topdown=False):
    # print(root)     # 当前目录路径
    # print(dirs)     # 当前目录下所有子目录
    print(files)  # 当前路径下所有非目录子文件
    a=0
    for file in files:
        filename = file_dir + "/" + file
        print(filename)
        # get_wav_make(filename)
        mfccs=extract_feature(filename)
        # print(S_dB.shape)
        a=a+1
        print(str(a)+'/15251')
        features = np.append(features, mfccs[None], axis=0)
        labels = np.append(labels, 0)

print(features.shape)
train_xm =np.array(features)
train_ym =np.array(labels, dtype=np.int)

print(train_xm.shape)
print(labels)



pickle.dump(train_xm, open('./train_x1.dat', 'wb'),protocol = 4)
pickle.dump(train_ym, open('./train_y1.dat', 'wb'),protocol = 4)
'''





