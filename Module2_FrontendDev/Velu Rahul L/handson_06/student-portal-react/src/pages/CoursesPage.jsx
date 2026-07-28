import CourseCard from "../components/CourseCard";

import { courses } from "../data";

function CoursesPage(){

return(

<div className="container">

<h1>

Courses

</h1>

{

courses.map(course=>(

<CourseCard

key={course.id}

course={course}

/>

))

}

</div>

);

}

export default CoursesPage;
