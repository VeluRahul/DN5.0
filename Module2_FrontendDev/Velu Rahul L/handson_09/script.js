const courseCards = document.querySelectorAll(".course-card");

courseCards.forEach(card=>{

card.addEventListener("click",()=>{

alert("Course Selected");

});

card.addEventListener("keydown",(event)=>{

if(event.key==="Enter"){

card.click();

}

});

});

const menuButton=document.getElementById("menuButton");

menuButton.addEventListener("click",()=>{

const expanded=

menuButton.getAttribute("aria-expanded")==="true";

menuButton.setAttribute(

"aria-expanded",

!expanded

);

});

const search=document.getElementById("search");

const result=document.getElementById("results");

search.addEventListener("keyup",()=>{

const cards=document.querySelectorAll(".course-card");

let count=0;

cards.forEach(card=>{

const title=

card.querySelector("h3")

.innerText

.toLowerCase();

if(

title.includes(

search.value.toLowerCase()

)

){

card.style.display="block";

count++;

}

else{

card.style.display="none";

}

});

result.innerText=

count+

" courses found";

});
