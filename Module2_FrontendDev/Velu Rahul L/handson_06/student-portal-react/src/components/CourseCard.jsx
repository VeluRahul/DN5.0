import { useNavigate } from "react-router-dom";

function CourseCard({course}){

const navigate = useNavigate();

function handleEnroll(){

navigate("/profile");

}

return(

<div
style={{
border:"1px solid #ccc",
padding:"20px",
margin:"20px",
borderRadius:"10px",
boxShadow:"0 0 8px gray"
}}
>

<h2>{course.name}</h2>

<p>

Course Code : {course.code}

</p>

<p>

Credits : {course.credits}

</p>

<p>

Grade : {course.grade}

</p>

<button

onClick={()=>navigate("/courses/"+course.id)}

>

View Details

</button>

<button

style={{marginLeft:"10px"}}

onClick={handleEnroll}

>

Enroll

</button>

</div>

);

}

export default CourseCard;
