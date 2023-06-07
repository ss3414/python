# ****************************************************************分割线****************************************************************
# todo flask_apscheduler

from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()

@scheduler.task(trigger="cron", day="1-31", hour="12", minute="0", second="0")
def job():
    print("job")

if __name__ == "__main__":
    app = Flask(__name__)

    scheduler.init_app(app)
    scheduler.start()

    app.run(host="127.0.0.1", port=80)
