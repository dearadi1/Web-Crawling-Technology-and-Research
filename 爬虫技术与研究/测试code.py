url = "https://pic.netbian.com/e/extend/downpic.php"
import requests
from bs4 import BeautifulSoup
params = {"id": 31814, "classid": 54}
r = requests.get(url,params=params)
r.encoding='gbk'
soup=BeautifulSoup(r.text,'html.parser')

with open ('111.jpg','wb') as f:
    f.write(r.contents)
