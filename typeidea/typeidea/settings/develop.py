from .base import *  #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'typeidea',  # 数据库名
        'USER': 'root',   # 用户名
        'PASSWORD': 'ary6769339jy',   # 密码
        'HOST': 'localhost',   # 主机
        'POST': '3306',   # 端口号
    }
}