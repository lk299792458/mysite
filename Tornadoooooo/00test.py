# !*/user/bin/python3
# -*- coding: utf-8 -*-
import tornado.ioloop       # 开启循环，让服务一直等待请求的到来
import tornado.web          # web服务基本功能都封装在此模块中
import tornado.options      # 让模块有自定义的选项
import tornado.httpserver   # 启动一个单线程的http服务器
from  tornado.options import define,options

define('port',default=8000,help = 'run port',type = int)#help是帮助文档，自定义

class MainHandler(tornado.web.RequestHandler):#   Handler
    def get(self):                            #在这里指定请求的资源
        self.write('hello ')
        self.write("<br>")


application = tornado.web.Application(
    handlers = [
    (r'/a',MainHandler),
    ],
    debug = True   #调试模式，生产环境不能使用
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()