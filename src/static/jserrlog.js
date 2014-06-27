///////////////////////////////////////////////////////////////////////////////
//
//  jsErrLog.js         version 1.4.2
//
//  Trap javascript errors on a webpage and re-direct them to a remote logging service
//  which can then be used to identify and resolve issues without impacting user experience
//
//  v1.4.2: domainBlacklist adds prefix ignore on file location
//  v1.4.1: added support for colNo in browsers that support it (IE10, Chrome30)
//  v1.4.0: limit initialization to one instance, escape FL and ERR parameter, limit reports sent
//  v1.3.0: add support for jsErrLog.qsignore parameter
//  v1.2.0: add support for jsErrLog.url parameter
//  v1.1.0: add support for jsErrLog.info parameter
//  v1.0.0: Original
///////////////////////////////////////////////////////////////////////////////

(function(window) {

	if (window.jsErrLog) return;

	//Support for Array.indexOf in older browsers IE 8 & lower | < ECMAScript 5th Edition
	if( !Array.prototype.indexOf )
	{
		Array.prototype.indexOf = function( element ){
            for( var i=0, ilen=this.length; i<ilen; i++ ){
            	if( this[i] == element ) return i;
            }
            return -1;
		};        
	}
	
	window.jsErrLog = {}; //Global
	var jsErrUtils	= {}; //Local

	//jsErrUtils definitions

	// Generate guid
	jsErrUtils.generateGuid = function() {
		return 'aaaaaaaa-aaaa-4aaa-baaa-aaaaaaaaaaaa'.replace(/[ab]/g, function(ch) { 
			var digit = Math.random()*16|0, newch = ch == 'a' ? digit : (digit&0x3|0x8); 
			return newch.toString(16); 
		}).toUpperCase();
	};
	
	// Needed to break the URL up if we want to ignore parameters
	jsErrUtils.parseURL = function(url) {
	
	    // save the unmodified url to "href" property so
	    // the returned object matches the built-in location object
	    var locn = { 'href' : url };
	
	    // split the URL components
	    var urlParts = url.replace('//', '/').split('/');
	
	    //store the protocol and host
	    locn.protocol = urlParts[0];
	    
	    if (urlParts.length > 1 ) {
	    
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
	
	    }
	    
	    return locn;
	}
	
	jsErrUtils.matchDomains = function( loc, domains ) {
		return (new RegExp( "(" + domains.join('|').replace(/\./g,'\\.').replace(/\*/g,'\\w+') + ")" )).test( loc );		
	}
	
	jsErrUtils.stripQueries = function( loc ) {
		var queries = {};
		// Use the String::replace method to iterate over each
		// name-value pair in the query string.
		loc.search.replace(
		new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
		// For each matched query string pair, add that
		// pair to the URL struct using the pre-equals
		// value as the key.
			function( $0, $1, $2, $3 ){
				// Only if the key is NOT in the ignore list should we pick it up
				if (jsErrLog.qsIgnore.indexOf($1.toLowerCase()) == -1) {
					queries[ $1 ] = $3;
				}
			}
		);
		
		var search = "";
		for (var key in queries) {
			search += ( search.length === 0 ? "?" : "&" ) + key + "=" + queries[key];
		};

		// Rebuild the url
		return 	( loc.protocol + loc.host + loc.pathname )
			+	( loc.search != ("") ? search : "" )
			+	( loc.hash != ("") ? loc.hash : "" );
	}
	
	//jsErrLog definitions
	
	// default to debugging off
	jsErrLog.debugMode = false;
	// default the index for the message to 0 in case there is more than one
	jsErrLog.err_i = 0;
	// default the additional info message to blank
	jsErrLog.info = "";
	// default the URL to the appspot service
	jsErrLog.url = "http://jserrlog.appspot.com/logger.js";
	// default the qsIgnore to nothing (ie pass everything on the querystring)
	jsErrLog.qsIgnore = new Array();
	// default ignored domains to nothing
	jsErrLog.domainBlacklist = new Array();
	// whitelist script domains which can trigger errors
	jsErrLog.domainWhitelist = new Array();
	// max number of reports sent from a page (defaults to 10, false allows infinite)
	jsErrLog.maxRep = 10;
	// set to false to log errors and also pass them through to the default handler
	// (and see them in the browser's error console)
	jsErrLog.trapErrors = false;
	// log errrors to browser console
	jsErrLog.logToConsole = false;
	// Skip CrossOrigin errors. These supply no helpful debugging info, and because
	// of JavaScript injection from a (possibly ill-behaved) browser plugin, these can't
	// be controlled from the app side.
	jsErrLog.ignoreCrossOriginErrors = false;
	// Use a unique guid for every error
	// default every error on 1 page uses the same guid
	jsErrLog.uniqueGuid = true;
	// Generate guid for page session
	jsErrLog.guid = jsErrUtils.generateGuid();
	
	// used internally for testing to know if test succeeded or not
	jsErrLog._had_errors = false;

	// add the hook to the onError event
	// - first store any existing error handler for the page
	jsErrLog.fnPreviousOnErrorHandler = window.onerror; 
	// - attach our error handler
	window.onerror = function(msg, file_loc, line_no, col_no){
		jsErrLog.errorTrap(msg, file_loc, line_no, col_no);
		if(typeof(jsErrLog.fnPreviousOnErrorHandler) == "function") {
			// process any existing onerror handler 
			jsErrLog.fnPreviousOnErrorHandler(msg, file_loc, line_no, col_no);
		}
        return jsErrLog.trapErrors;
	}

	//Append the script to head, calling your error logger
	jsErrLog.appendScript = function(index, src) {
		try {
			var script 	= document.createElement("script"),
				head 	= document.getElementsByTagName("head")[0];
				
			script.id = "script" + index;
			script.src = src;
			script.type = "text/javascript";
			
			head.appendChild(script);
		} catch (e) {
			jsErrLog.errorHandler("appendScript", e);
		}
	};
	
	//Hide the log call, this won't remove the Javascript completely but it'll remove it from the HTML
	jsErrLog.removeScript = function(index) {
		try {
			var script	= document.getElementById("script" + index),
				head 	= document.getElementsByTagName("head")[0];
			head.removeChild(script);
		} catch (e) {
			jsErrLog.errorHandler("removeScript", e);
		}
	};
	
	//Error handler to catch the removeScript & appendScript errors
	jsErrLog.errorHandler = function(source, error) {
		jsErrLog._had_errors = true;
		
		var message = "jsErrLog encountered an unexpected error.\n\nSource: " + source + "\nDescription: " + error.description;
		if (jsErrLog.debugMode) alert( message );
		else					console.log( message );
	};
	
	// Respond to an error being raised in the javascript
	jsErrLog.errorTrap = function (msg, file_loc, line_no, col_no) {
	    
		//When a whitelist exists only trigger errors from script coming from those domains
		if (jsErrLog.domainWhitelist.length > 0) {	
			if (jsErrUtils.matchDomains(file_loc,jsErrLog.domainWhitelist) === false){
				console.log("jsErrLog - report ignored because " + file_loc + " did not match the whitelist" );
				return;
			}
		}
		
		if (jsErrLog.domainBlacklist.length > 0) {	
			if (jsErrUtils.matchDomains(file_loc,jsErrLog.domainBlacklist) === true){
				console.log("jsErrLog - report ignored because " + file_loc + " matched the blacklist" );
				return;
			}
		}
		
		if (jsErrLog.ignoreCrossOriginErrors && msg == "Script Error" && line_no == "0") {
		    console.log("jsErrLog - cross origin script error ignored because no additional error info supplied.");
		    return;
		}
		
		var error_msg =	"Error found in page: " + file_loc +
	                    "\nat line number:" + line_no +
	                    "\nError Message:" + msg;
		
	    if (jsErrLog.info != "") {
	        error_msg += "\nInformation:" + jsErrLog.info;
	    }
	    
	    if (jsErrLog.logToConsole) {
	        console.log(error_msg);
	    }
	    
		// Is we are debugging on the page then display the error details
		if (jsErrLog.debugMode) {
			alert("jsErrLog caught an error\n--------------\n" + error_msg);
		} else {
			jsErrLog.err_i += 1;
	
			// if there are parameters we need to ignore on the querystring strip them off
			var sn = document.URL;
			if (jsErrLog.qsIgnore.length > 0) {
			    
			    // make sure the qsIgnore array is lower case
				for (var i=0,ilen=jsErrLog.qsIgnore.length; i<ilen; i++) {
					jsErrLog.qsIgnore[i] = jsErrLog.qsIgnore[i].toLowerCase();
				}
	 
				sn = jsErrUtils.stripQueries( window.location );
	
				// now repeat the process for the fileloc, if it exists 
				// (in some cases, like an explicitly thrown exception, fileloc might be empty)
				if (typeof file_loc !== "undefined" && file_loc.length > 1) {
					
					file_loc = jsErrUtils.stripQueries( jsErrUtils.parseURL(file_loc) );
					
				}
			}
			
			// format the data for the request
			var src = jsErrLog.url + "?i=" + jsErrLog.err_i;
			src += "&sn=" + escape(sn);
			src += "&fl=" + escape(file_loc);
			src += "&ln=" + line_no;
			src += "&cn="; 
			src += (typeof col_no === "undefined") ? "" : col_no;
			src += "&ui=" + ( jsErrLog.uniqueGuid ? jsErrUtils.generateGuid() : jsErrLog.guid );
			if (jsErrLog.info != "") {
				src += "&info=" + escape(jsErrLog.info.substr(0, 256));//You should be able to give enough information with 256 chars
	        }
	        src += "&err=";
	        // Keep the path length under 2000 chars which is advised for URL's in browsers 
	        src += escape(msg.substr(0, 1999-src.length)); 
	        
			// and pass the error details to the Async logging sender		
			// if the jsErrLog.maxRep hasn't tripped
			if (jsErrLog.maxRep > 0 || jsErrLog.maxRep === false) {
				if (jsErrLog.maxRep > 0) {
				    jsErrLog.maxRep -= 1;
				}
				jsErrLog.appendScript(jsErrLog.err_i, src);
			}
		}
		return true;
	}

})(window);