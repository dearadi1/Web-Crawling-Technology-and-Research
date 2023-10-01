from utils import url_manager
import requests
import re
from bs4 import BeautifulSoup

root_url='http://www.crazyant.net/'

urls=url_manager.UrlManager()
urls.add_new_url(root_url)

fout=open('blog_test/craw_all_pages.txt', 'w')
while urls.has_new_url():
    curr_url=urls.get_url()
    r=requests.get(curr_url,timeout=3)
    if r.status_code != 200:
        print('error,return status_code in not 200',curr_url)
        continue
    
    soup=BeautifulSoup(r.text,'html.parser')
    title=soup.title.string

    fout.write(f'{curr_url}\t{title}\n')
    fout.flush()
    print(f'success:{curr_url},{title},{len(urls.new_urls)}')

    links=soup.find_all('a')
    for link in links:
        href=link.get('href')
        if href is None:
            continue
        pattern=r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern,href):
            urls.add_new_url(href)
fout.close()