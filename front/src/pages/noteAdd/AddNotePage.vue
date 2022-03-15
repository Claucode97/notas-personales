<template>
  <main>
  <section>
        <h1>{{ pagetitle }}</h1>
    <select v-model="selectedCategory">
      <option :value="null" > Select Category</option>
        <option v-for="index in categories" :key="index.id_cat" :value="index">
          {{index.name}}
          </option>
    </select>
    {{selectedCategory}}
    </section>
    <section class="container">
        <form v-on:submit.prevent="addNewNote" action="">
            <input  v-model="note_title" type="text" name="title-form"  placeholder="type the title here">
            <textarea v-model ="note_description" name="text-form" rows="8" cols="50"  placeholder="type the description"></textarea>
        </form>
    </section>
    <section class="section-buttons">
          <router-link :to="{name:'Notes'}"><button class="buttons">Back</button></router-link>
          <button @click.prevent="addNewNote"  class="buttons">Save</button>
    </section>
  </main>
</template>

<script>
import config from '@/config.js';
import Swal from 'sweetalert2';
window.Swal= Swal;
import {v4 as uuidv4} from 'uuid';

export default {
  name: 'AddNote',
  data() {
    return {
        pagetitle:"New note",
        note_title: "",
        note_description: "",
        notes_front:[],
        categories: [],
        selectedCategory: null,
    }
  },   
  mounted() {
        this.loadData()
  },

  
  methods:{
    async loadData() {
      const response = await fetch(`${config.API_PATH}/notes`)
      this.notes_front= await response.json()

      this.categories = [
        {
        id_cat: "cat-0",
        name: "No category" },
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
    addNewNote(){
        if (this.note_title != "" && this.note_description != ""){
            let nextId= uuidv4()
            
            let newNote = {"id": nextId, "title": this.note_title,
                           "text": this.note_description, 
                           "user_id": localStorage.userId,
                          "id_cat": this.selectedCategory.id_cat }

            console.log("new note", newNote)

            const settings={
                method:'POST',
                body:JSON.stringify(newNote),
                headers:{
                    'Content-Type': 'application/json',
                    Authorization: localStorage.userId
                }
            }
            fetch(`${config.API_PATH}/notes`, settings)

            console.log("post a la BD hacia el endpoint - 5000/api/notes POST - ")
            console.log("obj mandado al back " + JSON.stringify(newNote))
            Swal.fire({
                      position: 'center',
                      icon: 'success',
                      title: 'Your note has been saved',
                      showConfirmButton: false,
                      timer: 1500
                      })
            //Esto redirige a la página principal de todas las notas, justo despues de añadir una nueva
            // Si no queremos la redirección, sólo hay que borrar la línea de abajo
            this.$router.push ("/notes") 
        }
              
        else{
            alert("Error! Fill in all the fields, please")
        }

        this.note_title = ""
        this.note_description= ""
        

        }
    }
}
</script>

<style scoped>

  h1 {
    font-size: 2em;
    text-align: center;
  }

  main {
    display: flex;
    flex-direction:column;
    justify-content: center;
    width: 100%;
  }
  .container {
   margin: auto;
   display: flex;
   flex-direction: row;
   justify-content: center;
   width: 90%;
  }
  
  form{
    margin: auto;
    width: 60%;
    height: 40%;
    }

  input {
    height: 2em;
    width: 80%;
    border: 0.2em solid grey;
    border-radius: 0.5em;
    margin-bottom: 1.9em;
  }
  
  textarea {
    width: 80%;
    border: 0.2em solid grey;
    border-radius: 0.5em; 

    }

  .buttons{
    background: rgb(122, 202, 175);
    border-radius: 0.5em;
    width: 4em;
    padding: 0.4em;
    margin-top: 4em;
    font-size: 1.2em;
  }

  .section-buttons {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: auto;

  }

select {
     background: transparent;
     margin: 0em 0em 2em 1em;
     border: none;
     font-size: 1.2em;
     height: 2.9em;
     padding: 1em;
     width: 14em;
}


</style>
