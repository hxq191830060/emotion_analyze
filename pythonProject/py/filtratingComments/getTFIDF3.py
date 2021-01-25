from collections import defaultdict
import math
import operator

"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
    classVec - 类别标签向量
"""
import jieba
def stopwords_list():
    file_path= "../../data/stop_word/StopWords"
    stopwords = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    return stopwords

#dataset是一个嵌套列表，里面包含了许多个列表，每个列表是一个句子
def loadDataSet():
    dataset=[]
    stopwords=stopwords_list()

    f=open("../../data/test_data/all_comments","r",encoding="UTF-8")
    all_comments=f.read().splitlines()
    f.close()
    for comment in all_comments:
        words1=jieba.cut(comment)
        words2=[]
        for word in words1:
            if word not in stopwords:
                words2.append(word)
        dataset.append(words2)
    return dataset


"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
"""


def get_words_TFIDF(list_words):
    # 总词频统计
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1

    # 计算每个词的TF值
    word_tf = {}  # 存储没个词的tf值
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
    # 计算每个词的IDF值
    doc_num = len(list_words)
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]

    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select

def get_comments_TFIDF(comments_words_list,dict_words_TFIDF):
    length=len(comments_words_list)
    f=open("../../data/test_data/all_commentsTF-IDF","w",encoding="UTF-8")
    for words_list in comments_words_list:
        number=0.00
        count=0.0
        for word in words_list:
            number=number+float(dict_words_TFIDF[word])
            count+=1.0
        if (int(count)==0):
            f.write("0\n")
        else:
            number = number / count
            f.write(str(number)+"\n")
    f.close()

if __name__ == '__main__':
    comments_words_list = loadDataSet()  # 加载数据
    dict_words_TFIDF = get_words_TFIDF(comments_words_list)  # 所有词的TF-IDF值
    dict_words_TFIDF=dict(dict_words_TFIDF)

    f=open("../../data/test_data/all_words","w",encoding="UTF-8")
    for word in dict_words_TFIDF.keys():
        f.write(word+"\n")
    f.close()
    f=open("../../data/test_data/all_words_TFIDF","w",encoding="UTF-8")
    for IDF in dict_words_TFIDF.values():
        f.write(str(IDF)+"\n")
    f.close()
    get_comments_TFIDF(comments_words_list,dict_words_TFIDF)
