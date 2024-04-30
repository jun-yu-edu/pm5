<template>
  <div class="my-child-component">
    this is my child component
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
  </div>
</template>

<script setup>
defineProps({
  article: Object
})
</script>

<style lang="scss" scoped>
.my-child-component {
  border: 2px solid blueviolet;
  margin: 1rem;
}
</style>