import os
import codecs
import math
import operator

# 1. 获取用户点击数据
def get_user_click(rating_file):
    fp = open(rating_file, encoding="utf-8")
    user_click = {}
    for line in fp:
        items = line.strip().split("::")
        uid = items[0]
        mid = items[1]
        rating = items[2]
        if float(rating) < 3.0:
            continue
        if uid not in user_click:
            user_click[uid] = []
        user_click[uid].append(mid)
    return user_click

user_click = get_user_click(r"协同过滤算法\tmp\景区用户.dat")

# 2. 获取景区信息
def get_item_info(item_file):
    fp = codecs.open(item_file, 'r', encoding="utf-8")
    item_info = {}
    for line in fp:
        items = line.strip().split("::")
        if items[0] not in item_info:
            item_info[items[0]] = [items[1], items[2]]
    return item_info

item_info = get_item_info(r"协同过滤算法\tmp\景区信息.dat")

# 3. 计算景区相似度
def base_contribute_score():
    return 1

co_appear = {}
item_user_click_times = {}

for user, itemlist in user_click.items():
    for index_i in range(0, len(itemlist)):
        itemid_i = itemlist[index_i]
        item_user_click_times.setdefault(itemid_i, 0)
        item_user_click_times[itemid_i] += 1
        for index_j in range(index_i + 1, len(itemlist)):
            itemid_j = itemlist[index_j]
            co_appear.setdefault(itemid_i, {})
            co_appear.setdefault(itemid_j, {})
            co_appear[itemid_i].setdefault(itemid_j, 0)
            co_appear[itemid_j].setdefault(itemid_i, 0)
            co_appear[itemid_i][itemid_j] += base_contribute_score()
            co_appear[itemid_j][itemid_i] += base_contribute_score()

item_sim_score = {}

for itemid_i, relate_item in co_appear.items():
    for itemid_j, co_time in relate_item.items():
        item_sim_score.setdefault(itemid_i, {})
        item_sim_score[itemid_i].setdefault(itemid_j, 0)
        item_sim_score[itemid_i][itemid_j] = co_time / math.sqrt(item_user_click_times[itemid_j] * item_user_click_times[itemid_i])

# 4. 获取与输入景区相似度最高的5个景区
def get_top_similar_items(input_item_id, item_sim_score, top_n=5):
    if input_item_id not in item_sim_score:
        return []
    
    similar_items = item_sim_score[input_item_id]
    sorted_items = sorted(similar_items.items(), key=operator.itemgetter(1), reverse=True)
    top_items = sorted_items[:top_n]
    
    top_item_ids = [item[0] for item in top_items]
    return top_item_ids

# 输入一个景区，例如 '1'，获取与其相似度最高的5个景区
input_item = '3'
top_similar_items = get_top_similar_items(input_item, item_sim_score)

# 打印结果
print(f"景区 '{input_item}' 的相似景区：")
for item_id in top_similar_items:
    print(f"{item_info[item_id][0]} - {item_info[item_id][1]}")

