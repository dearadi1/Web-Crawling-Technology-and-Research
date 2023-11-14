import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
data = pd.read_csv(r"datas\new_file\计算后.csv")

# 将字符串时间转换为日期时间类型
data["creationTime"] = pd.to_datetime(data["creationTime"])

# 提取星期几信息（0表示星期一，1表示星期二，以此类推）
data["day_of_week"] = data["creationTime"].dt.dayofweek

# 将星期几映射到具体的周几名称
day_mapping = {0: "周一", 1: "周二", 2: "周三", 3: "周四", 4: "周五", 5: "周六", 6: "周日"}
data["day_of_week"] = data["day_of_week"].map(day_mapping)

# 统计各个时间段评论的数量
time_bins = [0, 6, 12, 18, 24]  # 时间段：0-6点, 6-12点, 12-18点, 18-24点
data["time_period"] = pd.cut(data["creationTime"].dt.hour, bins=time_bins, labels=["凌晨", "上午", "下午", "晚上"])
comment_counts = data.groupby(["day_of_week", "time_period"]).size().unstack()

# 绘制折线图
comment_counts.plot(marker='o', figsize=(10, 6))
plt.title("不同时间段评论的分布")
plt.xlabel("时间段")
plt.ylabel("评论数量")
plt.legend(title="周几")
plt.grid()
plt.savefig(r"datas\image\不同时间段评论的分布.png")
plt.show()
