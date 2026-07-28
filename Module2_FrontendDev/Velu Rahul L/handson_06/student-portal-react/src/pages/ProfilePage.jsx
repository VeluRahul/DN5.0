import { useSelector, useDispatch } from "react-redux";

import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage(){

const dispatch = useDispatch();

const enrolledCourses = useSelector(

state => state.enrollment.enrolledCourses

);

return(

<div className="container">

<h1>

Student Profile

</h1>

<h2>

Enrolled Courses

</h2>

{

enrolledCourses.length===0 ?

(

<p>

No Courses Enrolled

</p>

)

:

(

enrolledCourses.map(course=>(

<div

key={course.id}

style={{
border:"1px solid gray",
padding:"15px",
marginBottom:"15px"
}}

>

<h3>{course.name}</h3>

<p>{course.code}</p>

<button

onClick={()=>

dispatch(

unenroll(course.id)

)

}

>

Remove

</button>

</div>

))

)

}

</div>

);

}

export default ProfilePage;
