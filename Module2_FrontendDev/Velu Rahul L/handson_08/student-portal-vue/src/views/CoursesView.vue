<template>

<div class="container">

<h1>

Available Courses

</h1>

<input

type="text"

placeholder="Search Course"

v-model="searchTerm"

/>

<div class="grid">

<CourseCard

v-for="course in filteredCourses"

:key="course.id"

:name="course.name"

:code="course.code"

:credits="course.credits"

:grade="course.grade"

/>

</div>

<div

v-if="filteredCourses.length===0"

>

No courses found

</div>

</div>

</template>

<script setup>

import {

ref,

computed,

onMounted

}

from "vue";

import CourseCard

from "../components/CourseCard.vue";

import {

useEnrollmentStore

}

from "../stores/enrollment";

const store = useEnrollmentStore();

const courses = ref([]);

const searchTerm = ref("");

onMounted(()=>{

courses.value=[

{

id:1,

name:"Data Structures",

code:"CS101",

credits:4,

grade:"A"

},

{

id:2,

name:"Database Management",

code:"CS102",

credits:3,

grade:"B"

},

{

id:3,

name:"Operating Systems",

code:"CS103",

credits:4,

grade:"A"

},

{

id:4,

name:"Computer Networks",

code:"CS104",

credits:3,

grade:"A"

},

{

id:5,

name:"Object Oriented Programming",

code:"CS105",

credits:4,

grade:"A"

}

];

});

const filteredCourses = computed(()=>{

return courses.value.filter(course=>

course.name

.toLowerCase()

.includes(

searchTerm.value.toLowerCase()

)

);

});

function enrollCourse(course){

store.enroll(course);

alert("Course Enrolled Successfully");

}

</script>

<style scoped>

.container{

padding:30px;

}

input{

width:100%;

padding:12px;

margin:20px 0;

font-size:16px;

}

.grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(280px,1fr));

gap:20px;

}

</style>
