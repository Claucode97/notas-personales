<template>
<main id="notes-page">
  <h1>{{currentUser}}</h1>
  <h2>{{notesTitle}}</h2>
  <section id = "filter-add">
    <div class="search-structure">
    <input type="text" v-model="filtered_note" placeholder="search notes...">
    <i class="fa fa-search"></i>
    </div>
    <router-link to="/notes/add"><button class="add_button">ADD NOTE</button></router-link>
  </section>
  <section id="notes-flex-container">
    <article
        id="note-item"
        v-for="note in filteredNote()" :key="note.id">
        <h2>{{ note.title }}</h2>
        <router-link :to="{name: 'NoteDetail', params: {id: note.id}}" ><button class="button-detail">detaills</button></router-link>
      <button  @click="removeNote(note)">remove</button>
      </article>
  </section>
</main>
</template>

<script>
import config from '../../config.js';
import Swal from 'sweetalert2';

window.Swal= Swal;
  export default {
  name: 'Notes',
  data() {
    return {
      notesTitle:"PERSONAL NOTES",
      notesList:[],
      filtered_note:'',
      currentUser: "",
      
      
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const settings = {
        method: 'GET',
        headers: {
          Authorization: localStorage.userId
        },
      };
      const response = await fetch(`${config.API_PATH}/notes`, settings)
      this.notesList = await response.json()
      this.currentUser= localStorage.userName
    },
    filteredNote(){
      const notes = this.notesList
      const filtered_note= this.filtered_note
      return notes.filter((note) => note.title.toLowerCase().includes(filtered_note.toLowerCase()))
  },
    async removeNote(note){

          Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
          fetch(`${config.API_PATH}/notes`+ "/" + note.id, {method: "DELETE"})
          this.loadData(fetch(`${config.API_PATH}/notes`));
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
h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    margin-top: 10px;
    text-align: center;
    text-transform: capitalize;
  }

h2 {
  text-transform: uppercase;
  text-decoration: underline;
  text-align: left;
  max-width: 70vw;   
  }

p {
    font-size: 1.2em;
    color: rgb(59, 58, 58);
    text-align: left;
  }
#notes-page {
    text-align: center;
    max-width: 90vw;
    height: 100vh;
    margin: auto;
    padding: 0;
  }
#filter-add{
  height: 10vh;
  width: 90vw;
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
  }

.search-structure i {
}
::placeholder{
    font-size: 150%;
    padding: 1em;
    color: rgb(6, 26, 117);
  }
.button-detail, button {
    float: right;
    color: white;
    background: rgb(41, 40, 40);
    border-radius: 1em;
    padding: 10px 5px 10px;
    font-size: 20px;
  }
.add_button{
  background:grey;
  width: 10em;
}
</style>