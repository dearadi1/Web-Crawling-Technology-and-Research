import requests
import time
import random
from bs4 import BeautifulSoup
from url_manager import UrlManager
import csv
from user_agent import get_user_agent

with open(r"data\data.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["名称", "评分", "地址", "评论精选", "评论数", "热点"])
urls = UrlManager()
# 创建目录
# 经过网站实际查找，桂林地区的景点页数总计有84页
for i in range(1, 84):
    urls.add_new_url(f"https://you.ctrip.com/sight/guilin28/s0-p{i}.html")

# ----------------------------------------------------------------
# with open("data.csv", "w",encoding="utf-8",newline="") as f:
#         w = csv.writer(f)
#         for r in ["名字","地址","评分","评论数"]:
#             w.writerow(r)
# ----------------------------------------------------------------
# 获取详情页url

def get_url(urls):
    headers = {"User-Agent": get_user_agent()}
    url_list = []
    idx=1
    while urls.has_new_url():
        url = urls.get_new_url()
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")
            div_node = soup.find_all("div", class_="list_mod2")
            for div in div_node:
                url_list.append(div.find("a")["href"])
            time.sleep(random.randint(0, 1))
        else:
            print("网络连接错误")
        print(idx)
        idx+=1
    urls.add_new_urls(url_list)
    print("所有url导入成功")


get_url(urls)
with open(r"data\urls_new.txt", "w") as f1, open(r"data\urls_old.txt", "w") as f2:
    f1.write(str(urls.new_urls))
    f2.write(str(urls.old_urls))

count=0
# 解析详情页面信息，并写入csv
def get_datas(urls):
    headers = {"User-Agent": get_user_agent()}
    url = urls.get_new_url()
    
    r = requests.get(url, headers=headers)
    if r.text=="" or r.text==[]:
        print("返回为空")
    soup = BeautifulSoup(r.text, "html.parser")
    datas = []
    
    # title
    try:
        datas.append(
            soup.find("div", class_="titleView")
            .find("div", class_="title")
            .get_text()
            .strip()
            .replace(",", "，")
        )
    except:
        datas.append("null")
    # score
    try:
        datas.append(
            soup.find("div", class_="comment")
            .find("div", class_="commentScore")
            .get_text()
            .rstrip("/5分")
            .replace(",", "，")
        )
    except:
        datas.append("null")
    # address
    try:
        datas.append(
            soup.find("div", class_="baseInfoContent")
            .find("div", class_="baseInfoItem")
            .get_text()
            .lstrip("地址")
            .replace(",", "，")
        )
    except:
        datas.append("null")
    # # application
    # datas.append(
    #     soup.find("div", class_="LimitHeightText")
    #     .find("p")
    #     .get_text()
    #     .strip()
    #     .replace(",", "，")
    # )
    # comment
    try:
        commentList = soup.find_all("div", class_="commentList")
        idx = 1
        clist = []
        for i in commentList:
            clist.append(
                str(idx)
                + "、"
                + i.find("div", class_="commentDetail")
                .get_text()
                .strip()
                .replace("\n", "")
                .replace(",", "，")
            )
            idx += 1
        datas.append(str(clist).lstrip("[").rstrip("]").replace(",", "，"))
    except:
        datas.append("null")
    # comment_num
    try:
        datas.append(
            soup.find("div", class_="comment")
            .find("p", class_="commentCount")
            .find("span", class_="hover-underline")
            .get_text()
            .rstrip("条点评")
        )
    except:
        datas.append("null")
    # redian
    try:
        datas.append(
            soup.find("div", class_="titleView")
            .find("div", class_="heatScoreView")
            .get_text()
            .strip()
            .replace("\n", "")
            .replace(",", "，")
        )
    except:
        datas.append("null")
    print(datas)
    
    with open(r"data\data.csv", "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(datas)
        print("写入成功")
    time.sleep(random.randint(0, 1))
    count+=1
    if count==100:
        count=1
        time.sleep(random.randint(60*2))

while urls.has_new_url():
    get_datas(urls)
