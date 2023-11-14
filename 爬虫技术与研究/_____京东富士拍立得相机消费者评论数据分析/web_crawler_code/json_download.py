import requests
from user_agent import get_user_agent  # 导入获取用户代理的库
import time
import random

c = 0  # 计数变量，用于计算请求次数

# 定义函数 json_download，用于下载 JSON 数据
def json_download(pg, id, bz):
    root_url = "https://api.m.jd.com/"  # 根URL，京东API接口
    if bz == "y":
        func = "pc_club_skuProductPageComments"  # 选择不同的功能函数
    elif bz == "n":
        func = "pc_club_productPageComments"

    # 准备请求的参数
    data = {
        "appid": "item-v3",
        "functionId": func,
        "productId": str(id),  # 商品ID，转换为字符串
        "t": str(time.time()),  # 当前时间戳
        "score": "0",
        "sortType": "5",
        "page": str(pg),  # 请求的页数，转换为字符串
        "pageSize": "10"  # 每页评论数
    }

    # 随机获取用户代理信息，模拟浏览器访问
    headers = {"User-Agent": get_user_agent()}

    # 发送GET请求，获取JSON数据
    r = requests.get(url=root_url, params=data, headers=headers)

    if r.status_code == 200:  # 如果请求成功（状态码200）
        data_json = r.json()  # 解析JSON数据
        print("json获取成功")
        
        global c  # 声明使用全局变量 c
        c += 1  # 请求计数加一

        # 下面的注释代码用于控制请求次数，如果需要，可以取消注释
        # if c == 100:
        #     print("已爬取1000条,暂停10min")
        #     time.sleep(60*10)

        return data_json  # 返回获取的JSON数据
    else:
        print("错误码：" + str(r.status_code))  # 如果请求不成功，打印错误码
        quit()  # 退出程序

if __name__ == "__main__":
    print(json_download(0, 100024128574, "n"))  # 调用函数并打印结果
