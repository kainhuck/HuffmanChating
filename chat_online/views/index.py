from tornado.web import RequestHandler, authenticated
from tornado.websocket import WebSocketHandler
import tornado.web

import time

from huff_code import huffman
# 上传文件使用
import config
import os

# 数据库使用
from models import users

# 聊天室后台
class ChatRoomHandler(WebSocketHandler):
	users = []
	# def prepare(self):
	# 	name = self.get_cookie('name')

	def open(self, *args, **kwargs):
		self.users.append(self)
		name = self.get_cookie('name')
		for user in self.users:
			t = time.ctime()
			user.write_message(u"<p>[%s]登陆了 [%s]</p>"%(name, str(t)))

	def on_message(self, message):
		name = self.get_cookie('name')
		code_dict_head = huffman.Main_HfTree()
		string = list(message)  # 将字符串转换成列表
		encode_string = [code_dict_head[0][str(each)] for each in string]  # 加密之后的列表

		ss = ''
		for each in encode_string:
			for i in each:
				ss += str(i)

		for user in self.users:
			user.write_message(u"<p>[%s]说:%s</p>"%(name, ss))

	def on_close(self):
		self.users.remove(self)
		name = self.get_cookie('name')
		for user in self.users:
			t = time.ctime()
			user.write_message(u"<p>[%s]退出了  [%s]</p>"%(name, str(t)))

	def check_origin(self, origin):
		return True

# 注册页面
class RegisterHandler(RequestHandler):
	def get(self, *args, **kwargs):
		self.render('register.html')

	def post(self, *args, **kwargs):
		username = self.get_argument('username')
		password = self.get_argument('password')
		repasd = self.get_argument('re_password')
		if repasd == password:
			# ip = self.request.remote_ip
			# print(username, password, ip)
			user = users(username, password)
			user.save()
			self.redirect('/home')
		else:
			self.redirect('/register')

# 聊天室主页
class HomeHandler(RequestHandler):
	def get_current_user(self):
		flag = self.get_argument('flag', None)
		return flag

	@authenticated
	def get(self, *args, **kwargs):
		self.render('home.html')

# 登陆页面
class LoginHandler(RequestHandler):
	def get(self, *args, **kwargs):
		next = self.get_argument('next', '/')
		url = 'login?next=' + next
		self.render('login.html', url=url)

	def post(self, *args, **kwargs):
		user_dict = {}
		users_list = users.all()
		user_dict['username'] = self.get_argument('username')
		user_dict['password'] = self.get_argument('password')
		if user_dict in users_list:
			next = self.get_argument('next', '/')
			self.set_cookie('name', user_dict['username'])
			print(user_dict['username'],'登陆了')
			self.redirect(next+'?flag=logined')
		else:
			next = self.get_argument('next', '/')
			self.redirect('/login?next='+next)

# 解码页面
class DecodeHandler(RequestHandler):
	def get(self, *args, **kwargs):
		text = "这里展示解码内容"
		self.render('decode.html', text=text)

	def post(self, *args, **kwargs):
		code_dict_head = huffman.Main_HfTree()
		code_string = self.get_argument('code')
		text_list = []  # 存放译文的列表
		huffman.decode(list(code_string), code_dict_head[1], code_dict_head[1], text_list)
		text = ''
		for each in text_list:
			text += each
		self.render('decode.html', text=text)







# 定义自己的StaticFileHandler
class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token