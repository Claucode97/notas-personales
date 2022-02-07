<template>
  <div class="home"> 
    <h1>{{ personalnotes }}</h1>
    <p> my notes</p>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    personalnotes:"WELCOME"
    }
  }
}
</script>

<style scoped>

h1 {
    font-family: Arial, Helvetica, sans-serif;
    border: 5px double gray;
    border-radius: 1em;
    font-size: 30px;
    margin-top: 80px;
    text-align: center;
    text-transform: capitalize; 
}

</style>
