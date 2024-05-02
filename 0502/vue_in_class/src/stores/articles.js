import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  function fetchArticles(){
    // django 서버에서 article들을 가져올꺼야
    axios({
      url : 'http://127.0.0.1:8000/articles/'
    })
      .then(response => {
        console.log(response.data)
        articles.value = response.data
      })
  }
  return { articles, fetchArticles}
})
