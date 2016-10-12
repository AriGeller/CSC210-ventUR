//LogIn.js//

$(document).ready(function() {
	console.log("Script loaded...");
	$('#form').submit(function(e) {
		$uname = $("#Username").val();
		$pass = $("#Password").val();

		if(!check(e)) {
			e.preventDefault();
			return false;
		}

	});
});

var check = function(e) {

	$.ajax({
		url: "../cgi-bin/login.py",

		data: {
			Username: $uname,
			Password: $pass
		},

		method: "post",

		datatype: "json",

		success: function() {
			return true;
		},

		error: function() {
			alert("Sorry, we couldn't find an account with those credentials. Please try again");
			e.preventDefault();
			return false;

		}
	})


}