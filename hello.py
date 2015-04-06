#!/usr/bin/env python

# Tornado模块
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options
# tornado.options 从命令行中读取设置
# 如果给出，就全局都使用
# 如果没给，就使用default值
# 当给出help时，返回help后内容
# type定义参数类型，默认port=8000，用户可以自定义端口
define("port",default=8000,help="run onthe given port",type=int)

# 请求处理函数类，处理一个请求时，Tornado将这个类实例化
# 调用http请求方法对应的方法
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		# 获取字符串，没传就取第二个参数值
		greeting=self.get_argument('greeting','Hello')
		# write方法，函数的参数，写入到http响应中
		self.write(greeting+', friendly user!')
if __name__ == '__main__':
	# 
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
