<template>
  <div class="row">
    <div v-for="image in images"  class="card col-4">
      <img :src="`/src/assets/images/${image}.jpg`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script setup>
const images = ['img0', 'img1', 'img2', 'img3', 'img4', 'img5']
</script>

<style lang="scss" scoped>

</style>