<template>
  <div>
    <!-- <button @click="articleStore.fetchArticles">article 가져오기!</button> -->
    <!-- {{ articleStore.articles }} -->
    <ul>
      <li v-for="article in articleStore.articles">
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <hr>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useArticleStore } from '../stores/articles';
import { onMounted } from 'vue';

const articleStore = useArticleStore()
onMounted(() => {
  articleStore.fetchArticles()
})
</script>

<style lang="scss" scoped>

</style>