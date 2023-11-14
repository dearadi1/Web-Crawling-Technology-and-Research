# 导入需要使用的模块
import requests                         # http请求
from fake_useragent import UserAgent    # 随机代理
import re                               # 正则表达式
import pandas as pd                     # 数据处理
import time                             # 内置库
import random                           # 随机

# 定义获取弹幕数据的函数，参数为cid
def get_data(cid):
    url=fr"https://comment.bilibili.com/{cid}.xml" #B站弹幕数据存放在https://comment.bilibili.com/cid.xml中，其中cid是视频的cid号
    headers={
        "User-Agent":str(UserAgent().random) # 随机生成User-Agent，模拟浏览器访问
    }
    r=requests.get(url,headers=headers) # 发送GET请求，获取网页内容
    if r.status_code!=200: # 判断请求是否成功
        print(f"连接错误：{r.status_code}") # 输出错误信息
        return None # 返回None，表示请求失败
    r.encoding="utf-8" # 设置响应编码为utf-8
    return r # 返回响应对象

# 定义解析弹幕数据的函数，参数为response
def html_parse(response):
    if response==False: # 判断响应是否为空
        print("No response") # 输出提示信息
        return None # 返回None，表示解析失败
    pattern = re.compile(r'<d p=".*?">(.*?)</d>') # 定义正则表达式，匹配弹幕数据
    danmuku = re.findall(pattern,response.text) # 使用正则表达式提取弹幕数据
    return danmuku # 返回弹幕数据列表

# 定义保存弹幕数据到文件的函数，参数为danmuku和cid
def save_data(danmuku,cid):
    Dict = {
        'danmuku' : danmuku # 将弹幕数据存入字典
    }
    pd_data = pd.DataFrame(Dict) # 将字典转换为DataFrame对象
    cid = str(cid) # 将cid转换为字符串类型
    name = cid + '弹幕文件.txt' # 拼接文件名
    path = f'datas\弹幕数据\{name}' # 拼接文件路径
    print(f"{cid}一爬取完成，一共{len(pd_data)}条") # 输出提示信息
    pd_data.to_csv(path,index = False,header=False,mode='w',encoding='utf-8-sig') # 将弹幕数据保存到文件

if __name__ == "__main__":
    cids=[1084294128,1054910356,1114382502,1077434739,916690256] # 定义需要爬取的cid列表
    # 爬取的视频是b站chgt gpt分区弹幕最多的5个视频
    # av号分别是BV1VL411U7MU、BV1MY4y1R7EN、BV1Ws4y1R7p7、BV1Nm4y1z7AT、BV1qD4y1h7io
    for cid in cids: # 遍历cid列表
        response=get_data(cid) # 调用get_data函数获取弹幕数据
        danmuku=html_parse(response) # 调用html_parse函数解析弹幕数据
        save_data(danmuku,cid) # 调用save_data函数保存弹幕数据到文件
        time.sleep(random.randint(2,5)) # 随机等待2到5秒，模拟人类浏览行为
