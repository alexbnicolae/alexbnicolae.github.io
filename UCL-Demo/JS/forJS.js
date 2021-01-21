// Add the Date and the Time on the page automatically

var time = document.querySelector(".time");

var MyTime = setInterval(TheDate, 1000);

function TheDate(){
    var d = new Date();
    var date = d.toLocaleString();
    time.innerHTML = date;
}

//Add comments

var ButtonReview = document.querySelector(".button-review");
var Comments = document.querySelector(".comments");
var TextFromTextarea = document.getElementById("review");
var c;

TextFromTextarea.addEventListener('keyup', function(event){
    TextFromTextarea.innerHTML =  event.target.value;
    c=0;
})


ButtonReview.addEventListener('click', function(event){  
    if(c==0)
    {   
        var d = new Date();
        var date = d.toLocaleString();
        Comments.innerHTML = Comments.innerHTML + "<div class=one-comment>" + TextFromTextarea.innerHTML + "<br> <div class=date-edit> The comment was added at: " + date + "</div>" + "</div>";
        console.log(Comments.innerHTML)
        localStorage.nr = Comments.innerHTML;
        TextFromTextarea.innerHTML ="";
        c=1;
    }
})


var ButtonLS = document.querySelector(".lastLS")
var LC = document.querySelector(".lastCom");

ButtonLS.addEventListener('click', function(event){
    event.preventDefault();
    LC.innerHTML = localStorage.nr;
})

var divRiview = document.querySelector(".div-review");
var ReviewStyle = document.querySelector(".review-style");

divRiview.addEventListener('click', function(event){
    if(window.getComputedStyle(divRiview, null).getPropertyValue("background-color").toLowerCase() == "rgba(0, 255, 255, 0.5)"){
        this.style.backgroundColor = "rgba(0, 0, 0, 0)";
    }
    else if(window.getComputedStyle(divRiview, null).getPropertyValue("background-color").toLowerCase() == "rgba(0, 0, 0, 0)") {
        this.style.backgroundColor = "rgba(0, 255, 255, 0.5)";   
    }
}, false)

ReviewStyle.addEventListener('click', function(event){
    if(window.getComputedStyle(ReviewStyle, null).getPropertyValue("background-color").toLowerCase() == "rgba(0, 0, 0, 0)"){
        this.style.backgroundColor = "rgba(255, 0, 0, 1)";
    }
    else
    {
        this.style.backgroundColor = "rgba(0, 0, 0, 0)";
    }
    event.stopPropagation();
    

},true)

//Stop the time!!!

var ButtonStopTime = document.querySelector(".stop-time");
var ButtonStartTime = document.querySelector(".start-time");

ButtonStopTime.addEventListener('click', function(event){
    clearInterval(MyTime);
    this.style.display = "none";
    ButtonStartTime.style.display = "initial";
});

ButtonStartTime.addEventListener('click', function(event){
    MyTime = setInterval(TheDate, 1000);
    this.style.display = "none";
    ButtonStopTime.style.display = "initial";
})

