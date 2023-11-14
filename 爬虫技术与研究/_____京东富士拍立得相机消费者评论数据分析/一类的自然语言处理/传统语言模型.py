import numpy as np
import pandas as pd
import jieba

# 定义情感分析函数
def sentiment_analysis(input_text):
    # 训练文件地址
    neg_file = r'一类的自然语言处理\训练数据\负面情绪词.txt'
    pos_file = r'一类的自然语言处理\训练数据\正面情绪词.txt'
    nodict_file = r'一类的自然语言处理\训练数据\否定词.txt'
    plus_file = r'一类的自然语言处理\训练数据\程度副词.txt'
    # 读取负面情感词典
    negdict = load_dictionary(neg_file)
    # 读取正面情感词典
    posdict = load_dictionary(pos_file)
    # 读取否定词词典
    nodict = load_dictionary(nodict_file)
    # 读取程度副词词典
    plusdict = load_dictionary(plus_file)
    # 进行情感分析
    result = predict_sentiment(input_text, negdict, posdict, nodict, plusdict)
    return result

# 定义加载情感词典的函数
def load_dictionary(file_name):
    dictionary = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary

# 定义情感预测函数
def predict_sentiment(text, negdict, posdict, nodict, plusdict):
    p = 0
    sd = list(jieba.cut(text))
    for i in range(len(sd)):
        if sd[i] in negdict:
            if i > 0 and sd[i - 1] in nodict:
                p = p + 1
            elif i > 0 and sd[i - 1] in plusdict:
                p = p - 2
            else:
                p = p - 1
        elif sd[i] in posdict:
            if i > 0 and sd[i - 1] in nodict:
                p = p - 1
            elif i > 0 and sd[i - 1] in plusdict:
                p = p + 2
            elif i > 0 and sd[i - 1] in negdict:
                p = p - 1
            elif i < len(sd) - 1 and sd[i + 1] in negdict:
                p = p - 1
            else:
                p = p + 1
        elif sd[i] in nodict:
            p = p - 0.5
    return p

# 判断是否是主程序
if __name__ == "__main__":
    # 导入需要判断的文件
    df=pd.read_csv(r"datas\new_file\file_data.csv")
    # 内容列提取出来
    content=df["content"]
    # 创建列表用于储存计算指数
    sentiment_scores = content.apply(sentiment_analysis)
    # 将计算指数赋值给content——type列
    df["content_type"] = sentiment_scores
    # 将数据流羞辱文件中
    df.to_csv(r"datas\new_file\计算后.csv",index=False)
