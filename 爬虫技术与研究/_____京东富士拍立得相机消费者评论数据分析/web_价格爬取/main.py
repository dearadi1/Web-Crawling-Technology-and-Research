import time
import pandas as pd
from selenium import webdriver
import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    search_word = input("请输入你要搜索的商品：")
    page_size = int(input("请输入你要爬取的页数："))
    prices, names, commits, shops = [], [], [], []
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.get("https://www.jd.com")
    time.sleep(1)
    # 将web网页窗口最大化
    driver.maximize_window()
    # 找到搜索框
    input_box = driver.find_element(By.ID, "key")
    # 将搜索的字输入到京东搜索框中
    input_box.send_keys(search_word)
    # 按下enter键
    input_box.send_keys(Keys.ENTER)

    # range(page_size)
    for i in range(page_size):
        # 将下拉框拖到最下面：
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)  # 确保在向下拖动的过程中，数据全部加载出来，加几秒等待

        # 获取所有的li
        good_lists = driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')

        for item in good_lists:
            # 找到产品的价格
            price = item.find_element(By.CLASS_NAME, "p-price").text
            # 找到商品的名字
            name = item.find_element(By.CLASS_NAME, "p-name").text
            # 找到商品的评论
            commit = item.find_element(By.CLASS_NAME, "p-commit").text
            # 找到商品的店铺
            shop = item.find_element(By.CLASS_NAME, "p-shop").text
            # 将每一次爬到的数据信息，追加到列表[ ]中
            prices.append(price)
            names.append(name)
            commits.append(commit)
            shops.append(shop)

        # 点击下一页
        driver.find_element(By.CLASS_NAME, "pn-next").click()

    df = pd.DataFrame({
        "价格": prices,
        "名称": names,
        "评论": commits,
        "商家": shops
    })

    # 将数据保存到excel表格中
    df.to_csv(r"datas\商品价格\{}.csv".format(search_word))