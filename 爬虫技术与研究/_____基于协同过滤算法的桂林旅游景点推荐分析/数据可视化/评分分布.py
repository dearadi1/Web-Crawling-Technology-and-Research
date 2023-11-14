import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV文件
df = pd.read_csv(r'data\data.csv')

# 提取评分列数据
ratings = df['评分']

# 移除空值和null值
ratings = ratings.dropna()

# 绘制柱状图
plt.figure(figsize=(8, 6))
plt.hist(ratings, bins=10, edgecolor='k', alpha=0.7)
plt.title('景区评分分布')
plt.xlabel('评分')
plt.ylabel('景区数量')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 保存图像到文件
plt.savefig(r'数据可视化\pic\rating_distribution.png')

# 显示图像（可选）
plt.show()
