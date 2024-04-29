<template>
  <div>
    <input type="text" @input="onInput">
    <h1 :style="`color: ${text};`">color change!</h1>
  </div>
</template>

<script setup>
import {ref} from 'vue'

let text = ref("")

function onInput(event){
  text.value = event.target.value

  console.log(text.value)
}
</script>

<style lang="scss" scoped>

</style>
