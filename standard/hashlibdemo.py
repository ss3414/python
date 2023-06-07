# ****************************************************************分割线****************************************************************
# todo hashlib

import hashlib

str = "123456"
enc = hashlib.md5()  # MD5
enc.update(str.encode(encoding="UTF-8"))
print(enc.hexdigest())
