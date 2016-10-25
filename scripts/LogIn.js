//LogIn.js//

$(document).ready(function() {
	console.log("Script loaded...");
	$('#form').submit(function(e) {

		if(!check(e)) {
			e.preventDefault();
			return false;
		}

	});
});

var check = function(e) {

	$.ajax({
		url: '../cgi-bin/test.py/',

		data: {
			Username: $("#Username").val(),
			Password: $("#Password").val()
		},

		method: "post",

		dataType: "json",

		success: function() {
			Cookies.set('name', $("#Username").val())
			return true;
		},

		error: function() {
			alert("Sorry, we couldn't find an account with those credentials. Please try again");
			e.preventDefault();
			return false;

		}
	})


}