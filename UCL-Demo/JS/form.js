var ButtonXML = document.querySelector(".buttonXML");
var divXML = document.querySelector(".button-XML");

ButtonXML.addEventListener('click', function(event){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() 
    {
        divXML.innerHTML = this.responseText;
    };
    xhttp.open("GET", "/HTML/date.txt", true);
    xhttp.send();
  })
