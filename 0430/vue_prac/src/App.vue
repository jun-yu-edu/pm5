<template>
  <div>
    <!-- <nav class="border"> 네브바 </nav> -->
    <NavBar/>
    <div class="flex">
      <!-- <aside class="border"> 어사이드</aside> -->
      <Aside/>
      <!-- <main class="border p-1">
        메인
        <div class="row">
          <article class="border col-4">아티클</article>
          <article class="border col-4">아티클</article>
          <article class="border col-4">아티클</article>
          <article class="border col-4">아티클</article>
          <article class="border col-4">아티클</article>
          <article class="border col-4">아티클</article>
        </div>
      </main> -->
      <Main/>
    </div>
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue';
import Aside from './components/Aside.vue';
import Main from './components/Main.vue';
</script>

<style lang="scss" scoped>
.flex {
  display: flex;
}
</style>