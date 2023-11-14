import re
import matplotlib.pyplot as plt

# 读取主题词分布数据
with open(r"datas\output\topic_word_distribution.txt", "r", encoding="utf8") as f:
    data = f.read()

# 使用正则表达式提取每个主题的词汇分布
topic_data = re.split(r'主题 \d+:', data)[1:]

# 设置中文字体以支持中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 遍历每个主题的数据并绘制图像
for i, topic_text in enumerate(topic_data):
    lines = topic_text.strip().split('\n')
    topic_title = lines[0].strip()
    words = {}
    word_weights = {}
    for line in lines[1:]:
        if ':' in line:
            word, weight = line.split(':')
            words[word.strip()] = float(weight.strip())
            word_weights[word.strip()] = float(weight.strip())

    # 创建主题词可视化图表
    plt.figure(figsize=(10, 6))
    plt.bar(words.keys(), words.values(), color='skyblue')
    plt.title(f"{topic_title}")
    plt.xlabel("主题词")
    plt.ylabel("权重")

    # 调整图表布局以避免重叠
    plt.tight_layout()

    # 保存图像到文件
    output_file = fr"datas\output\可视化分析_主题词分布\topic_{i + 1}_word_distribution.png"
    plt.savefig(output_file)

    print(f"已保存主题 {i + 1} 的词汇分布图到 {output_file}")
    plt.clf()  # 清空图形以准备下一个主题

# 显示图表（如果需要）
# plt.show()
