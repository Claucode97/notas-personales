<template>
  <main>
    <div class="wrapper">
      <div class="typing-demo">
        {{ notesTitle }}
      </div>
    </div>
    <h2>{{ currentUser }}</h2>
    <section id="filter-add">
      <article class="search-structure">
        <input
          class="search"
          type="search"
          v-model="searchNote"
          placeholder="Search..."
        />
      </article>
      <router-link to="/notes/add"
        ><button class="add_button">ADD NOTE</button></router-link
      >
    </section>
    <br />
    <div id="listOfCategories">
      <select v-model="selectedCategories" multiple>
        <option
          v-for="category in listOfCategories"
          :key="category"
          :value="category.id_cat"
        >
          {{ category.name }}
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
      selectedCategories: [],
      checked: "",
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
        .filter(
          (note) =>
            note.title.toLowerCase().includes(this.searchNote.toLowerCase()) ||
            note.text.includes(this.searchNote)
        )
        .filter((note) => {
          if (Object.keys(this.selectedCategories).length == 0) {
            return this.notesList;
          }
          if (
            Object.values(this.selectedCategories).indexOf(note.id_cat) > -1
          ) {
            return true;
          } else {
            return false;
          }
        });
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap");
* {
  font-family: Montserrat;
  color: white;
  scroll-behavior: smooth;
}
a {
  text-decoration: none;
}
.search-structure {
  position: absolute;
  min-width: 3rem;
  margin-right: 40%;
  margin-left: 40%;
  padding: 0.4rem;
  font-size: 1rem;
  box-shadow: 0px 2px 4px black;
  color: white;
}
.search-structure input {
  max-width: 100%;
}

.search {
  border: transparent;
  font-size: 1rem;
  display: block;
}
.search-icon {
  position: absolute;
  display: block;
  bottom: 0rem;
  right: 0.1rem;
}
.add_button {
  border-radius: 1rem;
  padding: 1rem 2rem;
  border: transparent;
  box-shadow: 0px 2px 10px black;
  margin-right: 2rem;
}
button:hover {
  cursor: pointer;
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
  border: 3px purple solid;
  border-radius: 1rem;
  padding: 0.5rem;
  align-self: center;
  margin: 0.3rem;
  font-size: 0.8rem;
}
.remove_button {
  border-radius: 1rem;
  padding: 0 3rem;
  border: transparent;
  box-shadow: 0px 2px 10px black;
}
#note-item {
  display: flex;
  box-shadow: 1px 1px 5px black;
  border-radius: 15px;
  justify-content: space-between;
  margin: 0.2rem;
}
h3 {
  margin-left: 1rem;
}
#notes-flex-container {
  margin-top: 1rem;
  margin: 1rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  max-height: 45vh;
  overflow-y: scroll;
}

.wrapper {
  /*This part is important for centering*/
  display: flex;
  align-items: center;
  justify-content: center;
  background: #c0a9ee;
  height: 4rem;
  box-shadow: 0px 2px 4px black;
}

.typing-demo {
  width: 14ch;
  animation: typing 2s steps(22), blink 0.5s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  font-family: monospace;
  font-size: 2em;
}

@keyframes typing {
  from {
    width: 0;
  }
}

@keyframes blink {
  50% {
    border-color: transparent;
  }
}
#filter-add {
  display: flex;
  flex-direction: row-reverse;
}
</style>