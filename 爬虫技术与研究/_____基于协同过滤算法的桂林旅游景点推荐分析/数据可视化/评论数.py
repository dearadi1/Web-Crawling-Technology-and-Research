import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV文件
df = pd.read_csv(r'data\data.csv')

# 移除缺失值
df = df.dropna(subset=['名称', '评论数'])

# 提取评论数列数据
comment_counts = df['评论数']

# 绘制柱状图
plt.figure(figsize=(12, 6))
plt.bar(df['名称'], comment_counts)
plt.title('景区评论数分布')
plt.xlabel('景区名称')
plt.ylabel('评论数')
plt.xticks([])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 保存图像到文件
plt.savefig(r'数据可视化\pic\comment_counts_distribution.png')

# 显示图像（可选）
plt.show()
