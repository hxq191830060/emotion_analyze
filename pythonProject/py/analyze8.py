import numpy as np
import wordcloud
import matplotlib.pyplot as plt
import collections
from PIL import Image
import matplotlib.font_manager as fm  # 字体管理器

emotion           =["../data/test_data/data_1.10-1.22/emotion1.10-1.22",
                    "../data/test_data/data_1.23-2.07/emotion1.23-2.07",
                    "../data/test_data/data_2.10-3.05/emotion2.10-3.05",
                    "../data/test_data/data_3.10-5.30/emotion3.10-5.30"]
back_ground_picture="../data/picture/picture1.jpg"

words_clound       ="../data/test_data/words_clound.jpg"


#传入字典，存储地址，生成词云并保存
def generate_words_clounds(dict_words,store_filepath):
    #设置词云背景背景
    mask = np.array(Image.open(back_ground_picture))  # 定义词频背景

    #词云设置
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        mask=mask,  # 设置背景图
        max_words=200,  # 最多显示词数
        max_font_size=100  # 字体最大值
    )
    #传入字典，生成词云
    wc.generate_from_frequencies(dict_words)
    # 从背景图建立颜色方案
    image_colors = wordcloud.ImageColorGenerator(mask)
    # 将单词颜色设置为背景图方案
    wc.recolor(color_func=image_colors)
    #将词云以jpg形似保存起来
    wc.to_file(store_filepath)
    #以图像形式显示词云
    plt.imshow(wc)
    #关闭坐标轴
    plt.axis('off')
    #显示图像
    plt.show()


#显示词云
def showWordsClound():
    f=open("../data/test_data/all_words","r",encoding="UTF-8")
    wordss=f.read().splitlines()
    f.close()
    f=open("../data/test_data/all_words_TFIDF","r",encoding="UTF-8")
    IDFss=f.read().splitlines()
    f.close()
    words=[]
    IDFs=[]
    for i in range(200):
        words.append(wordss[i])
        IDFs.append(float(IDFss[i]))
    dict_words_IDFs=dict(zip(words,IDFs))
    generate_words_clounds(dict_words_IDFs,words_clound)



def draw_pie_charts(datalist,labellist):
    labels = labellist[0]
    #字体设置
    distance_number=0.7
    distance_label=1.1
    #饼图半径r
    r=6
    my_font = fm.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
    #解决中文乱码
    plt.rcParams['font.sans-serif'] = 'simHei'
    # 使用自定义颜色
    colors = ['red', 'pink', 'magenta', 'purple', 'orange']
    plt.figure(figsize=(10, 8))
    # 221——2行2列第1个
    plt.subplot(221)
    plt.pie(x=datalist[0],
            labels=labels,
            colors=colors,
            autopct='%.1f%%',  # 数值设置为保留2位小数的百分数
            pctdistance=distance_number,  # 百分数和圆心的距离
            labeldistance=distance_label,  # 标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            center=(4, 4),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
            radius=r,  # 设置饼图的半径(相当于X轴和Y轴的范围)
            counterclock=False,  # False表示顺时针方向
            shadow=True,
            wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'black', 'fontproperties': my_font},  # 标签的属性值
            frame=1)  # 是否显示饼图的圆圈,1为显示
    plt.xticks(())
    plt.yticks(())
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.axis('equal')
    plt.title("第一个时间段情绪饼状图")

    # 222——2行2列第2个
    plt.subplot(222)
    plt.pie(x=datalist[1],
            labels=labels,
            colors=colors,
            autopct='%.1f%%',  # 数值设置为保留2位小数的百分数
            pctdistance=distance_number,  # 百分数和圆心的距离
            labeldistance=distance_label,  # 标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            center=(4, 4),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
            radius=r,  # 设置饼图的半径(相当于X轴和Y轴的范围)
            counterclock=False,  # False表示顺时针方向
            wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'black', 'fontproperties': my_font},  # 标签的属性值
            frame=1)  # 是否显示饼图的圆圈,1为显示
    plt.axis('equal')
    plt.xticks(())
    plt.yticks(())
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.title("第二个时间段情绪饼状图")

    # 223——2行2列第3个
    plt.subplot(223)
    plt.pie(x=datalist[2],
            labels=labels,
            colors=colors,
            autopct='%.1f%%',  # 数值设置为保留2位小数的百分数
            pctdistance=distance_number,  # 百分数和圆心的距离
            labeldistance=distance_label,  # 标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            center=(4, 4),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
            radius=r,  # 设置饼图的半径(相当于X轴和Y轴的范围)
            counterclock=False,  # False表示顺时针方向
            wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'black', 'fontproperties': my_font},  # 标签的属性值
            frame=1)  # 是否显示饼图的圆圈,1为显示
    plt.axis('equal')
    plt.xticks(())
    plt.yticks(())
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.title("第三个时间段情绪饼状图")

    # 224——2行2列第4个
    plt.subplot(224)
    plt.pie(x=datalist[3],
            labels=labels,
            colors=colors,
            autopct='%.1f%%',  # 数值设置为保留2位小数的百分数
            pctdistance=distance_number,  # 百分数和圆心的距离
            labeldistance=distance_label,  # 标签和圆心的距离
            startangle=180,  # 设置饼图的初始角度
            center=(4, 4),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
            radius=r,  # 设置饼图的半径(相当于X轴和Y轴的范围)
            counterclock=False,  # False表示顺时针方向
            wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
            textprops={'fontsize': 12, 'color': 'black', 'fontproperties': my_font},  # 标签的属性值
            frame=1)  # 是否显示饼图的圆圈,1为显示
    plt.axis('equal')
    plt.xticks(())
    plt.yticks(())
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['left'].set_color('none')
    plt.gca().spines['bottom'].set_color('none')
    plt.title("第四个时间段情绪饼状图")

    plt.tight_layout()  # 布局方法
    plt.savefig("../data/test_data/pie_chart.png")
    plt.show()  # 显示饼状图

