Readme for jsErrLog
====================

What is this?
-------------
jsErrLog is a simple JavaScript script that catches your in-browser
JavaScript errors and posts them to a
[jserrlog.appspot.com][jsErrLogService]. This enables you to always be on
top of your JavaScript errors.

[jsErrLogService]: http://jserrlog.appspot.com

How to use
----------
Insert

    <script type="text/javascript" src="jserrlog.js"></script>

directly after your browsers <head> tag. You may optionally, directly
after tha script tag add additional parameters to the error
reporthandling:

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
***stub***

Contribute
----------
This project can be forked on Github. Please issue pull requests from
feature branches.

