Readme for jsErrLog
====================

What is this?
-------------
jsErrLog is a simple JavaScript script that catches your in-browser
JavaScript errors and posts them to the
[jsErrLog Service](jserrlog.appspot.com). This enables you to always be on
top of your JavaScript errors.

jsErrLog Service: http://jserrlog.appspot.com

How to use
----------
Insert

    <script type="text/javascript" src="jserrlog.js"></script>

directly after your browsers <head> tag. You may optionally, directly
after tha script tag add additional parameters to the error
report handling:

    <script type="text/javascript">
        // Configure site parameters
        //jsErrLog.debugMode = true;
        // Optionally add additional debug information to the jsErrLog.info
        // message field
        //jsErrLog.info = "Populated the Info Message to pass to logger"
    </script>

The options are:

* **jsErrLog.debugMode**: Set to true if you'd like the web browser not
  to swallow in-browser errors.
* **jsErrLog.info**: A custom string bundled with the HTTP GET request.
  Can be used to add additional information, such as a customer number,
  extra state or similar.

Which web browsers does this script support?
--------------------------------------------
* IE 6.0 and above
* Firefox 4 and above
* Chrome 10 and above (including ChromeOS)
* Safari 5.1 and above / WebKit nightlies (thought this [error needs resolving](https://bugs.webkit.org/show_bug.cgi?id=63506).)

Un-supported browsers at this time
----------------------------------
* Opera
* Android

Additional information
----------------------
Original blog posts are [available here](http://post.offbeatmammal.com/tag/jserrlog)

Contribute
----------
This project can be forked on Github. Please issue pull requests from
feature branches.
