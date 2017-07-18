#!/usr/bin/env python
import os
import jinja2
import webapp2
from model import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")
    def post(self):
        message_text = self.request.get("message")
        message = Message()
        message.message_text = message_text
        message.put()
        return self.render_template("hello.html", params={
            "message": message_text
        })
class MessageHandler(BaseHandler):
    def get(self):
        messages = Message().query(Message.message_archived == False).fetch()
        return self.render_template("messages.html", params={
            "messages": messages
        })
class EditHandler(BaseHandler):
    def get(self, message_id):
        message = Message().get_by_id(int(message_id))
        return self.render_template("edit.html", params={
            "message": message
        })
    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message_text = self.request.get("message")
        message.message_text = message_text
        message.put()
        return self.redirect_to("message-list")


class DeleteHandler(BaseHandler):
    def get(self, message_id):
        message = Message().get_by_id(int(message_id))
        return self.render_template("delete.html", params={
            "message": message
        })
    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        #Message delete command
        #message.key.delete()
        message.message_archived = True
        message.put()
        return self.redirect_to("message-list")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/messages', MessageHandler, name="message-list"),
    webapp2.Route('/messages/<message_id:\d+>/edit',EditHandler),
    webapp2.Route('/messages/<message_id:\d+>/delete', DeleteHandler)
], debug=True)
