url='https://life.httpcn.com/xingming.asp'

import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

def get_score(xing,ming):
    data={
        'isbz': 1,
        'xing': xing.encode('gb2312'),
        'ming': ming.encode('gb2312'),
        'sex': 1,
        'data_type': 0,
        'year': 1980,
        'month': 10,
        'day': 2,
        'hour': 10,
        'minute': 7,
        'pid': '北京'.encode('gb2312'),
        'cid': '北京'.encode('gb2312'),
        'wxxy': 0,
        'xishen': '金'.encode('gb2312'),
        'yongshen': '金'.encode('gb2312'),
        'check_agree': 'agree',
        'act': 'submit'
    }

    headers={
        "Content-Type":"""application/x-www-form-urlencoded"""
    }

    r=requests.get(url,data=urlencode(data),headers=headers)
    r.encoding='gb2312'

    soup=BeautifulSoup(r.text,'html.parser')
    divs=soup.find_all('div',class_='chaxun_b')
    bazi,wuge=0,0
    for div in divs:
        if '姓名五格评分' not in div.get_text():
            continue
        fonts=div.find_all('font')
        bazi=fonts[0].get_text().replace('分','')
        wuge=fonts[1].get_text().replace('分','')
    
    return f'{xing}{ming}',bazi,wuge

with open('case\宝宝名字打分爬取\input.txt','r',encoding='gb2312') as fin,\
    open('case\宝宝名字打分爬取\output.txt','w',encoding='gb2312') as fou:
    ming_list=fin.readlines()
    for ming in ming_list:
        fou.write(''.join(get_score('裴',ming))+'\n')

