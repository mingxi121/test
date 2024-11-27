# -- coding:utf-8 --
"""
 @Software: PyCharm
 @Date: 2024/3/1 16:14
 @Author: Glimmering
 @Function: 系统配置
"""

# 加密盐
SECRET_KEY = "asdfghjklzxcvbn"

# 连接MySQL数据库的配置
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'sleep'   # 按实际情况更改
USERNAME = 'root'
PASSWORD = 'fanmingxi041201'
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2862528612@qq.com"  # 以下三项按实际情况更改，去QQ邮箱申请授权码就好
MAIL_PASSWORD = "hfxksnhqoeyyddii"
MAIL_DEFAULT_SENDER = "2862528612@qq.com"

# openAi api key
OPENAI_API_KEY = ""

# openAi 代理 api
URL = "https://api.openai-proxy.com/v1/chat/completions"