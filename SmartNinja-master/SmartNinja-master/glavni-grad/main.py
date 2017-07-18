#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2
import random

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
    drzave = {
        "Hrvatska": "Zagreb",
        "Slovenia": "Ljubljana",
        "Austrija": "Bec"
    }
    trenutna_drzava = "Ovo nije nista"
    def get(self):
        trenutna_pozicija = random.randint(0,2)
        self.trenutna_drzava = self.drzave.keys()[trenutna_pozicija]
        parametri = {
            "drzava": self.trenutna_drzava
        }
        return self.render_template("homepage.html", parametri)
    def post(self):
        rezultat = "Odgovor nije tocan"
        grad = self.request.get("grad").lower()
        self.trenutna_drzava = self.request.get("drzava")
        if(self.drzave[self.trenutna_drzava].lower() == grad):
            rezultat = "Odgovor je tocan"

        return self.write(rezultat)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
