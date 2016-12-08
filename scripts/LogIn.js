//LogIn.js//

var isValid = false
var isLoggedIn = false
$(document).ready(function() {
	var test = Cookies.get('name');
	if (test != undefined) {
		console.log("here")
		window.location.href = "FirstLogin-Page.html"
	}
	$('#Password').keyup(function(e) {
		$uname = $('#Username').val();
        if($uname.length > 0) {

        	$.ajax({
			url: '../cgi-bin/test.py/',

			data: {
				Username: $("#Username").val(),
				Password: $("#Password").val()
			},

			method: "post",

			dataType: "json",

			success: function() {
			
				isValid = true
			},

			error: function() {
				
				isValid = false

			}
			})
        }

		
		
	});

	$('#form').submit(function(e) {
		//e.preventDefault();
		check(e);
	});


});

var check = function(e) {
	if(!isValid) {
		alert("Sorry, we couldn't find an account with those credentials. Please try again");
		e.preventDefault()
		
	} else {
		Cookies.set('name', $("#Username").val(), {expires: 7});
		//window.location.href = "FirstLogin-Page.html"
	}


}