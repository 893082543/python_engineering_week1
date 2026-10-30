import pandas as pd

# 故意造一个有缺失值的表
dirty_data = pd.DataFrame({
    "name": ["感冒灵", "阿莫西林", "布洛芬"],
    "price": [15.0, None, 18.0],  # 阿莫西林的价格缺失了 (None)
    "stock": [100, 50, None]      # 布洛芬的库存缺失了
})

print("--- 原始脏数据 ---")
print(dirty_data)

# 1. 填充缺失值（fillna）
# 把 price 列的空缺填为 0，把 stock 列的空缺填为 -1（代表未知）
clean_data = dirty_data.copy() # 复制一份，不动原数据
clean_data["price"] = clean_data["price"].fillna(0)
clean_data["stock"] = clean_data["stock"].fillna(-1)

print("\n--- 填充后的数据 ---")
print(clean_data)

# 2. 删除缺失值（dropna）
# 只要这行有任何一个空缺，就把整行删掉
dropped_data = dirty_data.dropna()
print("\n--- 删除了缺失行后的数据 ---")
print(dropped_data)

# 3. 导出数据
# 把清洗好的数据保存成一个新的 csv 文件（index=False 表示不要保存行号 0,1,2...）
clean_data.to_csv("clean_drugs.csv", index=False)
print("\n清洗后的数据已保存为 clean_drugs.csv")