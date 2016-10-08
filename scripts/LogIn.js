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
		var username = $('#Username').val();
		if (username == "") {
            alert("Please enter a valid username.")
        } else {
            console.log(username);
        }
        var password = $('#Password').val();
        if (password.length < 4 || password.length > 15) {
            alert("Please enter a valid password. A valid password has between 4 and 15 characters.")
        }
	};

	document.getElementById("Sign Up").onclick = function() {
		console.log("You clicked sign up");

	};
}