//**Validate.js**//

$(document).ready(function() {
    console.log("Script loaded...");
   $('#form').submit(function(e) {
        console.log("Test");
        if(check(e)){
            addAcc();
        }
    });
   $('#Username').blur(function() {

        $uname = $('#Username').val();
        if($uname.length > 0) {
            

          $.ajax() {
              url: '../cgi-bin/checkuser.py',

             data: {
                 username: $uname 
            },
                
            type: "post",
            
            dataType: "json",
            
            success: function(data) {
                
            }
                
            
          }
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