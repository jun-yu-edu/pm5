<template>
  <main class="border p-1">
    메인
    <div class="row">
      <!-- <article class="border col-4">아티클</article>
      <article class="border col-4">아티클</article>
      <article class="border col-4">아티클</article>
      <article class="border col-4">아티클</article>
      <article class="border col-4">아티클</article>
      <article class="border col-4">아티클</article> -->
      <Article v-for="article in articles" :article="article"/>
    </div>
  </main></template>
<script setup>
import Article from './Article.vue';

const articles = [
  {
    title: 'Article 1',
    content: 'This is article 1'
  },
  {
    title: 'Article 2',
    content: 'This is article 2'
  },
  {
    title: 'Article 3',
    content: 'This is article 3'
  },
  {
    title: 'Article 4',
    content: 'This is article 4'
  },
  {
    title: 'Article 5',
    content: 'This is article 5'
  },
  {
    title: 'Article 6',
    content: 'This is article 6'
  },
]
</script>

<style lang="scss" scoped>

</style>