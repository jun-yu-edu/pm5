<template>
  <div>
    <input type="text" v-model="text">
    <h1 :style="`color: ${text};`">color change!</h1>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const text = ref("")

</script>

<style lang="scss" scoped>

</style>
