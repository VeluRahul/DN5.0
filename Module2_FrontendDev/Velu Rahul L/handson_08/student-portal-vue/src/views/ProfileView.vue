<template>

<div class="container">

<h1>

Student Profile

</h1>

<h2>

Enrolled Courses

</h2>

<div

v-for="course in store.enrolledCourses"

:key="course.id"

class="card"

>

<h3>

{{ course.name }}

</h3>

<p>

{{ course.code }}

</p>

<p>

Credits :

{{ course.credits }}

</p>

<button

@click="store.unenroll(course.id)"

>

Remove

</button>

</div>

<h2>

Total Credits :

{{ store.totalCredits }}

</h2>

</div>

</template>

<script setup>

import {

useEnrollmentStore

}

from "../stores/enrollment";

const store = useEnrollmentStore();

</script>

<style scoped>

.container{

padding:30px;

}

.card{

border:1px solid #ccc;

padding:15px;

margin-bottom:20px;

border-radius:8px;

}

button{

padding:8px 15px;

background:#1565c0;

color:white;

border:none;

cursor:pointer;

}

</style>
