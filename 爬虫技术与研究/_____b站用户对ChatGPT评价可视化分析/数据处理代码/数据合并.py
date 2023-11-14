import pandas as pd  # 导入pandas库，用于数据处理和分析

cids = [1084294128, 1054910356, 1114382502, 1077434739, 916690256,"自己收集的"]  # 定义一个包含多个cid的列表

data = []  # 初始化一个空列表，用于存储弹幕数据

# 遍历cids列表中的每个cid
for cid in cids:
    # 使用with语句打开对应的弹幕文件，并读取文件内容
    with open(fr"datas\弹幕数据\{cid}弹幕文件.txt", "r", encoding="utf-8") as f:
        # 将读取到的文件内容逐行添加到data列表中
        data.extend(f.readlines())

# 将data列表转换为pandas的Series对象
ser = pd.Series(data)

# 使用str.replace()方法将弹幕数据中的换行符替换为空字符
ser = ser.str.replace("\n", "").str.replace(" ","")

# 将处理后的弹幕数据保存到CSV文件中
ser.to_csv(r"datas\处理后\弹幕数据.txt", index=False, header=False, mode='w', encoding="utf-8-sig")
