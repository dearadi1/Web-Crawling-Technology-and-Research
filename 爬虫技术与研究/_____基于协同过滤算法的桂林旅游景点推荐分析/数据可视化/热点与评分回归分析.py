import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv(r'data\data.csv')

# 清理数据：移除包含空值的行
df = df.dropna(subset=['评分', '热点'])

# 将评分和热点列转换为数值类型
df['评分'] = df['评分'].astype(float)
df['热点'] = df['热点'].astype(float)

# 绘制回归分析图
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.regplot(x='评分', y='热点', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('评分与热点的回归分析')
plt.xlabel('评分')
plt.ylabel('热点')

# 进行回归分析
X = df['评分']
X = sm.add_constant(X)
y = df['热点']
model = sm.OLS(y, X).fit()
intercept, slope = model.params
plt.text(1, 40, f'回归方程: 热点 = {intercept:.2f} + {slope:.2f} * 评分', fontsize=12)

# 保存图像到文件
plt.savefig(r'数据可视化\pic\rating_heatmap_regression.png')

# 显示图像
plt.show()
