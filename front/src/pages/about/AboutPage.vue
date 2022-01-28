<template>
<section class="about">
  <h1>{{notaspersonales}}</h1>
   <article
      class="pepe"
      v-for="index in notes" :key="index.title"
    >
      <p>{{ index.title }}</p>
      <p>{{ index.text }}</p>
    </article>
</section>
</template>

<script>
  export default {
  name: 'Home',
  data() {
    return {
      notaspersonales:"NOTAS PERSONALES",
    notes:[]
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/my-notes')
      this.notes = await response.json()
    }
  }


}

</script>
<style scoped>
article{
  width: 300px;
  height: 200px;
  border: solid 5px;
  background: violet;
  color:darkmagenta;
}
</style>