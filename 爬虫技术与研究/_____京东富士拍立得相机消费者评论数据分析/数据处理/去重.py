import pandas as pd  # 导入 pandas 库

# 从指定路径读取 CSV 文件并存储在 DataFrame 对象 df 中
df = pd.read_csv(r"datas\old_file\awit_data.csv")

# 在 DataFrame 中筛选出内容不为"此用户未填写评价内容"的行
df = df.loc[df["content"] != "此用户未填写评价内容"]

# 在 DataFrame 中去除重复的行，以内容（"content" 列）为基准去重
df = df.drop_duplicates(subset=["content"])

# 在 DataFrame 中添加一个名为 "content_type" 的列，所有值初始化为 "null"
df["content_type"] = "null"

# 将处理后的 DataFrame 写入到新的 CSV 文件中，不包含索引列
df.to_csv(r"datas\new_file\file_data.csv", index=False)
