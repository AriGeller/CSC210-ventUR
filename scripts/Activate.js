/**
*AJAX file for the main paige
**/

$(document).ready(function() {
    console.log("Script loaded...");
    var username = Cookies.get("name");
    displayWelcome(username);
});

var getUserInfo = function(uname) {
    
    
    
    $.ajax({
        url: '../cgi-bin/'
        
    });
    
};


var displayWelcome = function(username) {
    $('#welcome').html('Hello, ' + username + '. Are You Ready To Go On An Adventure?');
}

