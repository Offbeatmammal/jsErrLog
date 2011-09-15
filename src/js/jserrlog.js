///////////////////////////////////////////////////////////////////////////////
//
//  jsErrLog.js   			version 1.1
//
//  Trap javascript errors on a webpage and re-direct them to a remote logging service
//  which can then be used to identify and resolve issues without impacting user experience
//
//  v1.1: add support for jsErrLog.info parameter
//  v1.0: Original
///////////////////////////////////////////////////////////////////////////////

if (!window.jsErrLog)
	window.jsErrLog = { };

// default to debugging off
jsErrLog.debugMode = false;
// default error message to blank
jsErrLog.error_msg = "";
// default the index for the message to 0 in case there is more than one
jsErrLog.err_i = 0;
// default the additional info message to blank
jsErrLog.info = "";

// add the hook to the onError event	
// - first store any existing error handler for the page
jsErrLog.fnPreviousOnErrorHandler = window.onerror; 
// - attach our error handler
window.onerror=function(msg, file_loc, line_no){
	jsErrLog.ErrorTrap(msg, file_loc, line_no);
	if(typeof(jsErrLog.fnPreviousOnErrorHandler) == "function") {
		// process any existing onerror handler 
		jsErrLog.fnPreviousOnErrorHandler(msg, file_loc, line_no);
	}
	return true;
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
	alert("jsErrLog encountered an unexpected error.\n\nSource: " + source + "\nDescription: " + error.description); 
};

jsErrLog.guid = function() { // http://www.ietf.org/rfc/rfc4122.txt section 4.4
	return 'aaaaaaaa-aaaa-4aaa-baaa-aaaaaaaaaaaa'.replace(/[ab]/g, function(ch) { 
		var digit = Math.random()*16|0, newch = ch == 'a' ? digit : (digit&0x3|0x8); 
		return newch.toString(16); 
		}).toUpperCase();
}

// Respond to an error being raised in the javascript
jsErrLog.ErrorTrap = function(msg, file_loc, line_no) {
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
		// format the data for the request
		var src = "http://jserrlog.appspot.com/logger.js?i=" + jsErrLog.err_i;
		src += "&sn=" + escape(document.URL.trim());
		src += "&fl=" + file_loc;
		src += "&ln=" + line_no;
		src += "&err=" + msg.trim().substr(0, 1024);
		src += "&ui=" + jsErrLog.guid();
		if (jsErrLog.info != "") {
			src += "&info=" + escape(jsErrLog.info.trim().substr(0, 512));
		}
		// and pass the error details to the Async logging sender		
		jsErrLog.appendScript(jsErrLog.err_i, src);
		jsErrLog.err_i = jsErrLog.err_i + 1;
	}
	return true;
}
