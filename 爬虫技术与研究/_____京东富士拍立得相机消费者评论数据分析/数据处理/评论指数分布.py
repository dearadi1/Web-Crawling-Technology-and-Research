import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv(r"datas\new_file\计算后.csv")

# 绘制分布图
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df, x="content_type")
plt.title("Distribution of Content Type")
plt.xlabel("Content Type")
plt.ylabel("Count")

# 设置X轴刻度标签
xtick_labels = [str(x) for x in ax.get_xticks()]
ax.set_xticklabels(xtick_labels)
ax.set_xticks([0])
ax.set_xticklabels(["0"])

# 保存图像
plt.savefig(r"datas\image\评价指数分布图.png")  # 保存为 PNG 文件

# 显示图像（可选）
# plt.show()
