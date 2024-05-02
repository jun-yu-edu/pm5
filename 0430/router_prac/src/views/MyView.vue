<template>
  <div>
    <h1>This is My View</h1>

    <button @click="goHome">홈으로</button>
    <button @click="goAbout">어바웃으로</button>
    <h1 @click="goContact">컨택트로 이동!</h1>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goHome() {
  router.push('/')
}

function goAbout() {
  router.push('/about')
}
function goContact(){
  router.push('/contact')
}

</script>

<style lang="scss" scoped>

</style>