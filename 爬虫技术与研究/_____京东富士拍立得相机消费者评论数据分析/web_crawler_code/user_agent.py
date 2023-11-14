import random  # 导入随机模块
from fake_useragent import UserAgent  # 导入 fake_useragent 模块

# 定义一个函数，用于获取随机的用户代理（User-Agent）
def get_user_agent():
    return UserAgent().random  # 调用 UserAgent 类的 random 方法来获取随机的用户代理

# 当作为主程序运行时，打印随机的用户代理
if __name__ == "__main__":
    print(get_user_agent())  # 调用 get_user_agent 函数并打印结果
