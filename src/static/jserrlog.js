///////////////////////////////////////////////////////////////////////////////
//
//  jsErrLog.js         version 1.4.2
//
//  Trap javascript errors on a webpage and re-direct them to a remote logging service
//  which can then be used to identify and resolve issues without impacting user experience
//
//  v1.4.2: domainIgnore adds prefix ignore on file location
//  v1.4.1: added support for colNo in browsers that support it (IE10, Chrome30)
//  v1.4.0: limit initialization to one instance, escape FL and ERR parameter, limit reports sent
//  v1.3.0: add support for jsErrLog.qsignore parameter
//  v1.2.0: add support for jsErrLog.url parameter
//  v1.1.0: add support for jsErrLog.info parameter
//  v1.0.0: Original
///////////////////////////////////////////////////////////////////////////////

if (!window.jsErrLog) {
	window.jsErrLog = { };

	// default to debugging off
	jsErrLog.debugMode = false;
	// default error message to blank
	jsErrLog.error_msg = "";
	// default the index for the message to 0 in case there is more than one
	jsErrLog.err_i = 0;
	// default the additional info message to blank
	jsErrLog.info = "";
	// default the URL to the appspot service
	jsErrLog.url = "http://jserrlog.appspot.com/logger.js";
	// default the qsIgnore to nothing (ie pass everything on the querystring)
	jsErrLog.qsIgnore = new Array();
	// default ignored domains to nothing
    jsErrLog.domainIgnore = new Array();
	// max number of reports sent from a page (defaults to 10, -1 allows infinite)
	jsErrLog.maxRep = 10;

	// used internally for testing to know if test succeeded or not
	jsErrLog._had_errors = false;

	// add the hook to the onError event
	// - first store any existing error handler for the page
	jsErrLog.fnPreviousOnErrorHandler = window.onerror; 
	// - attach our error handler
	window.onerror = function(msg, file_loc, line_no, col_no){
		jsErrLog.ErrorTrap(msg, file_loc, line_no, col_no);
		if(typeof(jsErrLog.fnPreviousOnErrorHandler) == "function") {
			// process any existing onerror handler 
			jsErrLog.fnPreviousOnErrorHandler(msg, file_loc, line_no, col_no);
		}
		return true;
	}
}

jsErrLog.appendScript = function(index, src) {
	try {
		var script = document.createElement("script");
		script.id = "script" + index;
		script.src = src;
		script.type = "text/javascript";

		var head = document.getElementsByTagName("head")[0];
		head.appendChild(script);
	}
	catch (e) {
		jsErrLog.ErrorHandler("appendScript", e);
	}
};

jsErrLog.removeScript = function(index) {
	try {
		var script = document.getElementById("script" + index);
		var head = document.getElementsByTagName("head")[0];
		head.removeChild(script);
	}
	catch (e) {
		jsErrLog.ErrorHandler("removeScript", e);
	}
};

jsErrLog.ErrorHandler = function(source, error) {
  jsErrLog._had_errors = true;
	alert("jsErrLog encountered an unexpected error.\n\nSource: " + source + "\nDescription: " + error.description); 
};

jsErrLog.guid = function() { // http://www.ietf.org/rfc/rfc4122.txt section 4.4
	return 'aaaaaaaa-aaaa-4aaa-baaa-aaaaaaaaaaaa'.replace(/[ab]/g, function(ch) { 
		var digit = Math.random()*16|0, newch = ch == 'a' ? digit : (digit&0x3|0x8); 
		return newch.toString(16); 
		}).toUpperCase();
}

// Needed to break the URL up if we want to ignore parameters
function parseURL(url)
{
    // save the unmodified url to "href" property so
    // the returned object matches the built-in location object
    var locn = { 'href' : url };

    // split the URL components
    var urlParts = url.replace('//', '/').split('/');

    //store the protocol and host
    locn.protocol = urlParts[0];
    locn.host = urlParts[1];

    //extract port number from the host
    urlParts[1] = urlParts[1].split(':');
    locn.hostname = urlParts[1][0];
    locn.port = urlParts[1].length > 1 ? urlParts[1][1] : '';

    //splice and join the remainder to get the pathname
    urlParts.splice(0, 2);
    locn.pathname = '/' + urlParts.join('/');

    //extract hash
    locn.pathname = locn.pathname.split('#');
    locn.hash = locn.pathname.length > 1 ? '#' + locn.pathname[1] : '';
    locn.pathname = locn.pathname[0];

    // extract search query
    locn.pathname = locn.pathname.split('?');
    locn.search = locn.pathname.length > 1 ? '?' + locn.pathname[1] : '';
    locn.pathname = locn.pathname[0];

    return locn;
}

