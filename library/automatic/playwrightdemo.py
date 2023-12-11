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
