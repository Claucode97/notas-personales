<template>
<input type="text"  class="filtrar_notas" v-model="filtered_note" placeholder="filtrar Notas">
<button class="buscar"  @click="filteredNote()"><span>filtrar</span></button><br><br>
<main id="notes-page">
<section id="notes-flex-container">
  <h1>{{notasPersonales}}</h1>
   <article
      id="note-item"
      v-for="note in filteredNote()" :key="note.id">
      <h2>{{ note.title }}</h2>
      <router-link :to="{name: 'NoteDetail',  params: {id: note.id}}" ><button class="button-detail">detaills</button></router-link>
    <button class="remove_note" @click="removeNote(note)">remove note</button>
    </article>
</section>
</main>
</template>

<script>
import Swal from 'sweetalert2';
window.Swal= Swal;
  export default {
  name: 'Notes',
  data() {
    return {
      notasPersonales:"NOTAS PERSONALES",
      notesList:[],
      filtered_note:'',
      
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
    filteredNote(){
      console.log('entrando')
      const notes = this.notesList
      const filtered_note= this.filtered_note
      return notes.filter((note) => note.title.includes(filtered_note.toLowerCase()))
  },
    async removeNote(note){

          Swal.fire({
      title: 'estas seguro?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
          fetch("http://localhost:5000/api/notes/" + note.id, {method: "DELETE"})
          this.loadData(fetch('http://localhost:5000/api/notes'));
          location.reload();
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
        )
      }
    })
    }
  },
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
  .filtrar_notas{
    width: 70%;
    height: 2em;
     border-width: thin thick mediu;
    border-radius: 10px;
  }
  ::placeholder{
    font-size: 150%;
    padding: 1em;
    color: rgb(6, 26, 117);

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