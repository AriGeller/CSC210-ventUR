var start;
var end;

$(document).ready(function() {
	

	function onChangeStart() {
		 $("#StartTime").val(kendo.toString(this.value(), 'g'));
		 start = kendo.toString(this.value(), 'g');
	}

	function onChangeEnd() {
		$("#EndTime").val(kendo.toString(this.value(), 'g'));
		end = kendo.toString(this.value(), 'g');
	}

	$('#StartTime').kendoDateTimePicker({
		value: new Date(),
		change: onChangeStart
	});
	$('#EndTime').kendoDateTimePicker({
		value: new Date(),
		change: onChangeEnd
	});
	
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
			},

			error: function(e) {
				e.preventDefault();
			}


		})
	});



});