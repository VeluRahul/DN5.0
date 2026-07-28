import { useContext }

from "react";

import {

EnrollmentContext

}

from "../context/EnrollmentContext";

function ProfilePage(){

const{

enrolledCourses,

remove

}

=

useContext(

EnrollmentContext

);

return(

<div className="container">

<h1>

Profile

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

<h3>

{course.name}

</h3>

<p>

{course.code}

</p>

<button

onClick={()=>

remove(course.id)

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
