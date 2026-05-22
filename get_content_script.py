import asyncio
from xiaohongshu_mcp import get_note_content

async def main():
    # 指定要爬取的URL
    url = "https://www.xiaohongshu.com/explore/69ce87a6000000001e00c8e0?xsec_token=ABoFZVDfmwy9YpnJHtL_snzNIGNsyIvuhK3ea7WDYyxYQ=&xsec_source=pc_cfeed"

    print(f"正在获取URL内容: {url}")
    content = await get_note_content(url)
    print("获取到的内容:")
    print(content)

if __name__ == "__main__":
    asyncio.run(main())