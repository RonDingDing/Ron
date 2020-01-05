from tornado.web import RequestHandler
 
class MainHandler( RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)

 