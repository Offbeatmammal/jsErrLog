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
        pageTitle = " - Report"
        pageHeader = "Tracking Javascript Errors"

        body = ("<p><a href='/index.html'>jsErrLog</a> Reporting: Requests for <b>" + url + "</b> <a href='rpt.html'>change</a><br>")
        body += ("Direct link to <a href=\"report.xml?sn=" + url + "\">XML version</a><br>")
        body += ("<table>")
        body += ("<tr><td>Time<td>Path<td>Location<td>Line No<td>Err Msg<td>OS<td>Browser<td>Info Msg")
        for p in results:		
            #t = datetime.strptime(str(p.ts).split(".", 1)[0], "%Y-%m-%d %H:%M:%S")
            #t2 = p.ts.strftime("%m/%d/%Y %H:%M:%S")
            body += ("<tr><td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s" % (p.ts.strftime("%m/%d/%Y %H:%M:%S"),p.serverPath,p.fileLoc, p.lineNo, p.errMsg, p.OSName+" "+p.OSVer, p.BrowserName+" " +p.BrowserVer, p.infoMsg))
        body += ("</table>")

        template_values = {
            'pageTitle': pageTitle,
            'pageHeader': pageHeader,
            'pageBody': body,
            'url': url
            }

        path = os.path.join(os.path.dirname(__file__), 'templateReport.html')
        self.response.out.write(template.render(path, template_values))	
    
def main():
    application = webapp.WSGIApplication([('/report.html', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
