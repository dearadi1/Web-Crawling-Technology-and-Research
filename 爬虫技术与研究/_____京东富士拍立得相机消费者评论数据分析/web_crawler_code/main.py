# 导入三个自定义模块，分别用于下载JSON数据、解析JSON数据、和保存数据到CSV文件
from json_download import json_download
from json_analyze import json_analyze
from data_save import data_save

if __name__ == '__main__':
    # 从用户输入获取需要爬取的页数、商品序号和是否筛选商品的标志
    pg = eval(input("需要爬取的页数: "))  # 输入爬取的页数，eval() 将字符串转换为数字
    id = eval(input("商品的序号: "))    # 输入商品的序号，eval() 将字符串转换为数字
    bz = str(input("是否筛选商品(y/n): "))  # 输入是否筛选商品的标志

    # 遍历需要爬取的页数，进行数据下载、解析和保存
    for i in range(1, pg + 1):
        # 调用 json_download 函数，获取JSON数据
        data_json = json_download(i, id, bz)
        
        # 调用 json_analyze 函数，解析JSON数据，返回解析后的数据
        datas = json_analyze(data_json)
        
        # 调用 data_save 函数，将解析后的数据保存到CSV文件
        data_save(datas)
