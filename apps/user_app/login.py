# encoding=utf-8
import tornado.ioloop
import tornado.web
import os
from apps.appsettings import generalsettings
from util.log.trace import Trace
class userLoginHandler(tornado.web.RequestHandler):
    __tracer = Trace('user_app')
    def get_template_path(self):
        return os.path.join(generalsettings['templates'], 'user')

    def get(self):
        #content_dict = {'username': ''}
        self.__tracer.trace('user app get method',streamlevel=20,filelevel=20)
        self.render('login.html',myusername='')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        self.__tracer.trace('user app post method', streamlevel=20, filelevel=20)
        content = {'myusername':username}
        self.render('login.html',**content)


if __name__ == '__main__':
    application = tornado.web.Application([
        (r"/", userLoginHandler),
    ])
    application.listen(generalsettings['port'])
    tornado.ioloop.IOLoop.current().start()