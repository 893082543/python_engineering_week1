import asyncio
import time
import httpx

# 这是一个同步请求（会阻塞）
def fetch_sync(url):
    print(f"开始同步请求: {url}")
    # httpx.get 会一直卡在这里等结果
    response = httpx.get(url) 
    print(f"同步请求完成: {url}, 状态码: {response.status_code}")

# 这是一个异步请求（不会阻塞）
async def fetch_async(url):
    print(f"开始异步请求: {url}")
    # async with 是异步的上下文管理器，await 意思是“等待网络返回，但期间交出控制权”
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    print(f"异步请求完成: {url}, 状态码: {response.status_code}")

async def main():
    start_time = time.time()
    
    # 假设我们要请求三个网址
    urls = [
        "https://httpbin.org/delay/2", # 这个网址会故意延迟 2 秒才返回
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2"
    ]
    
    print("--- 测试并发异步请求 ---")
    # asyncio.gather 的意思是：把这几个任务同时丢出去，谁先回来算谁的
    await asyncio.gather(
        fetch_async(urls[0]),
        fetch_async(urls[1]),
        fetch_async(urls[2])
    )
    
    print(f"总耗时: {time.time() - start_time:.2f} 秒") # 你会发现总共只用了大约 2 秒，而不是 6 秒

if __name__ == "__main__":
    # 运行异步函数的入口
    asyncio.run(main())