// Respond to an error being raised in the javascript
jsErrLog.ErrorTrap = function(msg, file_loc, line_no, col_no) {
	// Is we are debugging on the page then display the error details
	if(jsErrLog.debugMode) {
		jsErrLog.error_msg = "Error found in page: " + file_loc +
		                     "\nat line number:" + line_no +
		                     "\nError Message:" + msg;
		if (jsErrLog.info != "") {
			jsErrLog.error_msg += "\nInformation:" + jsErrLog.info;
		}
		alert("jsErrLog caught an error\n--------------\n" + jsErrLog.error_msg);
	} else {
		jsErrLog.err_i = jsErrLog.err_i + 1;

		// if there are parameters we need to ignore on the querystring strip them off
		var sn = document.URL;
		if (jsErrLog.qsIgnore.length > 0) {
		    var objURL = new Object();
		    // make sure the qsIgnore array is lower case
		    var len = jsErrLog.qsIgnore.length;
			for (var i=0; i<len; i++) {
				jsErrLog.qsIgnore[i] = jsErrLog.qsIgnore[i].toLowerCase();
			}
 
			// Use the String::replace method to iterate over each
			// name-value pair in the query string.
			window.location.search.replace(
			new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
			// For each matched query string pair, add that
			// pair to the URL struct using the pre-equals
			// value as the key.
				function( $0, $1, $2, $3 ){
					// Only if the key is NOT in the ignore list should we pick it up
					if (jsErrLog.qsIgnore.indexOf($1.toLowerCase()) == -1) {
						objURL[ $1 ] = $3;
					}
				}
			);
			var newSearch = "";
			for (var strKey in objURL) {
			    newSearch += newSearch == ("") ? "?" + strKey + "=" + objURL[strKey] : "&" + strKey + "=" + objURL[strKey];
			};

			// Rebuild the new "sn" parameter containing the sanitized version of the querystring
			sn = window.location.protocol + window.location.host + window.location.pathname;
			sn += window.location.search != ("") ? newSearch : "";
			sn += window.location.hash != ("") ? window.location.hash : "";
			
			// now repeat the process for the fileloc
			var fl = parseURL(file_loc);
			objURL = new Object();
			fl.search.replace(
			new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
			// For each matched query string pair, add that
			// pair to the URL struct using the pre-equals
			// value as the key.
				function( $0, $1, $2, $3 ){
					// Only if the key is NOT in the ignore list should we pick it up
					if (jsErrLog.qsIgnore.indexOf($1.toLowerCase()) == -1) {
						objURL[ $1 ] = $3;
					}
				}
			);
			var newFL = "";
			for (var strKey in objURL) {
			    newFL += newFL == ("") ? "?" + strKey + "=" + objURL[strKey] : "&" + strKey + "=" + objURL[strKey];
			};
			if (newFL != "") {
				file_loc = fl.protocol + fl.host + fl.pathname;
				file_loc += fl.search != ("") ? newFL : "";
				file_loc += fl.hash != ("") ? fl.hash : "";
 
			}
		}
		
		// format the data for the request
		var src = jsErrLog.url + "?i=" + jsErrLog.err_i;
		src += "&sn=" + escape(sn);
		src += "&fl=" + escape(file_loc);
		src += "&ln=" + line_no;
		src += "&cn="; 
		src += (typeof col_no === "undefined") ? "" : col_no;
		src += "&ui=" + jsErrLog.guid();
		if (jsErrLog.info != "") {
			src += "&info=" + escape(jsErrLog.info.substr(0, 512));
        }
        src += "&err=" + escape(msg.substr(0, 1792-src.length));

		// check that the fl domain/prefix doesn't match anything in the domainIgnore array
	    var ignore = false;
	    var ignoreFL = file_loc.toLowerCase();
	    len = jsErrLog.domainIgnore.length;
		for (var i=0; i<len; i++) {
			if (ignoreFL.substr(0,jsErrLog.domainIgnore[i].length) == jsErrLog.domainIgnore[i].toLowerCase()) {
				ignore = true;
				break;
			}
		}
		
		if (ignore) {
			// the file_loc matched an item we want to ignore
		    console.log("jsErrLog - report ignored because " + file_loc + " matched domainIgnore list");
		} else {

			// and pass the error details to the Async logging sender		
			// if the jsErrLog.maxRep hasn't tripped
			if ((jsErrLog.maxRep > 0) || (jsErrLog.maxRep = -1)) {
				if (jsErrLog.maxRep > 0) {
				    jsErrLog.maxRep -= 1;
				}
				jsErrLog.appendScript(jsErrLog.err_i, src);
			}
		}
	}
	return true;
}
