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
    personalnotes:"WELCOME"
    }
  }
}
</script>

<style >
h1 {
  font-style: italic;
  
}

</style>
