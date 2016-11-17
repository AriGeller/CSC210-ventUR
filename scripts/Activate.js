/**
*AJAX file for the main paige
**/

var isValidNewFriend = false;
var username;
$(document).ready(function() {
	username = Cookies.get("name");
	updateList();
	updateEvents();
	
    
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
		e.preventDefault()
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
	        		
	        		updateList()
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

			for (var i = 0; i < 3; i++) {
				if (data.events[i] != null) {
					console.log(data.events[i][0])
					$.ajax({
						url: "../cgi-bin/geteventinfo.py",

						data: {
							EventID: data.events[i][0]
						},

						type: "post",

						dataType: "json",

						success: function(data) {
							console.log(data["name"]);
							$('#CurrentEvents').append("<li>" + data["name"] + " at " + data["location"] + " starts at " + data["startime"] + "</li>")
						},

						error: function() {
							alert("Couldn't get event info");
						}
					})
				}
			}
			 			
			
		}, 

		error: function() {
			alert("Couldn't get events");
		}


	})
	
}
