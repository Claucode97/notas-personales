<template>
<main id="notes-page">
  <section id="notes-flex-container">
      <article id="note-item">
          <section>
            <label for="title-form">Title:</label>
            <input  v-model="note.title" type="text" id="title-form">
            <label for="note.text">Text:</label>
            <textarea v-model ="note.text" id="text-form" rows="8" cols="50"></textarea>          
            <button @click.prevent="modifyNote"  class="button-save">SAVE</button>
            <button @click="NoteDelete"  class="button-delete">DELETE</button>
          </section>
      </article>
  </section>
</main>
</template>

<script>
  export default {
  name: 'NoteDetail',
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
section{
  display: flex;
  align-content: center;
  flex-direction: column;
}



</style>
