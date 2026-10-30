import pandas as pd  # 导入 pandas 库，并给它起个简称 pd（这是行业惯例，大家都这么写）

# 1. 读取 CSV 文件
# read_csv 的作用是把磁盘上的 csv 文件，变成内存里的 DataFrame（表格）
df = pd.read_csv("drugs.csv")

# 2. 查看数据的前几行
# head() 的作用是不管数据有几千几万行，只显示前 5 行，方便你初步检查数据对不对
print("--- 前 5 行数据 ---")
print(df.head())

# 3. 查看数据的“整体健康状态”
# info() 的作用是告诉你：有多少行、每一列叫什么名字、每一列的数据类型（比如是数字还是文字）、有没有缺失值
print("\n--- 数据结构信息 ---")
df.info()

# 4. 查看数据的“统计概览”
# describe() 的作用是算一下数字列的平均值、最大值、最小值等
print("\n--- 描述性统计 ---")
print(df.describe())

# 5. 查看 Series（单独抽出一列）
# 当你用 df["列名"] 的时候，拿出来的就是一个 Series（一列）
# 比如我们单独把价格这列抽出来算平均价
print("\n--- 平均药价 ---")
avg_price = df["price"].mean() # mean() 就是算平均数
print(f"所有药品的平均价格是: {avg_price} 元")