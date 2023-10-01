import requests
import json

url = "https://maimai.cn/sdk/web/content/get_list"

headers={
    "User-Agent":"""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47""",
    "Cookie":"""seid=s1696171953447; guid=GxIZBBgbGQQcGgQZHVYHGBsZHx8eExIfG1YdHgQfHhoYBBoEHRsbBU1ObwocGQQdGR8FQ1hLTEt5ChoEGgQaBB0bGwVPR0VYQmkKA0VBSU9tCk9BQ0YKBmZnfmJhAgocGQQdGR8FXkNhSE99T0ZaWmsKAx4cUgoRHhxEQ30KERoEGhsKfmQKWV1FTkRDfQIKGgQfBUtGRkNQRWc=; csrftoken=IbfFDqR6-bnyIo6_M-cYEYQr_iI0c0e8-uf4; AGL_USER_ID=7eb0b10b-10b2-495b-b8dc-6c547f1e87df; _buuid=ec8f90b6-0cfe-417a-87c9-9857261a389a; browser_fingerprint=F46732D4; gdxidpyhxdE=PD3Uunx%5CfDjaLhKthUbGaZ7%2Bh275d%2FotZiLqzGGnM2I%2BAvMVhuHaVOIoIQeTh%5CmfHQhXL1MXORKyGVfdf0q2JRJR8Lhr6fwIYhPgkRcJ7eVlfS%2FlBxhNUDSS1uO3575GDXppYWsJi%5CgRiXBE3nsxMMb6oNyAhZ3UJP2qGPpfcRq1C46a%3A1696172886035; YD00198168557789%3AWM_NI=6Cjw7GnsP6RUpa1Tzwv1jCXOwapsj1DMAfFaAdsO3X93NKPsK5AnKOYYlebHPQB5wAzKhewhTV60D11y89yMNLuTzN0UHUaOdE9wChuuN90OYtoTCBzanwSXZCH8IegleE0%3D; YD00198168557789%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeacd870f2af82a8eb5b918a8fa7d15a929f9a86d867a2b2af9bf272818e858cfb2af0fea7c3b92af69da698b64daeada0d7d15fb4bfffb5f97db6efa6a4db45b5bfc094e93b88938f87c56b83bcbdb0b254fbed82acd37989eb8f8fca459b87a486e144948f8ed6f64bba95a886f664988afad1c73bf3a7f8dafc478e94bbb5f946f48b88b6e445a89bf798c264b7ab82dab3459baca1b5c24ababfa298d2549a9d88d9cc6fa5b4aba6b337e2a3; YD00198168557789%3AWM_TID=GzuufyCMO1pEVFQAQEPEjOnLjtiHVOkw; u=240133185; u.sig=gqDz3FfbrPJ77RVaBYdwGl2HJfU; access_token=1.3e933e6a12068a597d360aa8732880d2; access_token.sig=sJeMt7KzVgbT-u-oVpgQ2ibwqWA; u=240133185; u.sig=gqDz3FfbrPJ77RVaBYdwGl2HJfU; access_token=1.3e933e6a12068a597d360aa8732880d2; access_token.sig=sJeMt7KzVgbT-u-oVpgQ2ibwqWA; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJfMFcwd2JEcmprbUlqcUVLYVVTZzYzbUgiLCJ1IjoiMjQwMTMzMTg1IiwiX2V4cGlyZSI6MTY5NjI1ODUwMjgwMCwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=UUh27Qd3LVVYQEXeN_bLpM0K-Wo""",
    "Referer":"""https://maimai.cn/gossip_list""",
    "X-Csrf-Token":"""IbfFDqR6-bnyIo6_M-cYEYQr_iI0c0e8-uf4"""
}

def craw_page(page_number):
    params = {
        "api": "gossip/v3/square", 
        "u": "240133185", 
        "page": page_number,  
        "before_id": 0
        }
    datas=[]
    resp=requests.get(url, headers=headers,params=params)
    data = json.loads(resp.text)
    for text in data['list']:
        datas.append(text['text'])
    return datas

with open('case/脉脉职言爬取/脉脉结果.txt','w',encoding='utf-8') as f:
    for page in range(1,10+1):
        print('craw page',page)
        datas=craw_page(page)
        f.write('\n'.join(datas)+'\n')
