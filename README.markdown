Readme for jsErrLog
====================

What is this?
-------------
jsErrLog is a simple JavaScript script that catches your in-browser
JavaScript errors and posts them to the
[jsErrLog Service](jserrlog.appspot.com). This enables you to always be on
top of your JavaScript errors.

jsErrLog Service Homepage and demo site: http://jserrlog.appspot.com

How to use
----------
Insert

    <script type="text/javascript" src="jserrlog.js"></script>

directly after your browsers <code>&lt;head></code> tag. You may optionally, directly
after the script tag, add additional parameters to the error
report handling:

    <script type="text/javascript">
        // Configure site parameters
		// Optional to allow the error message to also be presented to the user
        //jsErrLog.debugMode = true;
        // Optionally add additional debug information to the jsErrLog.info
        // message field
        //jsErrLog.info = "Populated the Info Message to pass to logger"
        // Optionally specify URL to which the logging should be done
        //jsErrLog.url = "http://www.myservice.com/logger.js";
		// Optionally specify certain querystring parameters never to pass to the logging service
		// either on the fileloc or the server name. Simply list them in the array
		// and script will check for them (case insensitive)
		//jsErrLog.qsIgnore = ["userid","password"];
    </script>

The options are:

* **jsErrLog.debugMode**: Set to true if you'd like the web browser not
  to swallow in-browser errors.
* **jsErrLog.info**: A custom string bundled with the HTTP GET request.
  Can be used to add additional information, such as a customer number,
  extra state or similar.
* **jsErrLog.url**: The absolute URL to which GET requests will be made. See
  [below](#yourownservice) for more information on how to do this. If not
  specified, the jsErrLog.url will default to http://jserrlog.appspot.com/logger.js
* **jsErrLog.qsIgnore**: populates an array of querystring parameters to be stripped before reporting

Which web browsers does this script support?
--------------------------------------------
* IE 6.0 and above
* Firefox 3.6.22 and above
* Chrome 10 and above (including ChromeOS)
* Safari 5.1 and above / WebKit nightlies (thought this [error needs
  resolving](https://bugs.webkit.org/show_bug.cgi?id=63506).)
* Opera v11.60 (and Opera.Next v12) with Presto/2.10.229 JS engine and above

Un-supported browsers at this time
----------------------------------
* Android

Additional information
----------------------
Original blog posts are [available here](http://post.offbeatmammal.com/tag/jserrlog).

If your browser is not in the list above, please consider opening up the
jsErrLog demo page (_src/demo/index.html_) to help us verify whether the
script works in your browser or not.

How to point jsErrLog to your own service<a name="yourownservice"/>
-----------------------------------------
There are a couple of cases when you might want to host your own jsErrLog
server that receives all the errors on your site:

* You are worried about security. This includes:
 * That user credentials might get passed to the appspot service and be
   publicly available for others to view as long as they know your full domain
   URL.
 * That the response JavaScript file in the future might contain malicious code
   that enables cross site scripting attacks (XSS).
* You would like to have the errors e-mailed to you directly.
* You would like to incorporate the error messages into your existing company
  workflow. Two examples are
 * Sending out an e-mail to one or multiple people about the error.
 * Adding the JavaScript to some ticketing system.
* You are on an Intranet that blocks communication out to the WWW.

To roll your own jsErrLog service there are two things you need to do:

1. Override the default URL that the jsErrLog browser script should use.
2. Implement your server side engine to handle the requests coming in from
   browsers.

### Overriding the default URL

This one is easy. Just set the <code>jsErrLog.url</code> to something similar
to the URL of your error logger. A full example here below:

    <script type="text/javascript" src="jserrlog.js"></script>
    <script type="text/javascript">
        jsErrLog.url = "http://www.myownservice.com/logger.js";
    </script>

note that it is recommended for the URL to end with '.js'. Also note that it
must support HTTP GET requests.

### Implementing your own logging service

For every client side (in-browser) JavaScript error, an HTTP GET request is
is being made to the URL you specified. Every request contains the following
parameters:

* <code>i</code>: A unique identifier that identifies the a temporary
  <code>&lt;script /&gt;</code> tag added to your
  <code>&lt;head&gt; … &lt;/head&gt;</code>. This identifier is used in the
  response back to the client. See more on this below.
* <code>sn</code>: The <code>document.URL</code> at which the error occured.
* <code>fl</code>: The JavaScript file in which the error occurred.
* <code>ln</code>: The line number in <code>fl</code> on which the error
  occurred.
* <code>err</code>: A string describing the error.
* <code>ui</code>: A (most certainly) unique string for your error message.
  It is being generated according to [RFC 4112, section 4.4][RFC4112].
* <code>info</code>: The optionally specified <code>jsErrLog.info</code> string
  set when loading the page.

[RFC4112]: http://www.ietf.org/rfc/rfc4122.txt

You can verify that the format of the parameters using a tool such as [Fiddler](http://fiddlertool.com) to watch the messages as they are sent over http.

The response given by your service ***must be valid JavaScript***. This is
*very* important, as it otherwise might lead to a flood of requests coming in
as one JavaScript yields another one (and each one a new request).

Generally it is good to clean up in the client's DOM. This is done by adding
the following line in your response body:

    jsErrLog.removeScript(<?=$_GET['i']?>);

where <code><?=$_GET['i']?></code> (which is PHP) can be substituted with your
language specific way of extracting the value of the GET parameter
<code>i</code>.

You may also add additional JavaScript in your response if you want to. You
could for example show a simple <code>alert(…)</code> box telling the user that
the error has been logged and that you are looking into it. However, do note
that the alert box might pop up multiple times being both annoying and/or
making the browser unusable if stuck in a bad loop. Another option would be to
have a 'soft popup' show up in the client's web interface.

Also, note that not all JavaScript errors will always be errors that the user
will notice. Maybe he/she will never click on the button that would trigger the
broken callback function etcetera.

Contribute
----------
This project can be forked from
[Github](https://github.com/Offbeatmammal/jsErrLog). Please issue pull
requests from feature branches.
