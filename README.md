# Python 工程化练习 - 第1周

## 这个项目解决什么问题
把一段处理销售数据的脚本，拆分成可复用、可测试的函数模块。

## 包含哪些文件
- `week1.py`：主逻辑（读取、筛选、计数）
- `test_my_script.py`：pytest 测试用例

## 如何运行
1. 创建并激活环境：`conda create -n ai_agent_week1 python=3.11 && conda activate ai_agent_week1`
2. 安装依赖：`pip install pandas pytest`
3. 运行测试：`pytest -v`

## 本周学到的工程习惯
- 函数拆分与类型标注
- 具体异常捕获 + logging
- pytest 单元测试（正常/边界/异常）
- black + isort 代码格式化
