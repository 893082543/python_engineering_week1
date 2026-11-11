import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件里的环境变量
load_dotenv()

# 2. 实例化客户端，告诉它我们要连 DeepSeek 的服务器
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), # 从环境变量里安全地取密码
    base_url="https://api.deepseek.com"   # 如果是通义千问，这里就填通义的地址
)

def ask_llm(question: str):
    # 3. 发起对话请求
    response = client.chat.completions.create(
        model="deepseek-chat", # 指定模型名字
        messages=[
            # system: 给 AI 设定人设和规矩
            {"role": "system", "content": "你是一个专业的医药知识助手，说话要严谨。"},
            # user: 用户真正输入的问题
            {"role": "user", "content": question}
        ],
        temperature=0.1 # 温度越低，回答越保守严谨（医药场景通常设低一点）
    )
    # 4. 提取并返回回答
    return response.choices[0].message.content

if __name__ == "__main__":
    print("正在向大模型提问...")
    answer = ask_llm("阿莫西林和头孢能一起吃吗？")
    print("\nAI 回答：")
    print(answer)