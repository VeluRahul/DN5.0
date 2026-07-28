import { Link } from "react-router-dom";

import { useContext } from "react";

import { EnrollmentContext }

from "../context/EnrollmentContext";

function Header(){

const {

enrolledCourses

}

=

useContext(

EnrollmentContext

);

return(

<header>

<h2>

Student Portal

</h2>

<nav>

<Link to="/">Home</Link>

<Link to="/courses">Courses</Link>

<Link to="/profile">Profile</Link>

</nav>

<h3>

Enrolled :

{enrolledCourses.length}

</h3>

</header>

);

}

export default Header;
