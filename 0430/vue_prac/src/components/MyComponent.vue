<template>
  <div class="my-component">
    this is my component
    <div>text from App.vue : {{ text }}</div>
    <div>number from App.vue : {{ num }}</div>

    <MyChildComponent v-for="article in articles" :article="article"/>


  </div>
</template>

<script setup>
import MyChildComponent from './MyChildComponent.vue';
defineProps({
  text : String,
  num: Number,
})

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
  }
]

</script>

<style lang="scss" scoped>
.my-component{
  border: 1px solid black;
}
</style>