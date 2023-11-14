import re
import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体（例如SimHei）以支持中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取文档主题分布数据
with open(r"datas\output\document_topic_distribution.txt", "r", encoding="utf8") as f:
    data = f.read()

# 使用正则表达式提取每个文档的主题分布
document_topic_regex = r"文档 (\d+) 的主题分布：\[(.*?)\]"
matches = re.findall(document_topic_regex, data)

# 遍历每个文档的主题分布并绘制图像
for match in matches:
    doc_id = int(match[0])
    topic_dist = np.array([float(x) for x in match[1].split()])

    # 创建条形图
    plt.bar(range(len(topic_dist)), topic_dist)
    plt.xlabel("主题")
    plt.ylabel("分布")
    plt.title(f"文档 {doc_id} 的主题分布")

    # 保存图像到文件
    output_file = fr"datas\output\可视化分析_文档主题分布\document_{doc_id}_topic_distribution.png"
    plt.savefig(output_file)
    plt.clf()  # 清空图形以准备下一个文档

    print(f"已保存文档 {doc_id} 的主题分布图到 {output_file}")

# 如果你想显示图形，可以取消下面的注释
# plt.show()
