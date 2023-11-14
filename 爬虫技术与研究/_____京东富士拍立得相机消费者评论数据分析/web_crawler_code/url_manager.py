# -*- coding: utf-8 -*-

# 创建一个 UrlManager 类用于管理URL
class UrlManager:
    def __init__(self):
        # 初始化两个集合，一个用于存储新的URL，一个用于存储已经处理过的URL
        self.new_urls = set()  # 存储新的URL
        self.old_urls = set()  # 存储已处理的URL

    # 向 new_urls 集合中添加新的URL
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            # 如果URL既不在new_urls中也不在old_urls中，则将其添加到new_urls中
            self.new_urls.add(url)

    # 向 new_urls 集合中添加多个新的URL
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 从 new_urls 集合中获取一个新的URL，并将其移动到 old_urls 集合中
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 检查是否还有新的URL需要处理
    def has_new_url(self):
        return len(self.new_urls) != 0
