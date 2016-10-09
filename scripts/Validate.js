//**Validate.js**//

$(document).ready(function() {
    console.log("Script loaded...");
   $('#form').submit(function(e) {
        console.log("Test");
        check(e);
    });
});


var check = function(e){
    var $pass = $('#Password').val();
    var $checkPass = $('#Re-Password').val();
    if ($pass != $checkPass){
        alert("Your passwords do not match. Please try again.")
        $('submit').empty();
        e.preventDefault()
    }
    
}