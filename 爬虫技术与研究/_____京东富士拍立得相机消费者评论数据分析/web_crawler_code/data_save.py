import csv

# 创建包含列名的数据列表 datas
datas = [
    [   
        "content",         # 评论内容
        "creationTime",    # 评论时间
        "score",           # 评论分数
        "anonymousFlag",   # 是否匿名
        "plusAvailable",   # Plus会员可用性
        "location",        # 所在地
        "nickname",        # 昵称
        "productColor"     # 型号
    ] 
]

# 打开 CSV 文件以检查文件是否为空
f = open("data.csv", "r", encoding="utf-8")

# 如果文件为空，执行以下操作
if f.read() == "":
    # 打开 CSV 文件以附加（追加）模式，创建 CSV 写入器
    with open("data.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        # 将列名写入 CSV 文件
        for row in datas:
            csv_writer.writerow(row)

# 关闭文件
f.close()

# 定义函数 data_save 用于将数据写入 CSV 文件
def data_save(datas):
    with open("data.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        # 遍历数据列表 datas 并将每行数据写入 CSV 文件
        for row in datas:
            csv_writer.writerow(row)

    print("写入csv完成")  # 打印消息表示写入操作完成
