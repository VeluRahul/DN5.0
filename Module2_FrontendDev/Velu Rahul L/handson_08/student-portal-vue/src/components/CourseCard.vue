<template>

<div class="card">

<h2>{{ name }}</h2>

<p>

Course Code : {{ code }}

</p>

<p>

Credits : {{ credits }}

</p>

<p>

Grade : {{ grade }}

</p>

<button @click="enroll">

Enroll

</button>

</div>

</template>

<script setup>

const props = defineProps({

name:String,

code:String,

credits:Number,

grade:String

});

function enroll(){

alert(props.name+" Enrolled Successfully");

}

</script>

<style scoped>

.card{

border:1px solid #ddd;

padding:20px;

margin:15px;

border-radius:10px;

box-shadow:0 0 8px rgba(0,0,0,.2);

}

button{

margin-top:15px;

padding:10px 18px;

background:#1565c0;

color:white;

border:none;

cursor:pointer;

border-radius:5px;

}

</style>
