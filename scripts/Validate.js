//**Validate.js**//

var isValidUserName = true;

$(document).ready(function() {
    console.log("Script loaded...");
    console.log("test");
   $('#form').submit(function(e) {
        console.log("Test");
        check(e);
         
    });
   $('#Username').blur(function() {

        $uname = $('#Username').val();
        console.log($uname);
        if($uname.length > 0) {
            

          $.ajax({
              url: '../cgi-bin/checkuser.py',

             data: {
                 username: $uname 
            },
                
            type: "post",
            
            dataType: "json",
            
            success: function(data) {
                console.log("success");
                isValidUserName = false;
                $('#checkOK').empty();
                $('#checkBad').html("That username is already taken.")
            },
            
            error: function() {
                console.log("failure");
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
        if (isValidUserName) {
            return true;
        } else {
            alert("Sorry; your chosen username has been taken.");
            e.preventDefault();
            return false;
        }
        
    }
    
}

