#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {
            "title": "Ovo je neki naslov nesto",
            "number": -56
        }
        return self.render_template("hello.html", params=params)
    def post(self):
        inputValue = self.request.get("text_input")
        numberValue = self.request.get("number_input")
        params = {
            "title": inputValue,
            "number": numberValue
        }
        return self.render_template("hello.html", params=params)

class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")

class ResponceHandler(BaseHandler):
    def post(self):
        data = self.request.get("text_input")
        return self.write("Ovo radi " + data)


class CalculatorHandler(BaseHandler):
    def get(self):
        return self.render_template("calculator.html")
    def post(self):
        response = "Error (check your data)"
        try:
            first_num = float(self.request.get("first_num"))
            operator = self.request.get("operator")
            second_num = float(self.request.get("second_num"))
            if operator == "+":
                response = first_num + second_num
            elif operator == "-":
                response = first_num - second_num
            elif operator == "*":
                response = first_num * second_num
            elif operator == "/":
                response = first_num / second_num
            else:
                response = "Wrong operator"
        except:
            response = "First and last input must be numbers"
        return self.write(response)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/responce', ResponceHandler),
    webapp2.Route('/calculator', CalculatorHandler)
], debug=True)
