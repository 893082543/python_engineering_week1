import os
from dotenv import load_dotenv
# 导入 LangChain 的核心组件
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. 初始化模型（注意这里用的是 LangChain 包装过的类）
# 由于我们用的是 DeepSeek 兼容的接口，所以还是用 ChatOpenAI
llm = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.1
)

# 2. 定义 Prompt 模板
# 花括号 {} 里的就是将来要被填入的变量
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的医药客服，回答必须极其简洁，不超过50个字。"),
    ("user", "请问 {drug_name} 的主要功效是什么？")
])

# 3. 组装流水线 (LCEL 语法)
# 顺序是：输入字典 -> 填入模板 -> 发给模型 -> 提取纯文本
chain = prompt | llm | StrOutputParser()

# 4. 运行流水线
if __name__ == "__main__":
    print("正在通过 LangChain 调用...")
    # 注意：invoke 接收的是一个字典，键名必须和模板里的变量名一致
    result = chain.invoke({"drug_name": "布洛芬"})
    print("AI 回答：", result)