var index;
var score = 0;
function generateColor() {
    var r = Math.floor(Math.random()*226);
    var g = Math.floor(Math.random()*226);
    var b = Math.floor(Math.random()*226);

    var rightColorString = `rgb(${r}, ${g}, ${b})`

    var colorStringShow = document.getElementById("color_string");
    colorStringShow.textContent = rightColorString;

    var ballContainer = document.getElementById("ball_container");
    var ballList = ballContainer.getElementsByClassName("ball");

    index = Math.floor(Math.random()*3)
    ballList[index].style.backgroundColor = rightColorString;

    for (i=0;i<ballList.length;i++) {
        if (i != index){
            var errorIndex1 = Math.floor(Math.random()*100)+50;
            var x = Math.random();
            if (x>0.5) {
                errorIndex1 = -errorIndex1;
            };

            var errorIndex2 = Math.floor(Math.random()*100)+50;
            var x = Math.random();
            if (x>0.5) {
                errorIndex2 = -errorIndex2;
            };

            var errorIndex3 = Math.floor(Math.random()*100)+50;
            var x = Math.random();
            if (x>0.5) {
                errorIndex3 = -errorIndex3;
            };

            var wrongColorString = `rgb(${r+errorIndex1}, ${g+errorIndex2}, ${b+errorIndex3})`
            ballList[i].style.backgroundColor = wrongColorString;
        };
    };
};

function setupEvent() {
    var ballContainerEl = document.getElementById("ball_container");
    var ballEls = ballContainerEl.getElementsByClassName("ball");
    for (i=0; i<ballEls.length; i++) {
        ballEls[i].addEventListener("click", function(e) {
            var ball = e.target;
            var ball_index = ball.getAttribute("index");
            if (ball_index == index) {
                score+=1;
            } else {
                score = 0;
            };
            var scoreRemember = document.getElementById("score");
            scoreRemember.textContent = `SCORE: ${score}`;
            generateColor();
        });
    };
};

generateColor();
setupEvent();