from bs4 import BeautifulSoup

with open('./test.html',encoding='utf-8') as fin:
    heml_doc=fin.read()

soup=BeautifulSoup(heml_doc,'html.parser')

div_node=soup.find('div',id='content')
print(div_node,end='\n'+'#'*30+'\n')

links=div_node.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text(),sep='***')

img=div_node.find('img')
print(img['src'])