import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv(r'datas\商品价格\富士拍立得相机.csv', encoding='utf-8')

# 按商家分组，并累计评论数
store_reviews = df.groupby('商家')['评论'].sum().reset_index()

# 按评论数降序排序
top_5_stores = store_reviews.sort_values(by='评论', ascending=False).head(5)

# 设置中文显示和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(top_5_stores['商家'], top_5_stores['评论'])
plt.xlabel('商家')
plt.ylabel('累计评论数')
plt.title('累计评论最多的前五家店铺')
plt.xticks(rotation=15)  # 旋转x轴标签，以避免重叠
plt.yticks([])  # 隐藏y轴刻度数值
plt.savefig(r'datas\image\pinglunleiji.png')
# 显示图表
plt.show()
