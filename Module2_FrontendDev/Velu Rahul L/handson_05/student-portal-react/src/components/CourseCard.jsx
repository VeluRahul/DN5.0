function CourseCard({

name,
code,
credits,
grade,
onEnroll

}){

return(

<div
className="course-card"
style={{
background:"white",
padding:"20px",
borderRadius:"10px",
boxShadow:"0 0 8px rgba(0,0,0,.2)"
}}
>

<h3>{name}</h3>

<p>
<strong>Course Code :</strong> {code}
</p>

<p>
<strong>Credits :</strong> {credits}
</p>

<p>
<strong>Grade :</strong> {grade}
</p>

<button

style={{
marginTop:"10px",
padding:"10px 15px",
background:"#1565c0",
color:"white",
border:"none",
cursor:"pointer",
borderRadius:"5px"
}}

onClick={onEnroll}

>

Enroll

</button>

</div>

);

}

export default CourseCard;
