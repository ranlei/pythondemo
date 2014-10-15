import os.path
import sys
sys.path.append("..")

from model.dbmani import dboperation

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8888,help="run this port",type=int)
class LoginHandler(tornado.web.RequestHandler):
    """Cope form Request with from login"""
    
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        subtype = self.get_argument('submit')

        if subtype == 'register':
            self.render('register.html')
        elif subtype == 'login':
            data = dict(dboperation().find_one({"username":username}))
            print data
            if data.get("password") == password:
                    self.render('success.html',username = username,type = 'login',email = data.get('email'))
            else:
                self.render("fail.html",type="login")
        

class RegisterHandler(tornado.web.RequestHandler):
    """Cope form Request with form register"""
    def get(self):
        self.render('register.html')

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        username = self.get_argument('username')
        data = dict()
        data = {"email":email,"password":password,"username":username}
        flag = dboperation().insert(data)
        print flag
        if flag  == 1:
            self.render("success.html",type = 'register',username = username,email=email)
        else:
            self.render("fail.html",type="login")



if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers = [(r'/',LoginHandler),(r'/register',RegisterHandler)],
            template_path = os.path.join(os.path.dirname(__file__),"../view"),
            debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()