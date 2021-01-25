import re


"""
已经操作过了
"""
primitive_comments=["../data/test_data/data_1.10-1.22/primitive_comments1.10-1.22",
                    "../data/test_data/data_1.23-2.07/primitive_comments1.23-2.07",
                    "../data/test_data/data_2.10-3.05/primitive_comments2.10-3.05",
                    "../data/test_data/data_3.10-5.30/primitive_comments3.10-5.30"]

comments          =["../data/test_data/data_1.10-1.22/comments1.10-1.22",
                    "../data/test_data/data_1.23-2.07/comments1.23-2.07",
                    "../data/test_data/data_2.10-3.05/comments2.10-3.05",
                    "../data/test_data/data_3.10-5.30/comments3.10-5.30"]

def stopwords_list():
    file_path= "../data/stop_word/StopWords"
    stopwords = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    return stopwords


#数据过滤
def regex_filter(s_line):
    # 剔除英文、数字，以及空格
    special_regex = re.compile(r"[a-zA-Z0-9\s]+")
    # 剔除英文标点符号和特殊符号
    en_regex = re.compile(r"[.…{|}#$%&\'()*+,!-_./:~^;<=>?@★●。]+")
    # 剔除中文标点符号
    zn_regex = re.compile(r"[《》、“”；～？！：（）【】]+")

    s_line = special_regex.sub(r"", s_line)
    s_line = en_regex.sub(r"", s_line)
    s_line = zn_regex.sub(r"", s_line)
    return s_line


"""
测试数据处理过程：primitive_comments(原始评论)——comments(进行数据过滤后的评论)——all_comments(所有评论汇总)
"""
#将primitive_comments进行数据过滤转换为comments
def primitive_comments_to_comments(i):
    f=open(primitive_comments[i],"r",encoding="UTF-8")
    content=f.read().splitlines()
    f.close()
    f=open(comments[i],"w",encoding="UTF-8")
    length=len(content)
    for k in range(length):
        sentence=regex_filter(content[k])
        if((sentence=="")|(sentence==" ")):
            continue
        else:
            if(k==length-1):
                f.write(sentence)
            else:
                f.write(sentence + "\n")
    f.close()


def getAll_comments():
    allComments=open("../data/test_data/all_comments","w",encoding="UTF-8")
    for i in range(4):
        f=open(comments[i],"r",encoding="UTF-8")
        content=f.read().splitlines()
        length=len(content)
        for k in range(length):
            if((k==length-1)&(i==3)):
                allComments.write(content[k])
            else:
                allComments.write(content[k]+"\n")
        f.close()
    allComments.close()


if __name__=="__main__":
    for i in range(1):
        primitive_comments_to_comments(i)
    getAll_comments()