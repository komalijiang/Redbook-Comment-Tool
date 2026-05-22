import asyncio
from xiaohongshu_mcp import login

async def main():
    # 登录小红书
    print("正在登录小红书...")
    login_result = await login()
    print(f"登录结果: {login_result}")

if __name__ == "__main__":
    asyncio.run(main())