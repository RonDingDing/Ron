from tornado.web import RequestHandler, url, Application
from tornado.ioloop import IOLoop
import json


class MyFormHandler(RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))
        # self.write(self.request.body)

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None


if __name__ == "__main__":
    app = Application([
        url(r"/", MyFormHandler),
        url(r"/myform", MyFormHandler)

    ], debug=True)
    app.listen(8888)
    IOLoop.current().start()
