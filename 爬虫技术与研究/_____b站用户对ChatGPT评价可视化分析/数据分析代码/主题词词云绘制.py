from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取主题词数据
with open(r"datas\output\topic_word_distribution.txt", "r", encoding="utf8") as f:
    data = f.read()

# 使用正则表达式提取每个主题的主题词
topic_regex = r"主题 (\d+):\s*([\s\S]*?)(?=主题 \d+|\Z)"
matches = re.finditer(topic_regex, data)

# 遍历每个主题的主题词并生成词云图
for match in matches:
    topic_id = match.group(1)
    topic_words = match.group(2).strip().split('\n')
    topic_words_dict = {}

    for i in range(len(topic_words)):
        line = topic_words[i].strip()
        if ':' in line:
            word, weight = line.split(': ')
            topic_words_dict[word] = int(float(weight) * 1000)  # 乘以1000以增加词云中的显示频率

    # 创建词云对象
    wordcloud = WordCloud(
        font_path="C:\\Windows\\Fonts\\msyh.ttc",  # 指定字体文件路径，根据你的系统进行调整
        background_color='white',
        width=800,
        height=600
    )

    # 生成词云图
    wordcloud.generate_from_frequencies(topic_words_dict)

    # 绘制词云图
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(f"主题 {topic_id} 的主题词云")
    plt.axis("off")  # 隐藏坐标轴

    # 保存词云图到文件
    output_file = rf"datas\output\可视化分析_词云分布\topic_{topic_id}_wordcloud.png"
    wordcloud.to_file(output_file)
    print(f"已保存主题 {topic_id} 的主题词云图到 {output_file}")

plt.show()  # 显示所有词云图
