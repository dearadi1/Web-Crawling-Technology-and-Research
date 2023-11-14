from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

# 读取文本数据
with open(r"datas\处理后\分词以及停用词处理后弹幕数据.txt", "r", encoding="utf8") as f:
    documents = f.readlines()

# 创建CountVectorizer对象来将文本转化为文档-词汇矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

doc_term_matrix = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df=doc_term_matrix.transpose()
df.to_csv(r'datas\output\doc_term_matrix.csv', index=True)


# 保存词汇表到文件
with open(r'datas\output\vocabulary.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(vectorizer.get_feature_names_out()))

# 初始化LDA模型，指定不同的训练参数
num_topics = 4  # 修改为你想要的主题数量
num_top_words = 20  # 修改为你想要的主题词数量
random_state = 10000000  # 随机数，以确保每次训练出相同的结果
learning_method = 'batch'  # 可以选择 'batch' 或 'online'
max_iterations = 350  # 修改为你想要的迭代次数

# 修改alpha和beta参数
alpha = 0.3  # 修改为你想要的alpha值  alpha 控制文档-主题分布的稀疏性
"""
alpha值越高，表示文档在每个主题上的概率分布越均匀，即文档更倾向于涉及到多个主题，从而使得主题分布更为稀疏；反之，如果alpha值越低，那么文档在每个主题上的概率分布就越集中，即文档更倾向于集中在某一个或几个主题上，从而导致主题分布更为稠密。
"""
beta = 0.5  # 修改为你想要的beta值  
"""
高贝塔值意味着词稀疏性的影响较小，即我们期望每个主题将包含语料库的大部分词，这些主题将更“一般”，他们的单词概率将更加统一。而低β值则表示希望主题应更具具体性，即它们的单词概率分布会更不均匀，从而在更少的单词上放置更高的概率。
如果以错误的方式理解β值对稀疏性的影响，可能会得到错误的结论。稀疏性是指模型内的参数中，只用很少的几个非零元素或只有很少的几个远大于零的元素。因此，调整β值并不能直接增加或降低模型的整体稀疏性。而且，不当的使用稀疏性可能会带来问题，如增加计算空间的复杂性和计算处理时间。所以在实践中，应根据实际需求和数据集的特性来调整β值。
"""

lda = LatentDirichletAllocation(
    n_components=num_topics,
    random_state=random_state,
    learning_method=learning_method,
    max_iter=max_iterations,
    doc_topic_prior=alpha,
    topic_word_prior=beta
)

# 训练LDA模型
lda.fit(X)

# 输出主题-词汇分布和占比到文件
feature_names = vectorizer.get_feature_names_out()
with open(r'datas\output\topic_word_distribution.txt', 'w', encoding='utf-8') as f:
    for topic_idx, topic in enumerate(lda.components_):
        f.write(f"主题 {topic_idx + 1}:\n")
        top_words_idx = topic.argsort()[-num_top_words:][::-1]
        top_words = [feature_names[i] for i in top_words_idx]
        f.write(' '.join(top_words) + '\n')

        # 计算并输出每个主题词的占比
        word_weights = topic[top_words_idx] / topic.sum()
        for i, word in enumerate(top_words):
            f.write(f"{word}: {word_weights[i]:.4f}\n")

# 输出文档-主题分布到文件
doc_topic_dist = lda.transform(X)
with open(r'datas\output\document_topic_distribution.txt', 'w', encoding='utf-8') as f:
    for i, doc_topic in enumerate(doc_topic_dist):
        f.write(f"文档 {i + 1} 的主题分布：{doc_topic}\n")

from sklearn.metrics.pairwise import cosine_similarity


"""
主题距离的计算
主题距离是衡量两个主题之间相似度的指标，常用的有Jaccard distance、Kullback-Leibler divergence和Hellinger distance；困惑度是衡量模型好坏的常用指标，它越小表示模型越好；语义一致性是衡量文本集合中每个文档主题分布的一致性的指标
"""
# 获取LDA模型中的主题-词汇分布
topic_word_distribution = lda.components_
# 计算主题之间的余弦相似度
topic_similarity = cosine_similarity(topic_word_distribution)
# 输出主题之间的余弦相似度
print("主题之间的余弦相似度矩阵：")
print(topic_similarity)


"""
困惑度的计算
困惑度（Perplexity）是衡量语言模型好坏的常用指标，它表示在给定一个文本序列的情况下，这个语言模型对该序列的预测结果有多好。具体来说，困惑度越小表示模型越能够准确地预测下一个词，从而使得整个文本序列更加连贯和通顺。困惑度的计算方法通常采用交叉熵损失函数，即将真实标签的概率与模型预测的概率之间的差异进行加权平均，并取对数
"""
# 评估困惑度
perplexity = lda.perplexity(X)
print(f"模型困惑度: {perplexity}")
