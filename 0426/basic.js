let data
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => data = response.json())

console.log(data) // undefined

// console.log(undefined)