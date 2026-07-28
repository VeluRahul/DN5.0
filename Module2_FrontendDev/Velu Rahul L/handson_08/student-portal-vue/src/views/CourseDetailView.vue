<template>

<div class="container">

<h1>

Course Details

</h1>

<div v-if="course">

<h2>{{ course.name }}</h2>

<p>

Course Code : {{ course.code }}

</p>

<p>

Credits : {{ course.credits }}

</p>

<p>

Grade : {{ course.grade }}

</p>

<button @click="enrollCourse">

Enroll

</button>

</div>

<div v-else>

<h2>

Course Not Found

</h2>

</div>

</div>

</template>

<script setup>

import { ref,onMounted } from "vue";

import { useRoute,useRouter } from "vue-router";

const route = useRoute();

const router = useRouter();

const course = ref(null);

const courses=[

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

onMounted(()=>{

course.value=courses.find(

c=>c.id===Number(route.params.id)

);

});

function enrollCourse(){

alert("Course Enrolled Successfully");

router.push("/profile");

}

</script>

<style scoped>

.container{

padding:30px;

}

button{

margin-top:20px;

padding:10px 20px;

background:#1565c0;

color:white;

border:none;

cursor:pointer;

}

</style>
