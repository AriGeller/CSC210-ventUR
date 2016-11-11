$(document).ready(function() {
	$('#form').submit(function e) {
		$.ajax({
			url: ,

			data: {
				username: Cookies.get("name"),
				name: $('#EventName').val(),
				start: $('#StartTime').val(),
				end: $('#EndTime').val(),
				location: $('#location').val(),
				description: $('#Description').val()

			},

			type: "post",

			dataType: ,

			success: function() {

			},

			error: function(e) {
				e.preventDefault();
				alert("Oops!");
			}


		})
	}



});