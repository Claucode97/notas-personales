<template>
<main id="notes-page">
  <section id="notes-flex-container">
      <article id="note-item">
          <section>
            <label for="note.title">Title:</label>
            <input  v-model="note.title" type="text" id="title-form">
            <label for="note.text">Text:</label>
            <textarea v-model ="note.text" id="text-form" rows="8" cols="50"></textarea>          
            <button @click.prevent="modifyNote(note)"  class="button-save">SAVE</button>
            <router-link :to="{name:'NoteDetail'}" @click="removeNote" ><button>remove contact</button></router-link>
          </section>
      </article>
  </section>
</main>
</template>

<script>
import Swal from 'sweetalert2';
  export default {
  name: 'NoteDetail',
  data() {
    return {
    note: {}
    }
  },
  mounted() {
    this.loadData();
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


    async modifyNote() {
      if (this.note.title != "" && this.note.text != ""){

        const settings = {
          method: 'PUT',
          body: JSON.stringify(this.note),
          headers: {
              'Content-Type': 'application/json'
          }
                
        }

        await fetch("http://localhost:5000/api/notes/" + this.$route.params.id, settings)
        this.loadData();
        console.log("put a la BD hacia el endpoint - 5000/api/notes PUT - ")
        console.log("obj mandado al back " + JSON.stringify(this.note))
              Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
      })
      }
      else{
          alert("Error! Fill in all the fields, please.")
        }  
    },
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
