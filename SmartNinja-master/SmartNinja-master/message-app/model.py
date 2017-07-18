from google.appengine.ext import ndb

class Message(ndb.Model):
    message_text = ndb.StringProperty()
    message_time = ndb.DateTimeProperty(auto_now_add=True)
    message_archived = ndb.BooleanProperty(default=False)