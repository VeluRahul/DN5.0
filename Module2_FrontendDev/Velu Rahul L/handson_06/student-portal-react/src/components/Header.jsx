import { Link } from "react-router-dom";

function Header(){

return(

<header>

<h2>Student Portal</h2>

<nav>

<Link to="/">Home</Link>

<Link to="/courses">Courses</Link>

<Link to="/profile">Profile</Link>

</nav>

</header>

);

}

export default Header;
