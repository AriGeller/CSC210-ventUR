/**
*AJAX file for the main paige
**/

$(document).ready(function() {
    console.log("Script loaded...");
    var username = getCookie("Username");
    displayWelcome();
});

var getUserInfo = function(uname) {
    
    
    
    $.ajax({
        url: '../cgi-bin/'
        
    });
    
};

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
};

var displayWelcome = function() {
    $('#welcome').html('Hello, ' + username + '. Are You Ready To Go On An Adventure?');
}

