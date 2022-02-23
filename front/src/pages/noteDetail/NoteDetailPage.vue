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
            <router-link :to="{name:'NoteDetail'}" @click="removeNote" ><button>remove contact</button></router-link>
          </section>
      </article>
  </section>
</main>
</template>

<script>
import {v4 as uuidv4} from 'uuid';
uuidv4()
import Swal from 'sweetalert2';
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
      
    },
    async removeNote(){
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
          fetch("http://localhost:5000/api/notes/" + this.$route.params.id, {method: "DELETE"})
          this.$router.push("/notes")
          //this.loadData();
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
        )
      }
    })
    },

    modifyNote() {
      if (this.note_title != "" && this.note_description != ""){
        let nextId= uuidv4()

        let newNote = {"id": nextId, "title": this.note_title, "text": this.note_description}

        const settings= {
          method: 'POST',
          body:JSON.stringify(newNote),
          headers:{
            'Content-Type': 'application/json'
          }
        }
        fetch('http://localhost:5000/api/notes', settings)
        console.log("post a la BD hacia el endpoint - 5000/api/notes POST - ")
        console.log("obj mandado al back " + JSON.stringify(newNote))
      }
      else{
          alert("Error! Fill in all the fields, please")
        }

        this.note_title = "";
        this.note_description= "";
    }
  }
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
