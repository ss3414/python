# ****************************************************************分割线****************************************************************
# todo argparse

# 运行：python argparsedemo.py 127.0.0.1 -p 80

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str, help="host")
parser.add_argument("-p", "--port", type=int, default=80, help="port")
args = parser.parse_args()

print(args)
print(args.host)
print(args.port)