def pie_chart_analysis():
    f=open("../案例总结","w",encoding="UTF-8")
    f.write("情绪字典有喜好，厌恶，愤怒，悲伤，快乐 五种情绪\n")
    f.write("第一个时间段1月10日到1月22日，是疫情刚刚发生到武汉封城的时间段，从情绪比例可以看出，负面情绪厌恶，愤怒，悲伤是当时民众的主情绪\n"
            "因为疫情刚刚发生，政府还未来得及采取有效防控措施，面对疫情的迅速传播，民众悲观，面对部分武汉人出逃武汉将新冠病毒带向其他省份的行为，十分厌恶与愤怒\n")
    f.write("第二个时间段是1月23号到2月7号，武汉封城，病毒在全国扩散的时间段，从情绪比例可以看出，相比于第一个时间段，厌恶，愤怒等负面情绪比例提高\n")
    f.write("说明了民众对疫情的担忧以及悲观态度\n")
    f.write("第三个时间段是2月10日到3月5日，这是国家开始集中全国力量抗击疫情的阶段，可以看到负面情绪比例显著降低，喜好情绪(鼓舞，自信，希冀等情感)比例明显提高\n")
    f.write("在国家的领导下，全民抗疫热情高涨，对战争疫情充满信心，同时民众对一线医护人员给予了全力的支持和鼓励\n")
    f.write("第四个时间段是3月10日到5月30日，这是疫情控制住，生产生活逐渐回复的阶段，可以看到喜好情绪的比例继续增大\n")
    f.write("这个因为在外国因为疫情而手忙脚乱时，中国却迅速的控制住了疫情，恢复生产生活，全国空前团结，民众的民族自信心空前提高\n")
    f.close()

if __name__=="__main__":
    #将TF—IDF最高的200个词生成词云
    showWordsClound()

    #对四个时期的emotion进行分析，并生成饼状图
    datalist=[]
    emotionlist=[]
    for i in range(4):
        f=open(emotion[i],"r",encoding="UTF-8")
        content=f.read().splitlines()
        c=dict(collections.Counter(content))
        c=sorted(c.items(),key=lambda x:x[0])
        emotions=[]
        numbers=[]
        for key in c:
            emotions.append(key[0])
            numbers.append(key[1])
        del(emotions[len(emotions)-1])
        del(numbers[len(numbers)-1])
        emotionlist.append(emotions)
        datalist.append(numbers)
        f.close()
    draw_pie_charts(datalist,emotionlist)

    #根据饼状图分析民众在疫情各个阶段的情绪变化
    pie_chart_analysis()