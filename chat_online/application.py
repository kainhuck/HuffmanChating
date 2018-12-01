#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-11-2 下午7:32
# @Author  : KainHuck
# @Email   : kainhoo2333@gmail.com
# @File    : application.py

import tornado.web
from views import index
import os
import config

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/chatroom', index.ChatRoomHandler),
            (r'/home', index.HomeHandler),

            # 解密页面
            (r'/decode', index.DecodeHandler),

            # 注册页面
            (r'/register', index.RegisterHandler),

            # 登陆页面
            (r'/login', index.LoginHandler),

            # StaticFileHandler,注意要放在所有路由的最下面
            (r'/(.*)$', index.StaticFileHandler, {"path": os.path.join(config.BASE_DIRS, 'static/html'), \
                                                  "default_filename": "index.html"})
        ]
        super(Application,self).__init__(handlers,**config.settings)