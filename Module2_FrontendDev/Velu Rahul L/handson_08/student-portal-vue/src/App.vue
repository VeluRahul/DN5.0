<template>

<Header />

<RouterView />

</template>

<script setup>

import Header from "./components/Header.vue";

import { RouterView } from "vue-router";

</script>

<style>

body{

margin:0;

font-family:Arial, Helvetica, sans-serif;

background:#f5f5f5;

}

</style>
