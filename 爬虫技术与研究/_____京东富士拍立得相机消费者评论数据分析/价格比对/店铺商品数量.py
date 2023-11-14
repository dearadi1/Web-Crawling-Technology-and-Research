import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV文件
data = pd.read_csv(r'datas\商品价格\富士拍立得相机.csv')

# 使用Pandas的groupby和count函数计算每家店铺的商品数量
store_product_count = data.groupby('商家')['名称'].count()

# 排序，获取商品数量最多的店铺
store_product_count = store_product_count.sort_values(ascending=False)

# 绘制柱状图
plt.figure(figsize=(10, 6))
store_product_count.plot(kind='bar')
plt.title('每家店铺的商品数量')
plt.xlabel('商家')
plt.ylabel('商品数量')

# 保存图表到文件
plt.savefig('datas\image\store_product_count.png')

# 显示图表
plt.show()
