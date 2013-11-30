from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import os
import logging
from google.appengine.ext.webapp import template
from datetime import datetime, date, time
from google.appengine.api import memcache

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
		typ = self.request.get("type")
		
		rsp = memcache.get(typ + ":" + url)
		if rsp is None:
			rsp = self.render_rsp( url, typ )
			if not memcache.add(typ + ":" + url, rsp, 10800):
				logging.error("Memcache set failed.")
        
		
		template_values = {
			'pageBody': rsp,
			}

		path = os.path.join(os.path.dirname(__file__), 'report.xml')
		self.response.headers['Content-Type'] = "application/xml"
		self.response.out.write(template.render(path, template_values))		
		
	def render_rsp(self,url,typ):	
		q = db.GqlQuery("SELECT * FROM LogErr " + 
                "WHERE serverName = :1 " + 
                "ORDER BY ts DESC", 
                url)
 
		results = q.fetch(500) 

		if typ == "rss":
			now = datetime.now()
			body = '<rss version="2.0">\n'
			body += '<channel>\n'
			body += ('<title>jsErrLog Feed for %s</title>\n' % url)
			body += ('<link>%s</link>\n' % url)
			body += ('<description>Javascript errors reported for %s</description>' % url)
			body += '<language>en-us</language>'
			body += '<ttl>180</ttl>'
			body += ('<pubDate>%s</pubDate>\n' % now.strftime("%a, %d %b %Y %H:%M:%S +0000"))
			body += '<generator>jsErrLog</generator>\n'
			
			for p in results:
				body += '<item>\n'
				body += '<title>' + p.serverPath + '</title>\n'
				body += '<link>' + p.fileLoc + '</link>\n'
				body += '<description>'
				body += 'At ' + p.ts.strftime("%m/%d/%Y %H:%M:%S")
				body += (". Exception in %s " % p.serverPath)
				body += ("at line " + p.lineNo + " in " + p.fileLoc + "\n")
				body += ("The error was: %s\n" % p.errMsg)
				body += ("Client OS:" + p.OSName + " version=" + p.OSVer + "\n")
				body += ("Browser:" + p.BrowserName + " version=" + p.BrowserVer + "\n")
				body += ("Additional info:%s" % p.infoMsg)
				body += '</description>\n'
				body += "<pubDate>" + p.ts.strftime("%a, %d %b %Y %H:%M:%S +0000") + "</pubDate>\n"
				body += '<guid isPermaLink="false">'
				body += p.fileLoc + '-' + p.lineNo + '-' + p.ts.strftime("%m/%d/%Y-%H:%M:%S") + '-' + p.guid
				body += '</guid>\n'
				body += '</item>\n'
			
			body += '</channel>\n'
			body += '</rss>\n'
		else:
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

		return body
		
def main():
    application = webapp.WSGIApplication([('/report.xml', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
