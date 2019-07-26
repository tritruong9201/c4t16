var email_value = document.getElementById("email_value");
var password_value = document.getElementById("password_value");

function LogInFunction() {
    if (email_value.value == "trtr") {
        if (password_value.value == "minh") {
            alert("Correct");
        } else {
            alert("Wrong");
        };
    } else {
        alert("Wrong");
    };
};