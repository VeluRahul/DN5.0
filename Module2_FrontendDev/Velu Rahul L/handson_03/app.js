import { courses } from "./data.js";


courses.forEach(({ name, credits }) => {
    console.log(`${name} - ${credits} credits`);
});


const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log(formattedCourses);


const filteredCourses = courses.filter(
    course => course.credits >= 4
);

console.log("Courses with credits >=4 :", filteredCourses.length);


const totalCredits = courses.reduce(
    (sum, course) => sum + course.credits,
    0
);

console.log("Total Credits =", totalCredits);


const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsText =
    document.querySelector("#total-credits");

const selectedCourse =
    document.querySelector("#selected-course");

let displayedCourses = [...courses];


function renderCourses(courseArray){

    courseGrid.innerHTML="";

    courseArray.forEach(course=>{

        const article =
            document.createElement("article");

        article.className="course-card";

        article.dataset.id=course.id;

        article.innerHTML=`

        <h3>${course.name}</h3>

        <p>Code : ${course.code}</p>

        <p>Credits : ${course.credits}</p>

        `;

        courseGrid.appendChild(article);

    });

    const total=courseArray.reduce(
        (sum,c)=>sum+c.credits,
        0
    );

    totalCreditsText.textContent=
        `Total Credits : ${total}`;

}

renderCourses(displayedCourses);


const searchInput =
document.querySelector("#search-courses");

searchInput.addEventListener("input",e=>{

    const keyword =
        e.target.value.toLowerCase();

    displayedCourses =
        courses.filter(course=>

            course.name
            .toLowerCase()
            .includes(keyword)

        );

    renderCourses(displayedCourses);

});


const sortBtn=
document.querySelector("#sort-btn");

sortBtn.addEventListener("click",()=>{

    displayedCourses.sort(

        (a,b)=>b.credits-a.credits

    );

    renderCourses(displayedCourses);

});


courseGrid.addEventListener("click",event=>{

    const card=
        event.target.closest(".course-card");

    if(!card) return;

    const id=
        Number(card.dataset.id);

    const selected=
        courses.find(c=>c.id===id);

    selectedCourse.textContent=
    `Selected Course : ${selected.name}
     | Grade : ${selected.grade}`;

});
