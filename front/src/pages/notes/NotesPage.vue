<template>
<main id="notes-page">
<section id="notes-flex-container">
  <h1>{{notasPersonales}}</h1>
   <article
      id="note-item"
      v-for="note in notesList" :key="note.id">
      <h2>{{ note.title }}</h2>
      <router-link :to="{name: 'NoteDetail',  params: {id: note.id}}" ><button class="button-detail">detaills</button></router-link>
    <button class="remove_note" @click="removeNote(note)">remove note</button>
    </article>
</section>
</main>
</template>

<script>
  export default {
  name: 'Notes',
  data() {
    return {
      notasPersonales:"NOTAS PERSONALES",
      notesList:[]
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes')
      this.notesList = await response.json()
    },
    async removeNote(note){
      await fetch("http://localhost:5000/api/notes/" + note.id, {method: "DELETE"})
      this.loadData();
      
    }
  }
}

</script>

<style scoped>
#notes-page {
    text-align: center;
    max-width: 90vw;
    height: 100vh;
    margin: auto;
    padding: 0;
  }
#notes-flex-container {
    margin: auto;
  }

h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    margin-top: 10px;
    text-align: center;
    text-transform: capitalize;
  }
#note-item {
    float: left;
    width: 85vw;
   
    border: 5px double gray;
    border-radius: 1em;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 5px 5px; 
  }

h2 {
    text-transform: uppercase;
    text-decoration: underline;
    text-align: left;
    
  }

  p {
    font-size: 1.2em;
    color: rgb(59, 58, 58);
    text-align: left;
  }

  .button-detail, button {
    float: right;
    color: white;
    background: rgb(41, 40, 40);
    border-radius: 1em;
    padding: 10px 5px 10px;
    font-size: 20px;
  }

</style>