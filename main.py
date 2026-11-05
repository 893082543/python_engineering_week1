from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# 定义数据模型（安检机规则）
# 这相当于定义一个药品的录入模板
class DrugCreate(BaseModel):
    name: str                      # 必填
    price: float                   # 必填
    category: str = "未分类"       # 选填，如果不传，默认叫"未分类"
    stock: Optional[int] = 0       # 选填，也可以不传，默认0



# 1. 创建一个 FastAPI 的实例，你可以把它当成你的“餐厅”
# 括号里的 title 和 description 是给接口文档看的，就像餐厅门口的招牌
app = FastAPI(title="医药 AI Agent 接口测试", description="这是我的第一个 API 服务")

# 2. 定义一个装饰器，告诉 FastAPI：当别人访问根目录 "/" 时，执行下面的函数
@app.get("/")
def read_root():
    # 返回一个字典，FastAPI 会自动把它转换成 JSON 格式给前端
    return {"message": "欢迎来到医药数据接口中心", "status": "ok"}

# 3. 再加一个健康检查接口
@app.get("/health")
def health_check():
    return {"status": "running", "version": "1.0"}

# 1. 路径参数示例：查单个药品
# {drug_id} 就像占位符，函数里的 drug_id 必须与它同名
@app.get("/drugs/{drug_id}")
def get_drug(drug_id: int):  # 声明为 int，如果用户输入英文字母，FastAPI 会自动报错拦截
    # 模拟从数据库查数据
    return {"drug_id": drug_id, "name": "模拟药品", "price": 25.5}

# 2. 查询参数示例：搜索药品列表
# limit 后面给了默认值 = 10，代表如果不传这个参数，默认只返回 10 条
@app.get("/drugs/")
def search_drugs(keyword: str = "", limit: int = 10):
    # 模拟搜索逻辑
    return {
        "keyword": keyword,
        "limit": limit,
        "result": [{"id": 1, "name": f"包含 {keyword} 的药"}] if keyword else []
    }

# 1. 定义 POST 接口
@app.post("/drugs/create")
def create_drug(drug: DrugCreate): # 这里直接声明 drug 的类型是我们上面定义的模型
    # 走到这里，drug 一定包含了 name 和 price
    # 模拟保存到数据库的逻辑
    return {
        "message": "药品创建成功",
        "received_data": drug,
        "tips": "已自动校验数据格式"
    }