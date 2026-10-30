import pandas as pd

df = pd.read_csv("drugs.csv")

# 1. 单条件筛选
# 找出所有属于“抗生素”的药
antibiotics = df[df["category"] == "抗生素"]
print("--- 抗生素类药品 ---")
print(antibiotics)

# 2. 多条件筛选（注意：每个条件要用括号括起来，且不能用 and，要用 & 符号）
# 找出属于“抗生素” 且 价格大于 30 的药
expensive_antibiotics = df[(df["category"] == "抗生素") & (df["price"] > 30)]
print("\n--- 昂贵的抗生素 ---")
print(expensive_antibiotics)

# 3. 排序（sort_values）
# 按库存量（stock）从高到低排序（ascending=False 表示降序）
sorted_by_stock = df.sort_values(by="stock", ascending=False)
print("\n--- 按库存降序排列 ---")
print(sorted_by_stock)

# 4. 使用 loc 定位
# 语法：df.loc[行条件, 列名]
# 找出库存为 0 的药，只看它的名字和库存
out_of_stock = df.loc[df["stock"] == 0, ["drug_name", "stock"]]
print("\n--- 断货的药品 ---")
print(out_of_stock)