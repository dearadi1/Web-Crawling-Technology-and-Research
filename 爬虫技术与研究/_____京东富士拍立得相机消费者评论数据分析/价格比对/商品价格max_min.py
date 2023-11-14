import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV文件
data = pd.read_csv(r'datas\商品价格\富士拍立得相机.csv')

# 将价格列中的金额符号"￥"去掉，并将价格列转换为浮点数
data['价格'] = data['价格'].str.replace('￥', '').astype(float)

# 排序商品数据，找出最贵的2个和最便宜的3个
top5_expensive = data.nlargest(5, '价格')
top5_cheap = data.nsmallest(5, '价格')

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制最贵的商品
ax1.barh(top5_expensive['名称'], top5_expensive['价格'], color='red')
ax1.set_xlabel('价格')
ax1.set_title('最贵的2个商品')

# 绘制最便宜的商品
ax2.barh(top5_cheap['名称'], top5_cheap['价格'], color='green')
ax2.set_xlabel('价格')
ax2.set_title('最便宜的3个商品')

# 调整子图之间的间距
plt.tight_layout()

# 保存图表为文件
plt.savefig(r'datas\image\max_min.png')

# 显示图表
# plt.show()
