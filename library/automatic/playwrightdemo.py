# ****************************************************************分割线****************************************************************
# todo playwright

# import asyncio
#
# from playwright.async_api import async_playwright
#
# # 异步启动
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(proxy={"server": "socks5://127.0.0.1:10808"})
#         page = await browser.new_page()
#         await page.goto("https://www.google.co.jp/")
#         print(await page.title())
#         await browser.close()
#
# asyncio.run(main())

# ************************************************************半分割线******************************
# todo 同步启动
# playwright同步仅仅是对异步的包装

# from playwright.sync_api import sync_playwright, Playwright
#
# def run(playwright: Playwright):
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()
#
# with sync_playwright() as playwright:
#     run(playwright)

# ************************************************************半分割线******************************
# todo 生成PDF

# import asyncio
#
# from playwright.async_api import async_playwright
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.emulate_media(media="print")
#         await page.goto("http://playwright.dev")
#         await page.pdf(path="C:/Users/Administrator/Desktop/test.pdf", format="A4")
#         await browser.close()
#
# asyncio.run(main())

# ************************************************************半分割线******************************
# todo 保存cookie

# import json

# from playwright.sync_api import sync_playwright, Playwright

# # 导出cookie
# def dump(playwright: Playwright, site: str):
#     browser = playwright.chromium.launch(
#         headless=False,
#         args=[
#             "--disable-blink-features=AutomationControlled",  # 禁用自动化标记
#             "--disable-infobars",  # 禁用信息栏
#             "--start-maximized",  # 最大化窗口
#         ]
#     )
#     # 设置更真实的浏览器环境
#     context = browser.new_context(
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#         viewport={"width": 1280, "height": 720},
#         locale="zh-CN",
#         timezone_id="Asia/Shanghai",
#     )
#     page = context.new_page()
#     page.goto(site)
#     # 打断点手动登录
#     storage = context.storage_state()
#     # cookies = storage["cookies"]
#     json.dump(storage, open("cookie.json", "w"))

# # 使用cookie
# def load(playwright: Playwright, site: str):
#     browser = playwright.chromium.launch(
#         headless=False,
#         args=[
#             "--disable-blink-features=AutomationControlled",
#             "--disable-infobars",
#             "--start-maximized",
#         ]
#     )
#     context = browser.new_context(
#         storage_state="cookie.json",  # 加载cookie文件
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
#         viewport={"width": 1280, "height": 720},
#         locale="zh-CN",
#         timezone_id="Asia/Shanghai",
#     )
#     page = context.new_page()
#     page.goto(site)
#     page.pause()

# with sync_playwright() as playwright:
#     site = "http://bbs.wuyou.net/forum.php"
#     # dump(playwright, site)
#     load(playwright, site)

# ************************************************************半分割线******************************
# todo 监控请求

from playwright.sync_api import sync_playwright, Playwright

def monitor(playwright: Playwright, site: str):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    def handle_request(request):
        # 只处理fetch请求
        if request.resource_type == "fetch":
            print(f"URL：{request.url}")
            print(f"方法：{request.method}")
            response = request.response()
            print(response.body())

    # 监听所有网络请求
    page.on("requestfinished", lambda request: handle_request(request))
    page.goto(site)
    page.pause()

with sync_playwright() as playwright:
    site = "https://github.com"
    monitor(playwright, site)
