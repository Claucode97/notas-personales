<template>
  <main>
    
    <h1>{{ notesTitle }}</h1>
    <h2>{{ currentUser }}</h2>
    <section id="filter-add">
      <article class="search-structure">
        <input
          class="search"
          type="search"
          v-model="searchNote"
          placeholder="Search..."/>
        <span class="search-icon"><i class="fa fa-search"></i></span>
      </article>
      <router-link to="/notes/add"
        ><button class="add_button">ADD NOTE</button></router-link
      >
    </section>
    <br/>
    <div id="listOfCategories">
        <select v-model="selectedCategories" multiple>
          <option  v-for="category in listOfCategories"  :key="category" :value="category.id_cat">
            {{category.name}}
          </option>
        </select>
    </div>
    
    <section id="notes-flex-container">
      <article id="note-item" v-for="note in filterNote" :key="note">
        <router-link :to="{ name: 'NoteDetail', params: { id: note.id } }">
          <span class="data">
            <h3>{{ note.title }}</h3>
          </span>
        </router-link>
        <p class="category">{{ getCategoryNameById(note.id_cat) }}</p>
        <button class="remove_button" @click="removeNote(note)">❌</button>
      </article>
    </section>
  </main>
</template>

<script>
import config from "../../config.js";
import Swal from "sweetalert2";

window.Swal = Swal;
export default {
  name: "Notes",
  data() {
    return {
      notesTitle: "PERSONAL NOTES",
      notesList: [],
      searchNote: "",
      currentUser: "",
      listOfCategories: [],
      selectedCategory: "",
      selectedCategories:[],
      checked:"",
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {

    async loadData() {
      console.log;
      let usuario = localStorage.getItem("user");
      let jsonUsuario = JSON.parse(usuario);
      const settings = {
        method: "GET",
        headers: {
          Authorization: jsonUsuario.id,
        },
      };
      //Se cargan los datos de la nota
      const response = await fetch(`${config.API_PATH}/notes`, settings);
      this.notesList = await response.json();
      this.currentUser = jsonUsuario.name;

      //Se c argan los datos de la categoria
      const responseCategories = await fetch(`${config.API_PATH}/categories`);
      this.listOfCategories = await responseCategories.json();
    },
    getCategoryNameById(categoryId) {
      const result = this.listOfCategories
        .filter((c) => c.id_cat == categoryId)
        .map((c) => c.name)[0];
      return result;
    },
    async removeNote(note) {
      Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!",
      }).then(async (result) => {
        if (result.isConfirmed) {
          await fetch(`${config.API_PATH}/notes` + "/" + note.id, {
            method: "DELETE",
          });
          Swal.fire("Deleted!", "Your file has been deleted.", "success").then(
            function () {
              location.reload();
            }
          );
        }
      });
    },
  },

  computed: {
    filterNote() {
      return this.notesList
        .filter((note) =>
          note.title.toLowerCase().includes(this.searchNote.toLowerCase())
        )
        .filter((note) =>{
          if(Object.keys(this.selectedCategories).length == 0)
          {
            return this.notesList
          }
            if (Object.values(this.selectedCategories).indexOf(note.id_cat) > -1) {
              console.log(this.selectedCategories)
            return true
          }
          else{
            return false
          }
          
          
        })
    },
  },
};
</script>

<style scoped>
.search-structure {
  border: 1px solid;
  min-width: 3rem;
  position: relative;
  margin-right: 10%;
  margin-left: 10%;
  font-size: 1rem;
}
.search {
  border: transparent;
  width: 100%;
  font-size: 1rem;

  display: block;
  bottom: 0rem;
  right: 0.1rem;
}
.search-icon {
  position: absolute;
  display: block;
  bottom: 0rem;
  right: 0.1rem;
}
.add_button {
  background-color: #c0a9ee;
  width: 3rem;
  float: right;
  right: 2.3rem;
  top: 12.3rem;
  border-radius: 15%;
  position: absolute;
}
.selectCategory {
  display: flex;
  justify-content: center;
}
select {
  justify-content: center;
}
.data {
  display: flex;
}
.category {
  text-decoration: none;
  border: 2px purple solid;
  border-radius: 1rem;
  padding: 0.5rem;
  align-self: center;
  margin: 0.3rem;
  font-size: 0.8rem;
}
.remove_button {
  border-radius: 1rem;
}
#note-item {
  display: flex;
  border: 1px solid;
  border-radius: 15px;
  justify-content: space-between;
  margin: 0.2rem;
}
#notes-flex-container {
  margin-top: 1rem;
  margin: 1rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}


</style>