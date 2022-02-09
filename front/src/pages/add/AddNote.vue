<template>
  <main id="notes-page">
    <section id="notes-flex-container">
       <article id="note-item">
        <h1>{{ pagetitle }}</h1>
        <form v-on:submit.prevent="addNewNote" action="" >
          <section>
            <input  v-model="note_title" type="text" name="title-form"  placeholder="type the title here">
            <textarea v-model ="note_description" name="text-form" rows="8" cols="50"  placeholder="type the description"></textarea>          
            <button @click.prevent="addNewNote"  class="button-save">SAVE</button>
          </section>
        </form>
        </article>  
        
    </section>
  </main>
</template>

<script>
import {v4 as uuidv4} from 'uuid';
uuidv4()
export default {
  name: 'AddNote',
  data() {
    return {
        pagetitle:"New note",
        note_title: "",
        note_description: "",
        notes_front:[]

        
    }
  },   
  mounted() {
        this.loadData()
  },

  
  methods:{
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes')
      this.notes_front= await response.json()
    },
    addNewNote(){
        if (this.note_title != "" && this.note_description != ""){
            let nextId= uuidv4()
            
            let newNote = {"id": nextId,"title": this.note_title, "text": this.note_description}
            
            //this.notes_front.push(newNote)


            const settings={
                method:'POST',
                body:JSON.stringify(newNote),
                headers:{
                    'Content-Type': 'application/json'
                }

            }
            fetch('http://localhost:5000/api/notes', settings) // <-- comprobar ruta

            console.log("post a la BD hacia el endpoint - 5000/api/notes POST - ")
            console.log("obj mandado al back " + JSON.stringify(newNote))
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

<style escope>
#notes-page {
    text-align: center;
    height: 100vh;
    margin-top: 10px;
    padding: 0;
    font-family: Arial, Helvetica, sans-serif;
  }
#notes-flex-container {
    margin: auto;
  }
#note-item {
    width: 85vw;
    height: 30vh;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 15px 15px;
  }
#navegation-bar {
    display: block;
  }
label {
    display: block;
    text-align: left;
    font-size: 20px;
    padding: 10px;
  }
input {
    width: 85vw;
    border: 5px double gray;
    border-radius: 0.5em;
    font-family: Arial, Helvetica, sans-serif;
    margin-bottom: 20px;
  }
 
textarea {
    width: 85vw;
    height: 20vh;
    border: 5px double gray;
    border-radius: 0.5em;
    font-family: Arial, Helvetica, sans-serif;
    color: gray;
  }

h1 {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 30px;
    text-align: center;
    text-transform: capitalize;
  }

  h3 {
    text-transform: uppercase;
    text-decoration: underline;
  }

  p {
    font-size: 1.2em;
    color: rgb(59, 58, 58);
    text-align: left;
  }

  .button-save {
    color: black;
    background: rgb(197, 193, 193);
    border-radius: 0.5em;
    width: 100px;
    margin-top: 90px;
    margin-right: 10px;
    padding: 5px 10px;
    font-size: 20px;
    font-family: Arial, Helvetica, sans-serif;
  }

</style>
