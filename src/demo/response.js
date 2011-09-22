jsErrLog.removeScript(jsErrLog.err_i); // jsErrRpt

function changeClass(element, newClass) {
  // borrowed from http://www.webdeveloper.com/forum/showthread.php?t=134282
	element.setAttribute("class", newClass); //For Most Browsers
	element.setAttribute("className", newClass); //For IE; harmless to other browsers.
}

var element = document.getElementById('testbox');
if (!jsErrLog._had_errors) {
  changeClass(element, 'alert-message block-message success');
  element.innerHTML = '<strong>Things worked out great!</strong> The test passed joyously unless you got an alert box. If your browser is not in the <a href="../../README.markdown">README</a> file, please consider filing an <a href="">issue on Github</a> to notify the developers that jsErrLog works for your browser!';
} else {
  changeClass(element, 'alert-message block-message error');
  element.innerHTML = '<strong>Something went wrong :(.</strong> An error occurred when the script was being executed. If your browser is not in the <a href="../../README.markdown">README</a> file, please consider filing an <a href="">issue on Github</a> to notify the developers that jsErrLog does not work in your browser!';
}

