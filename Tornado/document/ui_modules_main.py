import uimodules
from tornado.web import RequestHandler, HTTPError, Application


class HomeHandler(RequestHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY date DESC")
        self.render("home.html", entries=entries)


class EntryHandler(RequestHandler):
    def get(self, entry_id):
        entry = self.db.get("SELECT * FROM entries WHERE id = %s", entry_id)
        if not entry:
            raise HTTPError(404)
        self.render("entry.html", entry=entry)


settings = {
    "ui_modules": uimodules,
}
application = Application([
    (r"/", HomeHandler),
    (r"/entry/([0-9]+)", EntryHandler),
], **settings)
