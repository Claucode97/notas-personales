<template>
<main>
  <h2>DETAILED NOTE</h2>
  <section id="notes-flex-container">
      <article id="note-item">
            <label for="modifiedNote.title">TITLE:</label>
            <input  v-model="modifiedNote.title">
            <label for="modifiedNote.text">TEXT:</label>
            <textarea v-model ="modifiedNote.text"  rows="8" cols="49"></textarea> 
      </article>
      <button @click.prevent="modifyNote(modifiedNote)"  class="save_button">SAVE</button>
      <router-link :to="{name:'NoteDetail'}" @click="removeNote"><button remove_button>REMOVE</button></router-link>
  </section>
</main>
</template>

<script>
import config from '../../config.js';
import Swal from 'sweetalert2';
  export default {
  name: 'NoteDetail',
  data() {
    return {
    note: {},
    modifiedNote: {},
    loggedUser: localStorage.userName
    }
  },
  
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
       const settings = {
        method: 'GET',
        headers: {
          Authorization: localStorage.userId
        },
      };
      const response = await fetch(`${config.API_PATH}/notes` + '/' + this.$route.params.id, settings)
      this.note = await response.json()
      this.modifiedNote = JSON.parse(JSON.stringify(this.note))
      
    },

    async removeNote(){
      Swal.fire({
      title: 'ARE YOU SURE?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {

          fetch(`${config.API_PATH}/notes` + "/" + this.$route.params.id, {method: "DELETE"})
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

    isNoteModified(){
      if(this.note.title != this.modifiedNote.title || this.note.text != this.modifiedNote.text){
        return true
      }
    },
    isNoteEmpty(){
      if (this.modifiedNote.title === "" && this.modifiedNote.text === ""){
        return true
      }
    },

    async modifyNote() {

      if (this.isNoteEmpty()){
        alert("Error! Fill in all the fields, please.")
      }
      else{
        if(this.isNoteModified()){
          const settings = {
          method: 'PUT',
          body: JSON.stringify(this.modifiedNote),
          headers: {
              'Content-Type': 'application/json'
            }
          }

          await fetch(`${config.API_PATH}/notes` + "/" + this.$route.params.id, settings)
          this.loadData();
          console.log("put a la BD hacia el endpoint - 5000/api/notes PUT - ")
          console.log("obj mandado al back " + JSON.stringify(this.modifiedNote))
                Swal.fire({
          position: 'center',
          icon: 'success',
          title: 'Your work has been saved',
          showConfirmButton: false,
          timer: 1500
        })

      }
        else{
          alert("Note has not being modified.")
        }
      }        
    },
  }
}

</script>
<style scoped>
main {
    text-align: center;
    width: 90vw; 
}
input, textarea {
  font-family: Arial, Helvetica, sans-serif;
  width: 90vw;
  border: 5px double gray;
  border-radius: 0.5em;
  font-size: 1em;
  text-transform: Capitalize;
  padding-top: 10px;
  margin:  5px 0px 15px ;
  color:black;
}
label {
  font-weight: bold;
}

#note-item {
  width: 85vw;
  margin-top: 20px;
  margin-bottom: 10px;
  padding: 5px 5px;
}
/* .save_button, .remove_button {
    width: 30vw;
    color: black;
    background: rgb(197, 193, 193);
    border-radius: 0.5em;
    padding: 5px 5px 5px;
    font-size: 15px;
    margin-right: 10px;
    margin-left: 10px;
    

} */
</style>
