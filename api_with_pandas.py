from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title="医药数据处理服务")

# 定义一个接收查询条件的模型
class CategoryQuery(BaseModel):
    category_name: str

@app.post("/analyze/category")
def analyze_category(query: CategoryQuery):
    try:
        # 1. 读取你第二周生成的 csv 数据
        df = pd.read_csv("drugs.csv")
        
        # 2. 用 Pandas 筛选指定类别的药
        filtered = df[df["category"] == query.category_name]
        
        if filtered.empty:
            # 如果筛选结果为空，返回 404
            raise HTTPException(status_code=404, detail=f"未找到类别为 {query.category_name} 的药品")
        
        # 3. 计算平均价格（用 Pandas 算）
        avg_price = float(filtered["price"].mean())
        total_stock = int(filtered["stock"].sum())
        
        # 4. 返回分析结果
        return {
            "category": query.category_name,
            "count": len(filtered),
            "avg_price": round(avg_price, 2),
            "total_stock": total_stock
        }
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="服务器数据文件丢失")

if __name__ == "__main__":
    import uvicorn
    # 加上这句，以后直接运行 python api_with_pandas.py 就能启动
    uvicorn.run(app, host="127.0.0.1", port=8000)