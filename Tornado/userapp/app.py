import tornado
from handlers import user as user_handlers

HANDLERS = [
    (r"/api/users", user_handlers.UserListHandler), 
    (r"/api/users/(\d+)", user_handlers.UserHandler)
]


def run():
    app = tornado.web.Application(HANDLERS, debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    port = 9000
    print("server start on port: {}".format(port))
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
