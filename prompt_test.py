import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

def analyze_drug_interaction(drug_a: str, drug_b: str):
    # 用 f-string 拼接包含背景信息的 Prompt
    prompt = f"""
    你是一个严谨的医药安全专家。
    我现在需要同时服用【{drug_a}】和【{drug_b}】。
    
    请严格按照以下 JSON 格式返回结果，不要输出任何额外的废话：
    {{
        "can_take_together": true 或 false,
        "risk_level": "高" 或 "中" 或 "低",
        "reason": "详细说明药理学原因",
        "suggestion": "给用户的建议"
    }}
    
    如果你不知道这两种药是否有冲突，请直接返回 "risk_level": "未知"，不要编造。
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(analyze_drug_interaction("布洛芬", "阿司匹林"))