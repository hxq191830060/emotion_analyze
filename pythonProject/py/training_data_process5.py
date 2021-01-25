import collections
import jieba

training_comment="../../data/training_data/training_comments"

def stopwords_list():
    file_path= "../data/stop_word/StopWords"
    stopwords = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    return stopwords

#处理训练评论，将其分词，转换为字典
def processTrainingComments(filepath):
    word_freqs = collections.Counter()  # 词频
    max_len = 0
    stopwordlist =stopwords_list()
    f=open(filepath,"r",encoding="UTF-8")
    lines=f.read().splitlines()
    for line in lines:
        index=line.index(" ")
        sentence=line[0:index]
        number=int(line[index+1])
        words=jieba.cut(sentence)
        x=0
        for word in words:
            if(word not in stopwordlist):
                word_freqs[word]+=1
                x+=1
        max_len=max(max_len,x)
    f.close()
    print(max_len)
    print('nb_words ', len(word_freqs))

    ## 准备数据
    MAX_FEATURES = 40000  # 最大词频数
    vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
    # 构建词频字典
    word2index = {x[0]: i + 2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
    word2index["PAD"] = 0
    word2index["UNK"] = 1
    # 将词频字典写入文件中保存
    with open("../data/training_data/word_dict_key", "w", encoding="UTF-8") as f:
        for key in word2index.keys():
            f.write(key + "\n")
    with open("../data/training_data/word_dict.value", "w", encoding="UTF-8") as f:
        for value in word2index.values():
            f.write(str(value) + "\n")

if __name__=="__main__":
    processTrainingComments(training_comment)