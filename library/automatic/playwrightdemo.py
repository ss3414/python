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

import json

from playwright.sync_api import sync_playwright, Playwright

# 导出cookie
def dump(playwright: Playwright, site: str):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(site)
    # 打断点手动登录
    storage = context.storage_state()
    # cookies = storage["cookies"]
    json.dump(storage, open("storage.json", "w"))

# 使用cookie
def load(playwright: Playwright, site: str):
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()

    # 加载cookie文件
    context = browser.new_context(storage_state="storage.json")

    # # 加载cookie数据
    # storage_data = {
    #     "cookies": [],
    #     "origins": [],
    # }
    # context = browser.new_context(storage_state=storage_data)
    page = context.new_page()
    page.goto(site)
    page.pause()

with sync_playwright() as playwright:
    site = "http://bbs.wuyou.net/forum.php"
    # dump(playwright, site)
    load(playwright, site)
