from google.appengine.api import xmpp
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import string

class LogUser(db.Model):
        userName = db.StringProperty()
        serverName = db.StringProperty()
        userActive = db.BooleanProperty(default=False)

class XMPPHandler(webapp.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        user_address = self.request.get('from').split('/')[0]       
        msg = ""
        
        if message.body[0:6].lower() == 'status':
            # Look up their URL(s) and list status(es)
            q = db.GqlQuery("SELECT * FROM LogUser " + 
                "WHERE userName = :1", 
                string.lower(user_address)) 

            msg = "For user: '" + user_address + "'\n"
            if q.count()>0:
                results = q.fetch(500)
                for p in results:
                    msg += "URL: " + p.serverName + ":"
                    if p.userActive:
                        msg += "Active"
                    else:
                        msg += "Inactive"
                    msg += "\n"
            else:
                msg += "No URLs defined for user\n"
            chat_message_sent = False
        elif message.body[0:4].lower() == 'stop':
            # Look up their URL(s) and disable them
            q = db.GqlQuery("SELECT * FROM LogUser " + 
                "WHERE userName = :1", 
                string.lower(user_address))
            results = q.fetch(500)
            for p in results:
                p.userActive = False
                p.put() 
            msg = "Alerts disabled for user: '" + user_address + "'\n"  
        elif message.body[0:5].lower() == 'start':
            # Look up their URL(s) and disable them
            q = db.GqlQuery("SELECT * FROM LogUser " + 
                "WHERE userName = :1", 
                string.lower(user_address))
            results = q.fetch(500)
            for p in results:
                p.userActive = True
                p.put() 
            msg = "Alerts enabled for user: '" + user_address + "'\n" 
        else:
            msg = "Available messages are:\n'Status' to list current conditions\n'Start' to enable messages\n'Stop' to disable messages."
            
        if msg != "":
            if xmpp.get_presence(user_address):
                status_code = xmpp.send_message(user_address, msg)
                chat_message_sent = (status_code == xmpp.NO_ERROR)            
                chat_message_sent = False

                
application = webapp.WSGIApplication([('/_ah/xmpp/message/chat/', XMPPHandler)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()