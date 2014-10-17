import os.path
import sys
import json
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
        self.render('login.html',flag=1)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        subtype = self.get_argument('submit')

        if subtype == 'register':
            self.render('register.html',flag=1)
        elif subtype == 'login':
            result = dboperation().find_one({"username":username})
            if type(result) == type(None):
                self.render("login.html",flag=1)
            else:
                data = dict(result)
                if data.get("password") == password:
                    self.render('login.html',username = username,email = data.get('email'),flag=2)
                else:
                    self.render("login.html",flag=1)
        

class RegisterHandler(tornado.web.RequestHandler):
    """Cope form Request with form register"""
    def get(self):
        self.render('register.html',flag=1)

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        username = self.get_argument('username')
        data = dict({"email":email,"password":password,"username":username})
        flag = dboperation().insert(data)
        if flag  == 1:
            # self.render("register.html",username = username,email=email,flag=2)
            self.write("true")
      
class CheckInputHandler(tornado.web.RequestHandler):
    """Cope ajax request"""
    def post(self):
        checktype = self.get_argument("type")
        username = self.get_argument("username")
        if checktype == 'login':
            result = dboperation().find_one({"username":username})
            if type(result) == type(None):
                """username is not exist."""
                self.write("1")
            elif result.get("password") != self.get_argument("password"):
                """password is wrong"""
                self.write("2")
            else:
                """login success"""
                self.write("3")

        elif checktype == 'register':
            email = self.get_argument("email")
            password = self.get_argument("password")
            result_user = dboperation().find_one({"username":username})
            result_email = dboperation().find_one({"email":email})
            if type(result_user) ==type(None) and type(result_email) == type(None):
                """sign up success"""
                data = dict({"email":email,"password":password,"username":username})
                flag = dboperation().insert(data)
                self.write("3")
            elif type(result_user) != type(None):
                """username is not exist."""
                self.write("2")
            elif type(result_email) != type(None):
                """email is not exist."""
                self.write("1")


    


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers = [
                (r'/',LoginHandler),
                (r'/register',RegisterHandler),
                (r'/check',CheckInputHandler),
            ],
            template_path = os.path.join(os.path.dirname(__file__),"../view"),
            static_path=os.path.join(os.path.dirname(__file__), "../view/static"),
            debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    print ("Server run in port %d\n" , options.port)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()