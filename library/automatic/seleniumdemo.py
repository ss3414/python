# ****************************************************************分割线****************************************************************
# todo selenium

# 准备工作
# ①Windows Firefox
# geckodriver解压放到Firefox根目录下
# 将Firefox目录（C:\Program Files\RunningCheeseFirefox\Firefox）添加进环境变量中
# ②Windows Chrome
# chromedriver.exe需要放在chrome.exe同级目录下
# Chrome加入环境变量后需要重启PyCharm
# selenium调用Chrome时不能存在已打开的Chrome
# ③Linux Firefox
# 安装：apt-get install firefox
# geckodriver解压放到/usr/local/bin/目录下：
# mv ./geckodriver /usr/local/bin/
# chmod +x /usr/local/bin/geckodriver

# ****************************************************************分割线****************************************************************
# todo 基本用法

# from selenium import webdriver
#
# browser = webdriver.Firefox()
# try:
#     browser.get("http://bbs.wuyou.net")
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# ****************************************************************分割线****************************************************************
# todo 查找节点

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Firefox()
# browser.get("http://bbs.wuyou.net")
# browser.find_element_by_xpath("")
# browser.find_elements_by_css_selector("")
# browser.find_element(By.XPATH, "")
# browser.find_element(By.CSS_SELECTOR, "")

# ****************************************************************分割线****************************************************************
# todo 获取节点信息

# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get("http://bbs.wuyou.net")
# nameInput = browser.find_elements_by_css_selector("#ls_username")
# print("id:" + nameInput.get_attribute("id"))
# print("text:" + nameInput.text)

# ****************************************************************分割线****************************************************************
# todo 运行JS

# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get("http://bbs.wuyou.net")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# browser.execute_script("alert('JS滚动到底部')")
# browser.execute_script("window.print();")

# ****************************************************************分割线****************************************************************
# todo 延时等待

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# browser = webdriver.Firefox()
# browser.get("http://bbs.wuyou.net")
# # 显式等待
# # ①EC.element_to_be_clickable可点击的节点
# # ②超时报错（TimeoutException）
# wait = WebDriverWait(browser, 1)
# nameInput = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pn, .vm")))
# print(nameInput)

# ****************************************************************分割线****************************************************************
# todo Cookie

# import json
#
# from customutil.sql.model import Cookie
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # 通过浏览器启动参数设置header
# # ①firefox_options.set_preference（Firefox about:config查看所有启动参数）
# # ②chrome_options.add_argument
# firefox_options = Options()
# firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
#
# # 添加Cookie
# # ①selenium只能手动添加Cookie，不能像requests一样快速添加
# # ②必须先访问一次才能添加Cookie
# browser = webdriver.Firefox(options=firefox_options)
# browser.get("http://bbs.wuyou.net")
# browser.delete_all_cookies()
#
# url = "mysql+pymysql://{user}:{pwd}@{host}:{port}/python".format(host="127.0.0.1", port="3306", user="root", pwd="2468")
# DBSession = sessionmaker(bind=create_engine(url))
# cookies = DBSession().query(Cookie).filter(Cookie.site == "wuyou").limit(1).all()[0].cookie
#
# for cookie in json.loads(cookies):
#     browser.add_cookie(cookie)
#
# browser.get("http://bbs.wuyou.net/home.php?mod=spacecp")
# if "ss2468776986" in browser.page_source:
#     print("ss2468776986登录成功")

# ****************************************************************分割线****************************************************************
# todo Chrome/Firefox代理问题

# ①Chrome可以加载指定用户数据，通过SwitchyOmega决定是否使用代理
# ②"请停用以开发者模式运行的扩展程序"（直接停用）

# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
#
# chrome_options = ChromeOptions()
# chrome_options.add_argument("--user-data-dir=C:/Program Files/Google_Chrome/User Data")  # 加载指定用户数据
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#
# browser = webdriver.Chrome(options=chrome_options)
# browser.get("https://www.google.co.jp")

# ************************************************************半分割线******************************

# Firefox无法加载指定用户数据，但可以手动配置代理

# from selenium import webdriver
#
# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference("network.proxy.type", 1)
# firefox_profile.set_preference("network.proxy.socks", "127.0.0.1")
# firefox_profile.set_preference("network.proxy.socks_port", 1080)
#
# browser = webdriver.Firefox(firefox_profile=firefox_profile)
# browser.get("https://www.google.co.jp")

# ****************************************************************分割线****************************************************************
# todo selenium识别及反识别

# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
#
# chrome_options = ChromeOptions()
# chrome_options.add_argument("--user-data-dir=C:/Program Files/Google_Chrome/User Data")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#
# browser = webdriver.Chrome(options=chrome_options)
# browser.get("http://127.0.0.1/selenium")
