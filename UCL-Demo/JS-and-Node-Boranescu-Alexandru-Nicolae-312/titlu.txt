// Find the InnerText from h1 with DOM proprities

var BodyChildren = document.body.children;
//console.log(BodyChildren[0]);
for (var i=0; i<BodyChildren.length; i++)
{
    if(BodyChildren[i].tagName.toLowerCase() == "header")
    {
        //console.log(BodyChildren[i]);
        var HeaderChildren = BodyChildren[i].children;
        //console.log(HeaderChildren);
    }
}

for (var i=0; i<HeaderChildren.length; i++)
{
    if(HeaderChildren[i].tagName.toLowerCase() == "section")
    {
        var SectionChildren = HeaderChildren[i].children;
        //console.log(SectionChildren);
    }
}

for (var i=0; i<SectionChildren.length; i++)
{
    if(SectionChildren[i].tagName.toLowerCase() == "div")
    {
        var DivChildren = SectionChildren[i].children;
        //console.log(DivChildren);
    }
}

for(var i = 0; i<DivChildren.length; i++)
{
    if(DivChildren[i].tagName.toLowerCase() == "h1")
    {
        var H1Text= DivChildren[i].innerText; // We have found the InnerText
        var H1 = DivChildren[i];
        //console.log(H1Text);
    }
}

var letters = [];

for(var i=0; i<H1Text.length; i++)
{
    letters.push(H1Text[i]);
}
//console.log(letters);

// console.log(H1);

H1.innerText =" ";
// console.log(H1.innerText);

for(var i=0; i<letters.length; i++)
{
    if(letters[i] != " ")
        H1.innerHTML = H1.innerHTML + "<span class=h1>" + letters[i] + "</span>";
    else 
        H1.innerHTML = H1.innerHTML + "<span>" + letters[i] + "</span>";
}

var SelectLetter = document.querySelectorAll(".h1");

for(let i=0; i<SelectLetter.length; i++)
{
    SelectLetter[i].addEventListener('mouseover', function(event){
        SelectLetter[i].classList.add("styleLetter");

    })

    SelectLetter[i].addEventListener('mouseout', function(event){
        SelectLetter[i].classList.remove("styleLetter");
    })
}


var classNames = document.querySelector(".classNames");

for(var i=0; i<SelectLetter.length; i++)
{
    SelectLetter[i].addEventListener('click', function(event){
        classNames.innerHTML = "The classes for lettter " + "<strong>" + this.innerText + "</strong>" + " are: " ;
        for(var j=0; j<this.className.length; j++)
        {
            if (j == this.className.length - 1)
                classNames.innerHTML = classNames.innerHTML + this.className[j] + ".";
            else if(this.className[j] == " ")    
                classNames.innerHTML = classNames.innerHTML + ", ";
            else 
            classNames.innerHTML = classNames.innerHTML + this.className[j];
        }

        classNames.innerHTML = classNames.innerHTML + "<br>";

        classNames.innerHTML = classNames.innerHTML + "The Horizontal coordinate are: " + event.pageX + ".";
    })
}

