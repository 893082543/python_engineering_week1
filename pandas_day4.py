import pandas as pd

# 读取两张表
drugs = pd.read_csv("drugs.csv")
sales = pd.read_csv("sales.csv")

# 1. 合并（merge）
# 语法：pd.merge(左表, 右表, on="用来连接的共同列名", how="连接方式")
# how="left" 表示以左表（药品表）为准，把销售记录贴上去
# 这样我们就能看到：卖出去的订单里，具体的药品名字、价格和类别是什么
merged_df = pd.merge(drugs, sales, on="drug_id", how="left")
print("--- 合并后的销售明细 ---")
print(merged_df)

# 2. 纵向拼接（concat）
# 假设我们有两批新药到了，生成了两个临时 DataFrame
new_drugs_batch1 = pd.DataFrame({"drug_id": [106], "drug_name": ["板蓝根"], "category": ["中成药"], "price": [9.9], "stock": [500]})
new_drugs_batch2 = pd.DataFrame({"drug_id": [107], "drug_name": ["罗红霉素"], "category": ["抗生素"], "price": [30.0], "stock": [100]})

# 用 concat 把它们上下叠起来，ignore_index=True 表示重新生成行号（0,1,2...）
all_new_drugs = pd.concat([new_drugs_batch1, new_drugs_batch2], ignore_index=True)
print("\n--- 新到货的药品清单 ---")
print(all_new_drugs)