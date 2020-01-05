from tornado.web import Application, url, RedirectHandler, RequestHandler
app = Application([
    url(r"/app",  RedirectHandler,
        dict(url="http://itunes.apple.com/my-app-id")),
    ])


class MyPhotoHandler(RequestHandler):
    pass


app = Application([
    url(r"/photos/(.*)", MyPhotoHandler),
    url(r"/pictures/(.*)", RedirectHandler,
        dict(url=r"/photos/{0}")),
    ])