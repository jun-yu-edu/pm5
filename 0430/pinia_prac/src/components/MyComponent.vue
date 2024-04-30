<template>
  <div>
    <h2>my Component</h2>
    <button @click="counterStore.increment">1 더하기</button>
    <input type="text" @input="onInput">
  </div>
</template>

<script setup>
import { useCounterStore } from '/src/stores/counter'
import { useTextStore } from '/src/stores/text';

const counterStore = useCounterStore()
const textStore = useTextStore()

function onInput(e) {
  // textStore에 있는 text를 변경하는 함수, 즉 setText를 실행한다.
  const newText = e.target.value
  textStore.setText(newText)
}
</script>

<style lang="scss" scoped>

</style>
