# ****************************************************************分割线****************************************************************
# todo airtest

# Airtest（基于图像识别），Poco（基于UI控件识别），AirtestIDE（Airtest/Poco的IDE）

# from airtest.core.api import *
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#
# # AirtestIDE
# # ①可以辅助连接设备，connect_device相当于在AirtestIDE中连接设备
# # ②可以录制脚本
# # ③连接Android需要允许USB调试+安装PocoServices/Yosemite
# # connect_device("Android://127.0.0.1:5037/e4cbc4d7")  # 小米8SE（USB）
# connect_device("Android://127.0.0.1:5037/192.168.2.172:5555")  # WiFi
#
# # Poco脚本可直接在AirtestIDE中运行
# poco = AndroidUiautomationPoco()
# poco(text="知乎").click()  # 点击知乎
