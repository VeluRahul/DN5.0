<template>

<header>

<h2>

Student Portal

</h2>

<nav>

<RouterLink to="/">

Home

</RouterLink>

<RouterLink to="/courses">

Courses

</RouterLink>

<RouterLink to="/profile">

Profile

</RouterLink>

</nav>

</header>

</template>

<script setup>

import {

RouterLink

}

from "vue-router";

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

</style>
