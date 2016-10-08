/**
**Log in script for ventUR
*/


$(document).ready(function() {
	console.log("Script loaded...");
	setup();
});

function setup() {


	document.getElementById("Log In").onclick = function() {
		console.log("You clicked log in.")
	};

	document.getElementById("Sign Up").onclick = function() {
		console.log("You clicked sign up");
	};
}