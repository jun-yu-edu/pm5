<template>
  <div>
    <button @click="toggleVisibility">toggle</button>

    <div v-if="isVisible">보일까 안보일까??</div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
const isVisible = ref(true)

function toggleVisibility() {
    // true -> false
    // false -> true
    isVisible.value = !isVisible.value

    // if (isVisible) {
    //   isVisible = false
    // } else{
    //   isVisible = true
    // }

}
</script>

<style lang="scss" scoped>

</style>
