//**Validate.js**//

var isValidUserName = true;

$(document).ready(function() {
    console.log("Script loaded...");
   $('#form').submit(function(e) {
        console.log("Test");
        if(check(e) && isValidUserName){
            addAcc();
        }
    });
   $('#Username').blur(function() {

        $uname = $('#Username').val();
        if($uname.length > 0) {
            

          $.ajax({
              url: '../cgi-bin/checkuser.py',

             data: {
                 username: $uname 
            },
                
            type: "post",
            
            dataType: "json",
            
            success: function(data) {
                isValidUserName = false;
                $('#checkOK').empty();
                $('#checkBad').html("That username is already taken.")
            },
            
            error: function() {
                isValidUserName = true;
                $('#checkOK').html("Your chosen username is available!");
                $('#checkBad').empty();
            }
            
    
                
            
          });
      }

    });
    
});


var check = function(e){
    var $pass = $('#Password').val();
    var $checkPass = $('#Re-Password').val();
    if ($pass != $checkPass){
        alert("Your passwords do not match. Please try again.")
        $('submit').empty();
        e.preventDefault()
        return false;
    } else {
        return true;
    }
    
}

//var addAcc = function() {

  //  $.ajax() {
      //  url: 
    //}

//}