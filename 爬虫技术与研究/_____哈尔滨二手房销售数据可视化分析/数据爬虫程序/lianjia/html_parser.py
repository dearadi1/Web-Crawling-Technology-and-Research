# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self):
        self.id = 1

    def get_ershoufang_data(self, html_cont, id):
        if html_cont is None:
            print("页面解析(detail):传入页面为空!")
            return

        ershoufang_data = []
        communityName = "null"
        areaName = "null"
        total = "null"
        unitPriceValue = "null"

        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        tag_com = bsObj.find("div", class_="communityName").find("a")
        if tag_com is not None:
            communityName = tag_com.get_text().replace(",","，")
        else:
            print("页面解析(detail):找不到communityName标签!")

        tag_area = (
            bsObj.find("div", class_="areaName").find("span", class_="info").find("a")
        )
        if tag_area is not None:
            areaName = tag_area.get_text().replace(",","，")
        else:
            print("页面解析(detail):找不到areaName标签!")

        tag_total = bsObj.find("span", class_="total")
        if tag_total is not None:
            total = tag_total.get_text().replace(",","，")
        else:
            print("页面解析(detail):找不到total标签!")

        tag_unit = bsObj.find("span", class_="unitPriceValue")
        if tag_unit is not None:
            unitPriceValue = tag_unit.get_text().replace(",","，")
        else:
            print("页面解析(detail):找不到total标签!")

        ershoufang_data.append(id)
        ershoufang_data.append(communityName)
        ershoufang_data.append(areaName)
        ershoufang_data.append(total)
        ershoufang_data.append(unitPriceValue)

        counta = 12
        for a_child in (
            bsObj.find("div", class_="introContent")
            .find("div", class_="base")
            .find("div", class_="content")
            .find_all("li")
        ):
            [s.extract() for s in a_child("span")]
            ershoufang_data.append(a_child.get_text().replace(",","，"))
            counta = counta - 1

        while counta > 0:
            ershoufang_data.append("null")
            counta = counta - 1

        countb = 8
        for b_child in (
            bsObj.find("div", class_="introContent")
            .find("div", class_="transaction")
            .find("div", class_="content")
            .find_all("li")
        ):
            string = (
                b_child.find_all("span")[1]
                .get_text()
                .replace("\n", "")
                .replace(" ", "")
            )
            ershoufang_data.append(string)
            countb = countb - 1

        while countb > 0:
            ershoufang_data.append("null")
            countb = countb - 1

        print("页面解析成功!")
        return ershoufang_data

    def get_erhoufang_urls(self, html_cont):
        if html_cont is None:
            print("页面为空")
            return

        ershoufang_urls = set()
        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        sellListContent = bsObj.find_all("li", class_="clear LOGVIEWDATA LOGCLICKDATA")

        for child in sellListContent:
            ershoufang_urls.add(child.find("a")["href"])

        print(f"{self.id}____pg网页解析完成")
        self.id += 1
        return ershoufang_urls
