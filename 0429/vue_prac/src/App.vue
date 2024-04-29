<template>
  <div>
    <div v-for="url in urls">
      <!-- {{ url }} -->
      <a :href="url.url">{{ url.name }} </a>
    </div>
  </div>
</template>

<script setup>
const urls = [
  { name: 'naver', url: 'https://www.naver.com/' },
  { name: 'google', url: 'https://www.google.com/' },
  { name: 'github', url: 'https://github.com/'},
  { name: 'vue', url: 'https://ko.vuejs.org/'},
]
</script>

<style lang="scss" scoped>

</style>