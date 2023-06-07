# ****************************************************************分割线****************************************************************
# todo pretty-errors

import pretty_errors

pretty_errors.replace_stderr()

# 全局导入：python -m pretty_errors
# （所有Python程序都能使用pretty_errors，而不需要一个个导入）
i = 1 / 0
print(i)
