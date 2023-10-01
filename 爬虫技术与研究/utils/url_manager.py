class UrlManager:
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def add_new_url(self, url):
        if url==None or len(url)==0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, *urls):
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url:
            url=self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls)>0
    
if __name__ == '__main__':
    r=UrlManager()
    print('#'*30)
    print(r.new_urls,r.old_urls)
    r.add_new_url('url1')
    print('#'*30)
    print(r.new_urls,r.old_urls)
    r.add_new_urls('url1','url2','url3')
    print('#'*30)
    print(r.new_urls,r.old_urls)
    print(r.get_url())
    print('#'*30)
    print(r.new_urls,r.old_urls)