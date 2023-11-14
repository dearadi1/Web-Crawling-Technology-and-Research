import pandas as pd
data = pd.read_csv('data\data.csv')
print(data.dtypes)
data = data.drop_duplicates(subset=['地址'])
data.to_csv('处理后的CSV文件路径.csv', index=False)
