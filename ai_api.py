from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
app = FastAPI(title="医药 AI 服务接口")

# 1. 初始化大模型和流水线（放在全局，避免每次请求都重新建连）
llm = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.1
)

# 定义 Prompt 模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个严谨的医药知识助手。如果不知道，请明确回答不知道。"),
    ("user", "{question}")
])

# 组装流水线s
chain = prompt | llm | StrOutputParser()

# 2. 定义前端传数据的格式
class AskRequest(BaseModel):
    question: str

# 3. 编写异步 API（注意这里用了 async def）
@app.post("/api/ask")
async def ask_ai(request: AskRequest):
    # 用 ainvoke (a 代表 async) 来异步执行流水线，这样不会卡死服务器
    result = await chain.ainvoke({"question": request.question})
    
    return {
        "status": "success",
        "data": {
            "question": request.question,
            "answer": result
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)