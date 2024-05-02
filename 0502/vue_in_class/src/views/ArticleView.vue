<template>
  <div>
    <button @click="articleStore.fetchArticles">article 가져오기!</button>
    {{ articleStore.articles }}
  </div>
</template>

<script setup>
import { useArticleStore } from '../stores/articles';

const articleStore = useArticleStore()
</script>

<style lang="scss" scoped>

</style>