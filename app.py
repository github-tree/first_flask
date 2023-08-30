import pymysql
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    connection = pymysql.connect(
        host='127.0.0.1',  # 数据库IP地址
        port=3306,  # 端口
        user='root',  # 数据库用户名
        password='flask_project',  # 数据库密码
        database='flask_databases'  # 数据库名称
    )
    return "恭喜，MySQL数据库已经连接上"

if __name__ == "__main__":
    app.run()