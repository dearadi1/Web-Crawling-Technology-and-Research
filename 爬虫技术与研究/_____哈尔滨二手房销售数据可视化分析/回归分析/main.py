import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV文件
data = pd.read_csv(r'数据分析程序\output\ershoufang_按需处理后.csv')

# 提取特征和目标变量
X = data[['面积']]
y = data['价格']

# 创建线性回归模型
model = LinearRegression()
model.fit(X, y)

# 预测价格
y_pred = model.predict(X)

# 绘制散点图和回归线
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='面积', y='价格', label='实际价格')
plt.plot(X, y_pred, color='red', label='回归线')
plt.xlabel('面积')
plt.ylabel('价格')
plt.title('房价与面积的回归分析')
plt.legend()

# 保存图表到文件
plt.savefig(r'回归分析\regression_analysis.png')

# 显示图表
plt.show()
