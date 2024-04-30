import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTextStore = defineStore('text', () => {
  const text = ref('텍스트야')

  function setText(newText){
    text.value = newText
  }
  return { text, setText }
})