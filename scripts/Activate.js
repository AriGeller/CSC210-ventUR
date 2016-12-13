/**
*AJAX file for the main paige
**/

var isValidNewFriend = false;
var username;

$(function () {
	$('#dialog').dialog({
		autoOpen: false,
		show: {
			effect: "clip",
			duration: 150
		},
		hide: {
			effect: "fade",
			duration: 250
		}
	});
});



$(document).ready(function() {
	username = Cookies.get("name");
	updateList();
	updateEvents();
	updateFriendEvents();

	$("#delete").click(function() {
		$.ajax({
			url: '../cgi-bin/deleteaccount.py',

			data: {
				Username: username
			},

			type: "post",

			dataType: "json",

			success: function(data) {
				Cookies.remove("name");
				window.location.href = "index.html";
			},

			error: function() {
				alert("Couldn't delete account");
			}
		})
	})
	
    
	$("#LogOut").click(function() {
		Cookies.remove("name");
		window.location.href = "index.html"
	})
    displayWelcome(username);
    var $new
    $('#toAdd').keyup(function() {
    	$new = $('#toAdd').val()
		$.ajax({
     		url: '../cgi-bin/checkuser.py',

        	data: {
           		username: $new 
        	},
                
        	type: "post",
            
        	dataType: "json",
            
        	success: function(data) {
        	
            	isValidNewFriend = true;

        	},
            
        	error: function() {
          
             	isValidNewFriend = false
        	}
            
    	});
	})

	$('#add').submit(function(e) {
		e.preventDefault();
		$('#toAdd').val('');
		if (isValidNewFriend){
			$.ajax({
	        	url: '../cgi-bin/addfriendreal.py',

	        	data: {
	        		username: username,
	        		friend: $new 

	        	},
	                
	        	type: "post",
	            
	        	dataType: "json",
	            
	        	success: function() {
	        		
	        		updateList();
	        		updateFriendEvents();
	       		},
	            
	        	error: function() {
	        		alert("Oops! Something went wrong!")
	        	}

        	});
		
		} else {
			alert("Sorry, that user doesn't exist. Please try again.")
		}
	})

});





var displayWelcome = function(username) {
    $('#welcome').html('Hello, ' + username + '. Are You Ready To Go On An Adventure?');
}


function updateList() {
	$('#accepted').empty()
	$.ajax({
		url: "../cgi-bin/getfriends.py",

		data: {
			username: username
		},

		type: "post",

		dataType: "json",

		success: function(data) {
			for (var i = 0; i < data.friends.length; i++){
				$('#accepted').append("<li>" + data.friends[i] + "</li>")
			}
		
		},

		error: function() {
			
		} 
	})
}

function updateEvents() {
	$('#CurrentEvents').empty()
	$.ajax({
		url: "../cgi-bin/getevents.py",

		data: {
			Username: username
		},

		type: "post",

		dataType: "json",

		success: function(data) {

			for (var i = 0; data.events[i] != null; i++) {
				$.ajax({
					url: "../cgi-bin/geteventinfo.py",

					data: {
						EventID: data.events[i][0]
					},

					type: "post",

					dataType: "json",

					success: function(data) {

						var start = data["startime"].split(" ");
						var startDate = start[0];
						var startTime = start[1] + " " + start[2];
						var end = data["endtime"].split(" ");
						var endDate = end[0];
						var endTime = end[1] + " " + end[2];
						var id = data['ID'];
						
					
						$('#CurrentEvents').append("<li>" + data["name"] + " at " + data["location"] + " starts at " + startTime +  " on " + startDate + "</li>")
						var $button = $("<button type='button'>Get info</button>");
						$button.click(function() {
							$("#dialog").empty();
							$("#dialog").append("<p> Event: " + data["name"] + "<br> Location: " + data["location"] + "<br> Starts At: " + data["startime"] + "<br> Ends At: " + data["endtime"] + "<br> Description: " + data["description"] + "<br> Guest List: " + data["guests"] + "</p>");
							$("#dialog").dialog("open");
						});

						
						$('#CurrentEvents').append($button);

						var $delButton = $("<button type='button'>Delete</button>");
						$delButton.click(function() {
							$.ajax({
								url: "../cgi-bin/deleteevent.py",

								data: {
									EventID: id
								},

								type: "post",

								dataType: "json",

								success: function(data) {
									window.location.href = "./FirstLogin-Page.html";
								},

								error: function() {
									alert("Couldn't delete event");
								}
							})
						});

						$('#CurrentEvents').append($delButton);

					},

					error: function() {
						alert("Couldn't get event info");
					}
				})
				
			}
			 			
			
		}, 

		error: function() {
			alert("Couldn't get events");
		}


	})
	
}

function updateFriendEvents() {
	$('#FriendEvents').empty()
	$.ajax({
		url: "../cgi-bin/getfriendsevents.py",

		data: {
			Username: username
		},

		type: "post",

		dataType: "json",

		success: function(data) {

			for (var i = 0; data.events[i] != null; i++) {

				$.ajax({
					url: "../cgi-bin/geteventinfo.py",

					data: {
						EventID: data.events[i]
					},

					type: "post",

					dataType: "json",

					success: function(data) {

						var start = data["startime"].split(" ");
						var startDate = start[0];
						var startTime = start[1] + " " + start[2];
						var end = data["endtime"].split(" ");
						var endDate = end[0];
						var endTime = end[1] + " " + end[2];
						var id = data["ID"];
						var joined = false;
					
						$('#FriendEvents').append("<li>" + data["name"] + " at " + data["location"] + " starts at " + startTime + " on " + startDate + "</li>");
						var $button = $("<button type='button'>Get info</button>");
						$button.click(function() {
							$("#dialog").empty();
							$("#dialog").append("<p> Event: " + data["name"] + "<br> Creator: " + data["owner"] + "<br> Location: " + data["location"] + "<br> Starts At: " + data["startime"] + "<br> Ends At: " + data["endtime"] + "<br> Description: " + data["description"] + "<br> Guest List: " + data["guests"] + "</p>");
							$("#dialog").dialog("open");
						});



						
						$('#FriendEvents').append($button);
						for (var user of data['guests']) {
							if (user == username) {
								joined = true;
							}
						}
						

						if (!joined) {
							var $joinButton = $("<button type='button'>Join</button>");
							$joinButton.click(function() {
								$.ajax({
									url: "../cgi-bin/joinevent.py",

									data: {
										eventid: id,
										username: username

									},

									type: "post",

									dataType: "json",

									success: function(data) {
										window.location.href = "./FirstLogin-Page.html"
									},

									error: function() {
									}
								})
							});

							$('#FriendEvents').append($joinButton);

						} else {
							var $leaveButton = $("<button type='button'>Leave</button>");
							$leaveButton.click(function() {
								$.ajax({
									url: "../cgi-bin/leaveevent.py",

									data: {
										eventid: id,
										username: username

									},

									type: "post",

									dataType: "json",

									success: function(data) {
										window.location.href = "./FirstLogin-Page.html";
									},

									error: function() {
										alert("oops");
									}
								})
							});

							$('#FriendEvents').append($leaveButton);
						}
						

					},

					error: function() {
						alert("Couldn't get event info");
					}
				})
				
			}
			 			
			
		}, 

		error: function() {
			alert("Couldn't get events");
		}


	})
}
