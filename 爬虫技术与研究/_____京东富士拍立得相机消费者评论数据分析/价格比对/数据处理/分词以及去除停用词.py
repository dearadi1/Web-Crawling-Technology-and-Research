import jieba  # 导入jieba分词库
from collections import Counter  # 导入Counter计数器
import pandas as pd
def load_stopwords(file_path):  # 定义加载停用词的函数，参数为停用词文件路径
    with open(file_path, 'r', encoding='utf-8') as f:  # 以只读模式打开文件
        stopwords = [line.strip() for line in f.readlines()]  # 读取文件的每一行，去除空格后存入列表
    return set(stopwords)  # 将列表转换为集合并返回

def remove_stopwords(text, stopwords):  # 定义移除停用词的函数，参数为文本和停用词集合
    words = jieba.cut_for_search(text)  # 使用jieba分词库对文本进行分词
    filtered_words = [word for word in words if word not in stopwords]  # 遍历分词结果，过滤掉停用词
    return filtered_words  # 返回过滤后的分词结果

if __name__ == '__main__':  # 判断是否为主程序
    stopwords = load_stopwords(r"datas\停用词表\哈工大停用词表.txt")  # 调用load_stopwords函数加载停用词
    # with open(r"datas\new_file\计算后.csv", "r", encoding="utf-8") as f:  # 以只读模式打开弹幕数据文件
    #     text_list = f.readlines()  # 读取文件的每一行，存入列表
    df=pd.read_csv(r"datas\new_file\计算后.csv")
    text_list=df["content"]
    data = []  # 定义一个空列表，用于存储处理后的弹幕数据
    for text in text_list:  # 遍历弹幕数据列表
        data.append(' '.join(remove_stopwords(text, stopwords)))  # 调用remove_stopwords函数移除停用词，并将处理后的弹幕数据添加到data列表中
    with open(r"datas\new_file\分词以及停用词处理后评论数据.txt", "w", encoding="utf-8") as fh:  # 以写入模式打开处理后的弹幕数据文件
        fh.write(''.join(data))  # 将处理后的弹幕数据写入文件
