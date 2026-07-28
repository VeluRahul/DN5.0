import { useState } from "react";

import "./App.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";

import { coursesData } from "./data";

function App(){

const [courses] = useState(coursesData);

const [searchTerm,setSearchTerm]=useState("");

const [enrolledCourses,setEnrolledCourses]=useState([]);

function handleEnroll(course){

const exists=enrolledCourses.find(

item=>item.id===course.id

);

if(!exists){

setEnrolledCourses(

[...enrolledCourses,course]

);

}

}

const filteredCourses=courses.filter(course=>

course.name.toLowerCase().includes(

searchTerm.toLowerCase()

)

);

return(

<div className="app">

<Header

siteName="Student Portal"

count={enrolledCourses.length}

/>

<h1
style={{
marginTop:"25px"
}}
>

Available Courses

</h1>

<input

type="text"

placeholder="Search Courses..."

className="search-box"

value={searchTerm}

onChange={(e)=>

setSearchTerm(e.target.value)

}

/>

<div className="course-container">

{

filteredCourses.map(course=>(

<CourseCard

key={course.id}

name={course.name}

code={course.code}

credits={course.credits}

grade={course.grade}

onEnroll={()=>

handleEnroll(course)

}

/>

))

}

</div>

<Footer/>

</div>

);

}

export default App;
