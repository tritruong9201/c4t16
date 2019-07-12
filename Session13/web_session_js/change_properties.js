// function startClick() {
//     console.log("Button clicked");
// };

var btn = document.getElementById("btn");
console.log(btn);
btn.textContent = "Stop";
btn.addEventListener("click", function(e) {
    console.log("Button clicked");
});

var search = document.getElementById("search_bar");
search.value = "";
search.style.backgroundColor = "Blue";

var menu = document.getElementById("menu");
var newLi = document.createElement("li");
newLi.textContent = "Fries";
menu.appendChild(newLi);

var liList = menu.getElementsByTagName("li");
var firstLi = liList[0];
firstLi.remove();

// menu.textContent = "";

var deleteButtons = document.getElementsByClassName("btn_delete");
console.log(deleteButtons);

for (i=0; i<deleteButtons.length; i++) {
    var deleteButton = deleteButtons[i];
    deleteButton.addEventListener("click", function(e) {
        console.log("Delete clicked");
        // console.log(e.target);
        var btn = e.target;
        var div = btn.parentNode;
        console.log(div);
        div.remove();
});
};