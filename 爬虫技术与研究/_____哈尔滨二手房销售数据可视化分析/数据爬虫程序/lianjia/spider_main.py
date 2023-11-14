from url_manager import UrlManager
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from html_outputer import HtmlOutputer
import time
import random


class SpiderMain:
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        areas = {"nangang": 80, 
                 "daoli": 70,
                 "pingfang":4,
                 "daowain":80,
                 "xiangfang":50,
                 "songbei":60
                 }
        for area, pg_sum in areas.items():
            for num in range(1, pg_sum + 1):
                pg_url = f"{root_url}{area}/pg{str(num)}/"
                html_cont = self.downloader.download(pg_url)
                ershoufang_urls = self.parser.get_erhoufang_urls(html_cont)
                time.sleep(random.randint(0, 1))
                self.urls.add_new_urls(ershoufang_urls)
                with open(
                    r"数据爬虫程序\lianjia\output\new_url.txt", "a", encoding="utf-8"
                ) as f:
                    f.write(f"{ershoufang_urls}\n")
                if num == pg_sum:
                    print(f"{area}所有url添加完成")

        id = 1
        stop = 1
        while self.urls.has_new_url():
            detail_url = self.urls.get_new_url()
            with open(r"数据爬虫程序\lianjia\output\old_url.txt", "a", encoding="utf-8") as f:
                f.write(f"{detail_url}\n")
            detail_html = self.downloader.download(detail_url)
            ershoufang_data = self.parser.get_ershoufang_data(detail_html, id)
            time.sleep(random.randint(0, 1))
            self.outputer.collect_data(ershoufang_data)
            id += 1
            stop += 1
            if stop == 2000:
                stop = 1
                print(f"已经收集{id}条")
                print("2min等待中")
                time.sleep(60*2)


if __name__ == "__main__":
    root_url = "https://hrb.lianjia.com/ershoufang/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
