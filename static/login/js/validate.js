function validate() {
    var name = document.forms["myform"]["Name"];
    var password = document.forms["myform"]["password"];
   

    if (name.value == "") {
        window.alert("Please enter your Userame.");
        name.focus();
        return false;
    }

   
    if (password.value.length < 5) {
        window.alert("Password too short");
        password.focus();
        return false;
    }


    return true;
}