# ****************************************************************分割线****************************************************************
# todo RunningCheeseFirefox-131
# 只支持Chrome104以下版本

import browser_cookie3
import requests

cookiejar = browser_cookie3.firefox(cookie_file="C:/Program Files/RunningCheeseFirefox/Profiles/cookies.sqlite")

session = requests.Session()
session.cookies = cookiejar
response = session.get("http://bbs.wuyou.net/forum.php")
print(response.text)
