$(document).ready(function() {
	
	$("#LogOut").click(function() {
		Cookies.remove("name");
		window.location.href = "index.html"
	})

	$('#form').submit(function (e) {
		$.ajax({
			url: "../cgi-bin/createevent.py",

			data: {
				Username: Cookies.get("name"),
				EventName: $('#EventName').val(),
				StartTime: $('#StartTime').val(),
				EndTime: $('#EndTime').val(),
				Location: $('#Location').val(),
				Description: $('#Description').val()

			},

			type: "post",

			dataType: "json",

			success: function() {
				alert("event added succesfully");
			},

			error: function(e) {
				e.preventDefault();
				alert("Oops!");
			}


		})
	});



});