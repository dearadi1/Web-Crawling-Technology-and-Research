import requests
import json
from bs4 import BeautifulSoup

url = "https://www.cnblogs.com/AggSite/AggSitePostList"


def craw_page(page_index):
    data = {
        "CategoryType": "SiteHome",
        "ParentCategoryId": 0,
        "CategoryId": 808,
        "PageIndex": page_index,
        "TotalPostCount": 4000,
        "ItemListActionName": "AggSitePostList",
    }

    headers = {
        "Content-Type": """application/json; charset=UTF-8""",
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47""",
    }

    r = requests.post(url, json.dumps(data), headers=headers)
    return r.text


def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    datas = []
    articles = soup.find_all("article", class_="post-item")
    for article in articles:
        link = article.find("a", class_="post-item-title")
        title = link.get_text()
        href = link["href"]
        author = article.find("a", class_="post-item-author").get_text()
        icon_digg = 0
        icon_comment = 0
        icon_views = 0
        for icon in article.find_all("a"):
            if "icon_digg" in str(icon):
                icon_digg = icon.find("span").get_text()
            if "icon_comment" in str(icon):
                icon_comment = icon.find("span").get_text()
            if "icon_views" in str(icon):
                icon_views = icon.find("span").get_text()
        datas.append([title, href, author, icon_digg, icon_comment, icon_views])
    return datas


all_datas = []
for page in range(1, 200 + 1):
    print(f"正在爬取:{page}页")
    html = craw_page(page)
    datas = parse_data(html)
    all_datas.extend(datas)

import pandas as pd

df = pd.DataFrame(all_datas, columns=["标题", "网址", "作者", "点赞数", "评论数", "浏览数"])
df.to_excel("case\博客园爬取\博客园前两百页文章信息.xlsx", index=False)
