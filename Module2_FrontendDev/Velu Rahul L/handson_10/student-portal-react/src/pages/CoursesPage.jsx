import {

useEffect

}

from "react";

import {

useDispatch,

useSelector

}

from "react-redux";

import {

fetchAllCourses

}

from "../redux/courseSlice";

import {

selectCourses,

selectCoursesLoading,

selectCoursesError

}

from "../selectors/courseSelectors";

function CoursesPage(){

const dispatch=

useDispatch();

const courses=

useSelector(

selectCourses

);

const loading=

useSelector(

selectCoursesLoading

);

const error=

useSelector(

selectCoursesError

);

useEffect(()=>{

dispatch(

fetchAllCourses()

);

},[]);

if(loading){

return(

<h2>

Loading Courses...

</h2>

);

}

if(error){

return(

<h2>

Error :

{error}

</h2>

);

}

return(

<div>

<h1>

Courses

</h1>

{

courses.map(course=>(

<div

key={course.id}

style={{

border:"1px solid gray",

padding:"15px",

marginBottom:"20px"

}}

>

<h3>

{course.title}

</h3>

<p>

Course ID :

{course.id}

</p>

</div>

))

}

</div>

);

}

export default CoursesPage;
