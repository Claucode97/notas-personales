<template>
<main id="notes-page">
<h1>{{$route.params.id}}</h1>
  <section id="notes-flex-container">
      <article id="note-item">
          <h3> {{note.title}}</h3>
          <p>{{note.text}}</p>
      </article>
  </section>
</main>
</template>

<script>
  export default {
  name: 'noteDetail',
  data() {
    return {
    note:{}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes/' + this.$route.params.id )
      this.note = await response.json()
      
    }
  },


}

</script>
<style scoped>
#notes-page {
    font-family: Arial, Helvetica, sans-serif;
    text-align: center;
    max-width: 90vw;
    height: 100vh;
    margin: auto;
    padding: 0;
}
#notes-flex-container {
    margin: auto;
  }
#note-item {
  float: left;
  width: 85vw;
  border: 5px double gray;
  border-radius: 1em;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 5px 5px;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
}
h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  margin-top: 10px;
  text-align: center;
  text-transform: capitalize;
}

h3 {
  text-transform: uppercase;
  text-decoration: underline;
}

</style>