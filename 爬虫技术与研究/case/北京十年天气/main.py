url = "https://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"""
}

import requests
import pandas as pd


def craw_table(year, month):
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month,
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    # data frame
    df = pd.read_html(data)[0]
    return df


df_list = []
for year in range(2012, 2023):
    for month in range(1, 13):
        print("爬取", year, month)
        df = craw_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_excel("case/北京十年天气/北京近十年天气.xlsx", index=False)
