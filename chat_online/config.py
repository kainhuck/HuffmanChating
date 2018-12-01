import os
BASE_DIRS = os.path.dirname(__file__)

# 参数
options = {
    'port': 8000,
}

# 数据库配置
mysql = {
    "host": "",
    "user": "",
    "passwd": "",
    "dbName": ""
}

# 配置
settings = {
    "static_path": os.path.join(BASE_DIRS, 'static'),
    "template_path": os.path.join(BASE_DIRS, 'templates'),
    "login_url":'/login',
    "xsrf_cookies": True,
    "debug": True
}