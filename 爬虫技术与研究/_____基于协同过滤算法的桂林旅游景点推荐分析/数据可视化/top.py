import pandas as pd

# 读取CSV文件
df = pd.read_csv('data\data.csv')

# 根据评论数（"评论数"列）降序排序
df_sorted = df.sort_values(by='评论数', ascending=False)

# 获取前三最受欢迎的景区
top_three = df_sorted.iloc[:3]

# 获取后三最受欢迎的景区
bottom_three = df_sorted.iloc[-3:]

# 输出前三最受欢迎的景区信息
print("前三最受欢迎的景区信息：")
for idx, row in top_three.iterrows():
    print("名称:", row['名称'])
    print("评论数:", row['评论数'])
    print()

# 输出后三最受欢迎的景区信息
print("后三最受欢迎的景区信息：")
for idx, row in bottom_three.iterrows():
    print("名称:", row['名称'])
    print("评论数:", row['评论数'])
    print()

# 如果需要保存到文件，可以使用to_csv方法
# top_three.to_csv('top_three_scenic_spots.csv', index=False)
# bottom_three.to_csv('bottom_three_scenic_spots.csv', index=False)
