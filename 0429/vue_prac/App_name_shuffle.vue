<template>
  <div>
    <div class="mb-5">화면</div>
    <div class="row">
      <div v-for="name in names"  class="col-2 p-2">
        <div class="border p-2">
          {{ name }}
        </div>
      </div>
    </div>
    <button class="mt-3" @click="shuffleNames">섞기!</button>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
const names = reactive(['카비바라', '강유진', '김서진', '백민지', '손명근', '신유정', '우수빈', '이다은', '이명준', '이정민', '정성윤', '조상아'])

function shuffle(array) {
  array.sort(() => Math.random() - 0.5);
}

function shuffleNames(){
  shuffle(names)
  console.log(names)
}

</script>

<style lang="scss" scoped>
.border {
  border: 2px solid black !important;
}
</style>