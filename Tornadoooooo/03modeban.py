# !*/user/bin/python3
# -*- coding: utf-8 -*-
import tornado.ioloop       # 开启循环，让服务一直等待请求的到来
import tornado.web          # web服务基本功能都封装在此模块中
import tornado.options      # 让模块有自定义的选项
import time
import tornado.httpserver #启动一个单线程的http服务器
from tornado.options import  define,options

define('port',default=8000, help='run port',type = int)

class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('in_out_1.html')

    def post(self,*args,**kwargs):
        name = self.get_argument('name','None')
        urllist = [
            ('https://www.shiguangkey.com','时光课堂'),
            ('https://www.baidu.com','百度'),
            ('https://www.taobao.com','淘宝'),
        ]
        atga = '<a href = "https://www.baidu.com" target = "_blank">__百度__</a><br>'
        self.render('templates02.html',
                    username = name,
                    time = time,
                    urllist = urllist,
                    atga = atga
        )

application = tornado.web.Application(
    handlers=[
        (r'/main',MainHandle)
    ],
    static_path='statics',        #静态文件路径
    template_path = 'templates',  #template_path 命名不可变，固定用法，文件名自定义
    debug = True                  #调试模式，生产不能用，实际上线之后，不能用
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()