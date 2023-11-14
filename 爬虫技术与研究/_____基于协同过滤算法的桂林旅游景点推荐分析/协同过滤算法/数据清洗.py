import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'data\data.csv')
# 提取所需的列
selected_columns = df[['Unnamed: 0', '名称', '地址']]
selected_columns = selected_columns.drop_duplicates()
# 将数据以::分隔的格式存入.dat文件
selected_columns.to_csv(r'协同过滤算法\tmp\景区信息.dat', sep=':', index=False, header=False)
