<template>
  <div>
    <form @submit.prevent="onSubmit">
      <input v-model="newText">
      <input type="submit" value="제출">
    </form>
    <ul>
      <li v-for="todo in todos">
        {{ todo.text }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

let newText = ref('')

const todos = reactive([
  { text: 'Hello' },
  { text: 'World' },
  { text: 'and Vue!' }
])
function onSubmit(){
  // console.log(newText.value)
  todos.push( { text : newText.value })
  newText = ref('')
}

</script>

<style lang="scss" scoped>
</style>
