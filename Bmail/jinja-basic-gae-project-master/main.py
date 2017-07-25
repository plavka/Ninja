#!/usr/bin/env python
import json
import os
import jinja2
import webapp2
from model import Message
from google.appengine.api import users
from google.appengine.api import urlfetch



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
        user = users.get_current_user()
        if user:
            is_user = True
            user_url = users.create_logout_url('/')

        else:
            is_user = False
            user_url = users.create_login_url('/')
        params = {
            "user": user,
            "is_user": is_user,
            "user_url": user_url
        }
        return self.render_template("hello.html", params)
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
        message.message_archived = True
        message.put()
        return self.redirect_to("message-list")

class NewMessageHandler(BaseHandler):
    def get(self):
        return self.print_template()


class WeatherHandler(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=e8ddcce3dc2a1afd1dc47479e2cdd6cd"
        result = urlfetch.fetch(url)
        data = json.loads(result.content)
        params = {"data": data}
        self.render_template("weather.html", params)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/login', WeatherHandler),
    webapp2.Route('/messages', MessageHandler),
    webapp2.Route('/messages/<message_id:\d+>/delete', DeleteHandler),
    webapp2.Route('/messages/<message_id:\d+>/edit',EditHandler),
    webapp2.Route('/new_message', NewMessageHandler),
    webapp2.Route('/weather', WeatherHandler)
], debug=True)
