<template>
  <article class="border col-4">
    <h4>{{ article.title }}</h4>
    <p>{{ article.content }}</p>
  </article>
</template>

<script setup>
defineProps({
  article : Object
})
</script>

<style lang="scss" scoped>

</style>