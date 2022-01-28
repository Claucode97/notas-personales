<template>
  <div class="home">
   
    <h1>{{ personalnotes }}</h1>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    personalnotes:"WELLCOME"
    }
  }
}
</script>

<style scoped>
h1 {
  font-style: italic;
  
}

</style>
