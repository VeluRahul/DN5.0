import { useNavigate }

from "react-router-dom";

import { useContext }

from "react";

import { EnrollmentContext }

from "../context/EnrollmentContext";

function CourseCard({

course

}){

const navigate=

useNavigate();

const {

enroll

}

=

useContext(

EnrollmentContext

);

function handleEnroll(){

enroll(course);

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

<h2>

{course.name}

</h2>

<p>

{course.code}

</p>

<p>

Credits :

{course.credits}

</p>

<p>

Grade :

{course.grade}

</p>

<button

onClick={()=>

navigate(

"/courses/"+course.id

)

}

>

View Details

</button>

<button

style={{

marginLeft:"10px"

}}

onClick={handleEnroll}

>

Enroll

</button>

</div>

);

}

export default CourseCard;
