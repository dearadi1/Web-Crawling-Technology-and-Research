import requests
from bs4 import BeautifulSoup
import os

urls=['https://pic.netbian.com/4kmeinv/index.html']
for i in range(2,4):
    urls.append(f'https://pic.netbian.com/4kmeinv/index_{i}.html')

img_urls=[]
for url in urls:
    r= requests.get(url)
    r.encoding='gbk'
    soups= BeautifulSoup(r.text,'html.parser')
    soups=soups.find_all('img')
    for soup in soups:
        if '/uploads/' not in soup['src']:
            continue
        img_urls.append(f"https://pic.netbian.com/{soup['src']}")

idx=0
for url in img_urls:
    with open(f"case/美女图片/数据/{os.path.basename(url)}",'wb') as f:
        r_img=requests.get(url)
        f.write(r_img.content)
        idx+=1
        print(idx)
        if idx==5:
            break
        
    