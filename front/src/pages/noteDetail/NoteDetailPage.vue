<template>
<main>

  <h2>Detailed note</h2>

  <select v-model=" clickedCategory">
          <option value="" >Select Category</option>
          <option v-for="category in this.listOfCategories" :value="category" :key="category.id_cat">{{ category.name }}</option>
  </select>
  {{clickedCategory}}
  <section>
      <article>
            <input v-model="modifiedNote.title">
            <textarea v-model ="modifiedNote.text"  rows="8" cols="49"></textarea> 
      </article>
  </section>
       <router-link :to="{name:'Notes'}"><button>Volver</button></router-link>
      <button @click.prevent="modifyNote(modifiedNote)" class="save_button">Save</button>
      <router-link :to="{name:'NoteDetail'}" @click="removeNote"><button remove_button>Remove</button></router-link>
  
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
    loggedUser: localStorage.userName,
    listOfCategories: [],
    clickedCategory: null
   };
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

      this.listOfCategories = [
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

    removeNote(){
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
      if((this.note.title != this.modifiedNote.title) || (this.note.text != this.modifiedNote.text)){
        return true
      }
    },
    isNoteEmpty(){
      if ((this.modifiedNote.title === "") && (this.modifiedNote.text === "")){
        return true
      }
    },

    modifyNote() {

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

          fetch(`${config.API_PATH}/notes` + "/" + this.$route.params.id, settings)
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
          alert("Note has not been modified.")
        }
      }        
    },
  }
}

</script>
<style scoped>
main {
    width: 100%;
    height: 100%;
}
  section {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 90%;
    height: 80%;
    margin-bottom: 3em;
   
  }

  article {
    display: flex;
    flex-direction: column;
    width: 50%;
    height: 40%;
    margin: 0em 0em 0em 8em;
  }

  input {
    box-sizing: border-box;
    width: 60%;
    border: 0.16em solid grey;
    border-radius: 0.5em;
    font-size: 1em;
    padding-top: 1em;
    margin: 1em 0em 1em 7.4em;
  }


textarea {
  box-sizing: border-box;
  width: 60%;
  border: 0.2em solid grey;
  border-radius: 0.5em;
  font-size: 1em;
  padding-top: 1em;
  margin: 1em 0em 1em 9em;
}

select {
     background: transparent;
     border: none;
     font-size: 1.4em;
     height: 3em;
     padding: 1em;
     width: 14em;
  }

</style>
