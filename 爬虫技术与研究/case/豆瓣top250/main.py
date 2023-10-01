import requests
from bs4 import BeautifulSoup
import pandas
from utils.url_manager import UrlManager
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
urls = UrlManager()
datas = []

for i in range(0,250,25):
    urls.add_new_url(f'https://movie.douban.com/top250?start={i}&filter=')

while urls.has_new_url():
    curr_url = urls.get_url()
    r = requests.get(curr_url, timeout=3, headers=headers)
    if r.status_code != 200:
        print("Error,retuen status code is not 200", curr_url)
        continue
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, "html.parser")

    article_items = (
        soup.find("div", class_="article")
        .find("ol", class_="grid_view")
        .find_all("div", class_="item")
    )

    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = (
            info.find("div", class_="hd")
            .find("a")
            .find("span", class_="title")
            .get_text()
        )

        stars = (
            info.find("div", class_="bd").find("div", class_="star").find_all("span")
        )
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append(
            {
                "rank": rank,
                "title": title,
                "rating_star": rating_star.replace("rating", "").replace("-t", ""),
                "rating_num": rating_num,
                "comments": comments.replace("人评价", ""),
            }
        )

datas=sorted(datas, key=lambda x: int(x['rank']))

df = pandas.DataFrame(datas)
df.to_excel('case/豆瓣top250/豆瓣评分TOP250.xlsx')
