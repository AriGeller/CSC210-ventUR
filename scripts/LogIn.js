//LogIn.js//

var isValid = false

$(document).ready(function() {
	$('#Password').keyup(function() {
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
		check(e);
		
	});
});

var check = function(e) {
	if(!isValid) {
		alert("Sorry, we couldn't find an account with those credentials. Please try again");
		e.preventDefault()
	} else {
		Cookies.set('name', $("#Username").val())
	}


}