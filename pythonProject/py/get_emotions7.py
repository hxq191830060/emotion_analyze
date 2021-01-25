import train6
import jieba
import numpy as np
from keras.engine.saving import load_model
from keras.preprocessing import sequence

emotion_caculate_comments    =["../data/test_data/data_1.10-1.22/emotion_caculate_comments1.10-1.22",
                               "../data/test_data/data_1.23-2.07/emotion_caculate_comments1.23-2.07",
                               "../data/test_data/data_2.10-3.05/emotion_caculate_comments2.10-3.05",
                               "../data/test_data/data_3.10-5.30/emotion_caculate_comments3.10-5.30"]

emotion           =["../data/test_data/data_1.10-1.22/emotion1.10-1.22",
                    "../data/test_data/data_1.23-2.07/emotion1.23-2.07",
                    "../data/test_data/data_2.10-3.05/emotion2.10-3.05",
                    "../data/test_data/data_3.10-5.30/emotion3.10-5.30"]

MAX_SENTENCE_LENGTH = 80
print("加载模型")
model = load_model("../model/my_model")
#输入评论，分析评论的情感
def predict(sentence):
    # 加载分词字典
    word2index=train6.getDict()
    xx = np.empty(1, dtype=list)
    # 数据预处理
    words = jieba.cut(sentence)
    seq = []
    for word in words:
        if word in word2index:
            seq.append(word2index[word])
        else:
            seq.append(word2index['UNK'])
    xx[0] = seq
    xx = sequence.pad_sequences(xx, maxlen=MAX_SENTENCE_LENGTH)

    label2word = {1: '喜好', 2: '悲伤', 3: '厌恶', 4: '愤怒', 5: '快乐', 0: '无情绪'}
    for x in model.predict(xx):
        x = x.tolist()
        label = x.index(max(x[0], x[1], x[2], x[3], x[4], x[5]))
    return label2word[label]

def get_emotion(i):
    f=open(emotion_caculate_comments[i],"r",encoding="UTF-8")
    content=f.read().splitlines()
    f.close()
    f=open(emotion[i],"w",encoding="UTF-8")
    length=len(content)
    for i in range(length):
        sentence=content[i]
        if(sentence!=""):
            e=predict(sentence)
            f.write(e+"\n")
    f.close()
if __name__ == '__main__':
    for i in range(4):
        get_emotion(i)