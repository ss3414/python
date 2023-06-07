# ****************************************************************分割线****************************************************************
# todo logging

import logging

# 日志等级：FATAL>ERROR>WARN>INFO>DEBUG（错误>异常>警告>信息>调试，默认WARN）
logging.basicConfig(
    level=logging.DEBUG,
    # format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
    format="%(message)s",
    # filename="C:/Users/Administrator/Desktop/logging.log"  # 写入到文件
)

str = "str"
logging.debug(str)
logging.info("logging.info")
