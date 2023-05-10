function validate() {
    var name = document.forms["myform"]["Giver_Name"];
    var Aaddhar = document.forms["myform"]["aaddhar"];
    var Address = document.forms["myform"]["address"];
    var Mobno = document.forms["myform"]["mobno"];
    var Native = document.forms["myform"]["native"];
    var Nationality = document.forms["myform"]["nationality"];
    var Car = document.forms["myform"]["car_type"];
    var Upload = document.forms['myform']['uploadfile'];
    var password = document.forms["myform"]["password"];
   

    if (name.value == "") {
        window.alert("Please enter your Name.");
        name.focus();
        return false;
    }

    if (Aaddhar.value == "") {
        window.alert("Please enter your Aaddhar Number.");
        Aaddhar.focus();
        return false;
    }
    if (Aaddhar.value.length !=12 ) {
        window.alert("Please enter your valid Aaddhar Number.");
        Aaddhar.focus();
        return false;
    }

    if (Address.value == "") {
        window.alert("Please enter Address.");
        Address.focus();
        return false;
    }

    if (Mobno.value == "") {
        window.alert("Please enter your Mobile number.");
        Mobno.focus();
        return false;
    }
    if (Mobno.value.length!=10) {
        window.alert("Please enter valid Mobile number.");
        Mobno.focus();
        return false;
    }
    if (Native.value == "") {
        window.alert("Please enter Native Place.");
        Native.focus();
        return false;
    }
    if (Nationality.selectedIndex < 1) {
        alert("Please enter your Nationality.");
        Nationality.focus();
        return false;
    }
    if (Car.selectedIndex < 1) {
        alert("Please enter your Car Type.");
        Car.focus();
        return false;
    }
    if (Upload.value =="") {
        alert("Please upload your image");
        Upload.focus();
        return false;
    }
    if (password.value == "") {
        window.alert("Please enter your password");
        password.focus();
        return false;
    }

    if (password.value.length < 5) {
        window.alert("Password too short");
        password.focus();
        return false;
    }


    return true;
}