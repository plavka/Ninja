from google.appengine.ext import ndb

class Todo(ndb.Model):
    task = ndb.StringProperty()
    done = ndb.BooleanProperty(default=False)