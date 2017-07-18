#!/usr/bin/env python
import os
import jinja2
import webapp2
from model import Todo
from google.appengine.api import users

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
        return self.print_template()
    def post(self):
        task = self.request.get("task")
        todo = Todo()
        todo.task = task
        todo.put()
        return self.print_template()
    def print_template(self):
        user = users.get_current_user()
        if user:
            is_user = True
            user_url = users.create_logout_url('/')

        else:
            is_user = False
            user_url = users.create_login_url('/')
        tasks = Todo().query().fetch()
        params = {
            "tasks": tasks,
            "user": user,
            "is_user": is_user,
            "user_url": user_url
        }
        return self.render_template("hello.html", params)


class DeleteHandler(BaseHandler):
    def get(self, delete_id):
        task = Todo().get_by_id(int(delete_id))
        params = {
            "task": task.task
        }
        return self.render_template("delete.html", params)
    def post(self, delete_id):
        task = Todo().get_by_id(int(delete_id))
        task.key.delete()
        return self.redirect_to("home")


class EditHandler(BaseHandler):
    def get(self, edit_id):
        task = Todo().get_by_id(int(edit_id))
        params = {
            "task": task
        }
        return self.render_template("edit.html", params)
    def post(self, edit_id):
        done = self.request.get("done")
        task = Todo().get_by_id(int(edit_id))
        task.task = self.request.get("task")
        if done == "1":
            task.done = True
        else:
            task.done = False
        task.put()
        params = {
            "task": task
        }
        return self.render_template("edit.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="home"),
    webapp2.Route('/delete/<delete_id:\d+>', DeleteHandler),
    webapp2.Route('/edit/<edit_id:\d+>', EditHandler)
], debug=True)
