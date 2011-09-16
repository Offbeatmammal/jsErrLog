from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import os
from google.appengine.ext.webapp import template
from datetime import datetime, date, time

class LogErr(db.Model):
		#appName = db.StringProperty()
		serverName = db.StringProperty()
		serverPath = db.StringProperty()
		fileLoc = db.StringProperty()
		lineNo = db.StringProperty()
		errMsg = db.StringProperty()
		infoMsg = db.StringProperty()
		IP = db.StringProperty()
		UA = db.StringProperty()
		OSName = db.StringProperty()
		OSVer = db.StringProperty()
		BrowserName = db.StringProperty()
		BrowserVer = db.StringProperty()
		guid = db.StringProperty()
		ts = db.DateTimeProperty( auto_now_add=True )

class MainHandler(webapp.RequestHandler):
	def get(self):
		url = self.request.get("sn")
		q = db.GqlQuery("SELECT * FROM LogErr " + 
                "WHERE serverName = :1 " + 
                "ORDER BY ts DESC", 
                url)
 
		results = q.fetch(500) 

		body = ("<results url=\"%s\">\n" % url)
		for p in results:		
			body += ("<entry ts=\"%s\">\n" % (p.ts.strftime("%m/%d/%Y %H:%M:%S")))
			body += ("<serverPath>%s</serverPath>\n" % p.serverPath)
			body += ("<file lineNo=\"" + p.lineNo + "\">" + p.fileLoc + "</file>\n")
			body += ("<error>%s</error>\n" % p.errMsg)
			body += ("<OS name=\"" + p.OSName + "\" version=\"" + p.OSVer + "\"/>\n")
			body += ("<Browser name=\"" + p.BrowserName + "\" version=\"" + p.BrowserVer + "\"/>\n")
			body += ("<infoMsg>%s</infoMsg>\n" % p.infoMsg)
			body += ("</entry>\n")
		body += ("</results>\n")

		template_values = {
			'pageBody': body,
			}

		path = os.path.join(os.path.dirname(__file__), 'report.xml')
		self.response.headers['Content-Type'] = "application/xml"
		self.response.out.write(template.render(path, template_values))	
	
def main():
    application = webapp.WSGIApplication([('/report.xml', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
