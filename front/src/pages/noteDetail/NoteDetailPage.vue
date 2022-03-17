<template>
<main>

  <h2>DETAILED NOTE</h2>
  
  <section>
      <article>
            <input id="title" v-model="modifiedNote.title">
            <textarea id="text" v-model ="modifiedNote.text"  rows="8" cols="49"></textarea> 
      </article>
      <p>Selecciona la categoria</p>      
      <select v-model="clickedCategory"> 
          <option disabled value="">{{this.noteCategoryName}}</option>
          <option v-for="index in this.listOfCategories" :value="index" :key="index.id_cat" >{{ index.name }}</option>
      </select>
  </section>
  <br/>
  <section>
    <router-link :to="{name:'Notes'}"><button>Volver</button></router-link>
    <button @click.prevent="modifyNote(modifiedNote)" class="save_button">Save</button>
    <router-link :to="{name:'NoteDetail'}" @click="removeNote"><button remove_button>Remove</button></router-link>
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
    loggedUser: localStorage.userName,
    listOfCategories: [],
    clickedCategory: "",
    noteCategoryName: ""
   };
  },
  computed: {

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
      //Carga los datos de la nota
      const response = await fetch(`${config.API_PATH}/notes` + '/' + this.$route.params.id, settings)
      this.note = await response.json()
      this.modifiedNote = JSON.parse(JSON.stringify(this.note))
      console.log(this.modifiedNote)
      
      //Esto carga los datos de categorias
      const responseCategories = await fetch(`${config.API_PATH}/categories`)
      this.listOfCategories = await responseCategories.json()
      console.log(this.listOfCategories[0].id_cat)

      for (let category of this.listOfCategories){
        console.log(category.id_cat + "==" + this.note.id_cat)
        if (category.id_cat == this.note.id_cat){
          console.log(category)
          this.noteCategoryName = category.name
          console.log(this.noteCategoryName)
        }
      }
      
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
      console.log(this.modifiedNote.id_cat +  this.clickedCategory.id_cat)
      this.modifiedNote.id_cat = this.clickedCategory.id_cat
      console.log(this.modifiedNote.id_cat)

      if((this.note.title != this.modifiedNote.title) || (this.note.text != this.modifiedNote.text || (this.note.id_cat != this.modifiedNote.id_cat))){
        return true
      }
    },
    isNoteEmpty(){
      if ((this.modifiedNote.title) === ("" && this.modifiedNote.text === "")){
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
          alert("Note has not been modified.")
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
  padding-top: 10px;
  margin:  5px 0px 15px ;
  color:black;
}

label {
  font-weight: bold;
}

</style>
