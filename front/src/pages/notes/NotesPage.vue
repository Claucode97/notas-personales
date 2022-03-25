<template>
  <main id="notes-page">
    <h1>{{ currentUser }}</h1>
    <h2>{{ notesTitle }}</h2>
    <section id="filter-add">
      <article class="search-structure">
        <input type="text" v-model="searchNote" placeholder="Search notes..." />

        <i class="fa fa-search"></i>
      </article>
      <router-link to="/notes/add"
        ><button class="add_button">ADD NOTE</button></router-link
      >
    </section>
    <br />
    <section>
      <select class="selectFount" v-model="selectedCategory">
        <option value="">Select category</option>
        <option
          v-for="index in this.listOfCategories"
          :value="index.id_cat"
          :key="index.id_cat"
        >
          {{ index.name }}
        </option>
      </select>
    </section>
    <section id="notes-flex-container">
      <article id="note-item" v-for="note in filterNote" :key="note">
        <router-link :to="{ name: 'NoteDetail', params: { id: note.id } }">
          <span>
            <p>{{ note.title }}</p>
            <p class="category">{{ getCategoryNameById(note.id_cat) }}</p>
          </span>
        </router-link>
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
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
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
        .filter((note) => {
          if (this.selectedCategory != "" || this.selectedCategory == null) {
            if (note.id_cat == this.selectedCategory) {
              return true;
            }
          } else {
            return this.notesList;
          }
        });
    },

    // filterByCategory(){

    //  let notesWithCategories = this.notesList
    //  let selectedCategory = this.selectedCategory
    //  let newArray =  notesWithCategories.filter((category) => category.id_cat == selectedCategory.id_cat)
    //  return this.notesList = newArray
    // },
  },
};
</script>

<style scoped>
.category {
  border: 2px solid mediumpurple;
  border-radius: 4px;
  padding: 2px 2px;
}
h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  text-align: center;
}

h2 {
  text-transform: uppercase;
  text-align: center;
}

input {
  width: 70vw;
  font-size: 1em;
  border: none;
}

#notes-page {
  width: 90vw;
  margin: auto;
}

#filter-add {
  height: 10vh;
  width: 90vw;
}

#notes-flex-container {
  margin: auto;
}
span {
  display: flex;
}
#note-item {
  border: 5px double gray;
  border-radius: 1em;
  padding: 2px 2px;
}
#note-item p {
  width: 10rem;
}
#note-item .category {
  width: 5rem;
}
.search-structure {
  width: 90vw;
  border: 1px double gray;
}
::placeholder {
  font-size: 1em;
  color: rgb(168, 196, 160);
}
.detail_button,
.remove_button {
  float: right;
  color: white;
  background: rgb(61, 59, 59);
  border-radius: 0.5em;
  padding: 5px 5px 5px;
  font-size: 12px;
  margin-right: 5px;
  border-color: black;
}
.add_button {
  background: rgb(152, 155, 154);
  color: white;
  width: 90vw;
  margin-top: 10px;
  border-radius: 0.5em;
}
</style>