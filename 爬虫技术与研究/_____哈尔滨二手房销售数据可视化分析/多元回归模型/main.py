import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV文件
data = pd.read_csv(r'数据爬虫程序\lianjia\output\ershoufang.csv')

# 数据预处理和特征工程
# 选择自变量（特征）
X = data[['建筑面积', '房屋户型', '所在楼层', '房屋朝向', '装修情况', '配备电梯']]

# 选择因变量
y = data['总价']

# 将非数值特征进行独热编码
X = pd.get_dummies(X)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建多元回归模型
model = LinearRegression()

# 拟合模型
model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)

# 评估模型性能
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 输出模型性能指标
print(f"均方误差 (MSE): {mse}")
print(f"决定系数 (R-squared): {r2}")

# 可视化结果
plt.scatter(y_test, y_pred)
plt.xlabel("实际值")
plt.ylabel("预测值")
plt.title("多元回归模型预测结果")
plt.savefig(r'多元回归模型\多元回归模型预测结果.png')
plt.show()

# 绘制残差图
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.xlabel("预测值")
plt.ylabel("残差")
plt.title("残差图")
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig(r'多元回归模型\残差图.png')
plt.show()
