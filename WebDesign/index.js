AOS.init();
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
};

var search_value = document.getElementById("search_value");
var Result = search_value.value;

function SearchFunction() {
    alert(Result);
};