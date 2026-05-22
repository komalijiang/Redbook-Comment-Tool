import asyncio
from xiaohongshu_mcp import login, search_notes

async def main():
    # 登录小红书
    print("正在登录小红书...")
    login_result = await login()
    print(f"登录结果: {login_result}")

    # 搜索2026春假旅游攻略
    keywords = "2026春假旅游攻略"
    print(f"正在搜索关键词: {keywords}")
    search_result = await search_notes(keywords, limit=5)
    print(f"搜索结果: {search_result}")

if __name__ == "__main__":
    asyncio.run(main())