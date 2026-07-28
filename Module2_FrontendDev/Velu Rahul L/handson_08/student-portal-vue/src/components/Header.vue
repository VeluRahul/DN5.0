<template>

<header>

<h2>

Student Portal

</h2>

<nav>

<RouterLink to="/">Home</RouterLink>

<RouterLink to="/courses">Courses</RouterLink>

<RouterLink to="/profile">Profile</RouterLink>

</nav>

<h3>

Enrolled :

{{ store.enrolledCourses.length }}

</h3>

</header>

</template>

<script setup>

import { RouterLink } from "vue-router";

import { useEnrollmentStore }

from "../stores/enrollment";

const store = useEnrollmentStore();

</script>

<style scoped>

header{

display:flex;

justify-content:space-between;

align-items:center;

padding:20px;

background:#1565c0;

}

h2{

color:white;

}

nav{

display:flex;

gap:20px;

}

a{

color:white;

text-decoration:none;

font-weight:bold;

}

h3{

color:white;

}

</style>
