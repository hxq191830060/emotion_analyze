import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

comments    =["../../data/test_data/data_1.10-1.22/comments1.10-1.22",
              "../../data/test_data/data_1.23-2.07/comments1.23-2.07",
              "../../data/test_data/data_2.10-3.05/comments2.10-3.05",
              "../../data/test_data/data_3.10-5.30/comments3.10-5.30"]

comments_TFIDF=["../../data/test_data/data_1.10-1.22/comments1.10-1.22_TFIDF",
             "../../data/test_data/data_1.23-2.07/comments1.23-2.07_TFIDF",
             "../../data/test_data/data_2.10-3.05/comments2.10-3.05_TFIDF",
             "../../data/test_data/data_3.10-5.30/comments3.10-5.30_TFIDF"]

emotion_caculate_comments    =["../../data/test_data/data_1.10-1.22/emotion_caculate_comments1.10-1.22",
                               "../../data/test_data/data_1.23-2.07/emotion_caculate_comments1.23-2.07",
                               "../../data/test_data/data_2.10-3.05/emotion_caculate_comments2.10-3.05",
                               "../../data/test_data/data_3.10-5.30/emotion_caculate_comments3.10-5.30"]
def get4commentsTFIDF():
    f=open("../../data/test_data/all_commentsTF-IDF")
    content=f.read().splitlines()
    f.close()
    length=len(content)
    count=0
    for i in range(4):
        f=open(comments[i],"r",encoding="UTF-8")
        number=len(f.read().splitlines())
        f.close()
        f=open(comments_TFIDF[i],"w",encoding="UTF-8")
        for k in range(count,count+number):
            f.write(content[k]+"\n")
        count+=number
        f.close()

#从comments中筛选IDF位于MIN到MAX之间的数据，放入emotion_caculate_comments中
def filter_data(MIN,MAX):
    get4commentsTFIDF()
    for i in range(4):
        commentsFile=open(comments[i],"r",encoding="UTF-8")
        comments_IDF_File=open(comments_TFIDF[i],"r",encoding="UTF-8")
        emotion_caculate_comments_File=open(emotion_caculate_comments[i],"w",encoding="UTF-8")
        sentences=commentsFile.read().splitlines()
        IDFs=comments_IDF_File.read().splitlines()
        length=len(sentences)
        for k in range(length):
            if(sentences[k]!=""):
                if((float(IDFs[k])>=MIN)&(float(IDFs[k])<=MAX)):
                    emotion_caculate_comments_File.write(sentences[k])
                    emotion_caculate_comments_File.write("\n")
        commentsFile.close()
        comments_IDF_File.close()
        emotion_caculate_comments_File.close()

def filter_data_and_draw_histogram():
    f = open("../../data/test_data/all_commentsTF-IDF", "r", encoding="UTF-8")
    content = f.read().splitlines()
    f.close()
    list = []
    for number in content:
        list.append(float(number))
    x = np.array(list)
    # n, bins, patches = plt.hist(x, 20, density=1, facecolor='blue', alpha=0.75)  #第二个参数是直方图柱子的数量
    mu = np.mean(x)  # 计算均值
    sigma = np.std(x)  # 计算方差

    num_bins = 200  # 直方图柱子的数量
    n, bins, patches = plt.hist(x, num_bins, density=1, alpha=0.75)
    # 直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
    y = norm.pdf(bins, mu, sigma)  # 拟合一条最佳正态分布曲线y

    plt.grid(True)
    plt.plot(bins, y, 'r--')  # 绘制y的曲线
    plt.xlabel('IDF')  # 绘制x轴
    plt.ylabel('rate')  # 绘制y轴
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('TF-IDF Histogram : $\mu$=' + str(round(mu, 4)) + ' $\sigma=$' + str(round(sigma, 4))+"\n"+"红色曲线为高斯分布曲线，如图所示，TF-IDF的分布不符合正态分布")
    plt.savefig(fname="../../data/test_data/TF-IDF_histogram", figsize=[10, 10])
    plt.show()

    #接下来筛选mu-2sigma到mu+2sigma之间的数据
    MIN=mu-0.5*sigma
    MAX=1
    filter_data(MIN,MAX)

if __name__=="__main__":
    filter_data_and_draw_histogram()