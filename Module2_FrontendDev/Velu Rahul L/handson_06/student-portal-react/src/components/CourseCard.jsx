import { useNavigate } from "react-router-dom";

import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

function CourseCard({ course }) {

const dispatch = useDispatch();

const navigate = useNavigate();

function handleEnroll(){

dispatch(

enroll(course)

);

navigate("/profile");

}

return(

<div
style={{
border:"1px solid gray",
padding:"20px",
margin:"20px",
borderRadius:"10px"
}}
>

<h2>{course.name}</h2>

<p>Code : {course.code}</p>

<p>Credits : {course.credits}</p>

<p>Grade : {course.grade}</p>

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
