import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url='http://www.89wx.cc/54/54325/'
    r=requests.get(root_url)
    r.encoding='gbk'
    soup=BeautifulSoup(r.text,'html.parser')

    data=[]
    for dd in soup.find_all('dd'):
        link=dd.find('a')
        if not link:
            continue
        data.append(('http://www.89wx.cc'+link['href'],link.get_text()))
    
    return data


def get_chapter_content(url):
    r=requests.get(url)
    r.encoding='gbk'
    soup=BeautifulSoup(r.text,'html.parser')
    return soup.find('div',id='content').get_text()

novel_chapters=get_novel_chapters()
total_cnt=len(novel_chapters)
idx=0
for chapter in novel_chapters:
    idx+=1
    print(idx,total_cnt)
    url,title=chapter
    with open(f'case/龙王传说小说爬取/数据/{title}.txt','w',encoding='utf-8') as fout:
        fout.write(get_chapter_content(url))
    