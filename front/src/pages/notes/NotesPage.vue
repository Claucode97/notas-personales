<template>
<main>
  <h1>{{currentUser}}</h1>
  <h2>{{notesTitle}}</h2>
 <section class="filter-button-section">
  <select v-model="selectedCategory">
      <option :value="null"> Select Category</option>
        <option v-for="index in categories" :key="index.id_cat" :value="index">
          {{index.name}}
          </option>
    </select>
    <button @click="filteredByCategory(selectedCategory)">Filter By Category</button>
    </section>
  <section class="search-section">
    <input type="text" v-model="filtered_note" placeholder="Search notes..." >
  </section>
    <router-link to="/notes/add"><button class="add-button">Add note</button></router-link>
  <section>
    <article v-for="note in filteredNote()" :key="note.id">
        <p>{{ note.title }}</p>
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
      notesTitle:"Personal notes",
      notesList:[],
      filtered_note:'',
      currentUser: "",
      categories: [],
      selectedCategory: null,
      
      
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    filteredButton(){

      this.selectedCategory
      const categoryNotes = []
      return categoryNotes

    },
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

      this.categories = [
        {
        id_cat: "cat-1",
        name: "Sports" },
        {
        id_cat: "cat-2",
        name: "Music"
        },
         {
        id_cat: "cat-3",
        name: "Shops"
        }]
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
  
main{
      width: 100%;
    }

h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    text-align: center; 
  }

h2 {
   font-size: 2em;
   text-align: center;
  }
  .filter-button-section {
    display: flex;
    flex-direction: row;
    justify-content:center;
    width: 100%;
    height: 6em;
  }
  
  .filter-button-section button{
    font-size: 1.2em;
    width: 9em;
    height: 1.6em;
    margin-right: 14em;
  }

 select {
     margin-left: 12.4em;
     border: none;
     font-size: 1.2em;
     height: 1.6em;
     width: 9em;
}
.search-section {
    display: flex;
    flex-direction: row-reverse;
    margin:auto;
    width: 100%;
    height: 100%;
  }
  
  input{
    width: 29em;
    height: 2.4em;
    border:solid 0.1em;
    margin-right: 37em;
  }
  .add-button{
      background: rgb(122, 202, 175);
      border-radius: 0.5em;
      width: 8em;
      padding: 0.4em;
      margin-top: 4em;
      font-size: 1.2em;
    }

</style>