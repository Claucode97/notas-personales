<template>
<main id="notes-page">
  <h1>{{currentUser}}</h1>
  <h2>{{notesTitle}}</h2>
  <section id = "filter-add">
    <article class="search-structure">
    <input type="text" v-model="filteredNote" placeholder="Search notes...">

    <i class="fa fa-search"></i>
    </article>
    <router-link to="/notes/add"><button class="add_button">ADD NOTE</button></router-link>
  </section>
  <br>
  <section>
  <select class="selectFount" v-model="selectedCategory"> 
    <option value="null">Select category</option>
    <option v-for="index in this.listOfCategories" :value="index" :key="index.id_cat" >{{ index.name }}</option>
  </select>
  <button @click="filterByCategory">Filter By Category</button>
  {{selectedCategory}}
  </section>
  <section id="notes-flex-container">
    <article
        id="note-item"
        v-for="note in filterNote()" :key="note.id">
        <p>{{ note.title }}</p>
        <router-link :to="{name: 'NoteDetail', params: {id: note.id}}" ><button class= "detail_button">DETAILLS</button></router-link>
      <button  class="remove_button" @click="removeNote(note)">REMOVE</button>
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
      filteredNote:'',
      currentUser: "",
      listOfCategories: [],
      selectedCategory: null,
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
      //Se cargan los datos de la nota
      const response = await fetch(`${config.API_PATH}/notes`, settings)
      this.notesList = await response.json()
      this.currentUser= localStorage.userName
      
      //Se c argan los datos de la categoria
      const responseCategories = await fetch(`${config.API_PATH}/categories`)
      this.listOfCategories = await responseCategories.json()

    },
    filterNote(){
      const notes = this.notesList
      const filteredNote= this.filteredNote
      return notes.filter((note) => note.title.toLowerCase().includes(filteredNote.toLowerCase()))
  },


  filterByCategory(){

   let notesWithCategories = this.notesList
   let selectedCategory = this.selectedCategory
   let newArray =  notesWithCategories.filter((category) => category.id_cat == selectedCategory.id_cat)
   return this.notesList = newArray 
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
    }).then(async(result) => {
      if (result.isConfirmed) {
        await fetch(`${config.API_PATH}/notes`+ "/" + note.id, {method: "DELETE"})
        await  this.loadData(fetch(`${config.API_PATH}/notes`));
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
    text-align: center; 
  }

h2 {
  text-transform: uppercase;
  text-align: center; 
  }

p {
    font-size: 1.2em;
    color: black;
    text-align: left;
    text-transform: capitalize;
  }
input{
  width: 70vw;
  font-size: 1em;
  border: none; 
  
}

#notes-page {
    width: 90vw;
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
  height: 12vh;
  border: 5px double gray;
  border-radius: 1em;
  margin-top: 10px;
  padding: 5px 5px; 
  }

.search-structure {
  
  width: 90vw;
  border: 1px double gray;

}
::placeholder{
    font-size: 1em;
    color: rgb(168, 196, 160);
  }
.detail_button, .remove_button {
    float: right;
    color: white;
    background: rgb(61, 59, 59);
    border-radius: 0.5em;
    padding: 5px 5px 5px;
    font-size: 12px;
    margin-right:5px;
    border-color: black;
  }
.add_button{
  background:rgb(152, 155, 154);
  color: white;
  width: 90vw;
  margin-top: 10px;
  border-radius: 0.5em;
}
</style>