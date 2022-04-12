<template>
  <main>
    <section class="main">
      <h1>
        <i>{{ currentUser }}</i> {{ notesTitle }}
      </h1>
      <section id="filter-add">
        <article class="search-structure">
          <input
            class="search"
            type="search"
            v-model="searchNote"
            placeholder="Search..."
          />
          <span class="search-icon"><i class="fa fa-search"></i></span>
        </article>
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
      <section>
        <article class="comic">
          <div class="panel" v-for="note in filterNote" :key="note.id">
            <p @click="goToNoteDetail(note)" class="text top-left">
              {{ note.title }}
            </p>
            <p class="text bottom-right">
              {{ getCategoryNameById(note.id_cat) }}
            </p>
            <button class="remove_button" @click="removeNote(note)">❌</button>
          </div>
        </article>
      </section>
      <router-link to="/notes/add"
        ><button class="add_button">ADD NOTE</button></router-link
      >
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
    goToNoteDetail(note) {
      this.$router.push("/notes/" + note.id);
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


<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");

* {
  margin: 0;
  padding: 0;
  font-family: Poppins;
}
main {
  margin-top: 3rem;
}
.comic {
  display: flex;
  flex-wrap: wrap;
  font-family: "Comic Sans", cursive;
  padding: 1vmin;
  max-height: 47vh;
  overflow-y: scroll;
}
.panel {
  box-shadow: 0 6px 6px -6px #000;
  display: inline-block;
  flex: 1 1;
  height: 100px;
  margin: 1vmin;
  overflow: hidden;
  position: relative;
}
.rigth {
  margin-right: 5rem;
}
input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 1rem 0;
  box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.4);
}
.text {
  background-color: rgb(249, 252, 255);
  margin: 0;
  padding: 10px 40px;
  border-radius: 5px;
}
.top-left {
  left: -6px;
  position: absolute;
  top: -2px;
  transform: skew(-5deg);
  box-shadow: 0px 2px 4px 5px rgba(0, 0, 0, 0.4);
}

.bottom-right {
  bottom: -2px;
  position: absolute;
  right: 5px;
  border-radius: 5px;
  border: transparent;
  transform: skew(-5deg);
  background: transparent;
  padding: 0.4rem;
}
.speech {
  background-color: #fff;
  border: solid 2px #000;
  border-radius: 12px;
  display: inline-block;
  margin: 0.5em;
  padding: 0.5em 1em;
  position: relative;
}
.speech:before {
  border: solid 12px transparent;
  border-left: solid 12px #000;
  border-top: solid 12px #000;
  bottom: -24px;
  content: "";
  height: 0;
  left: 24px;
  position: absolute;
  transform: skew(-15deg);
  width: 0;
}
.speech:after {
  border: solid 10px transparent;
  border-left: solid 10px #fff;
  border-top: solid 10px #fff;
  bottom: -19px;
  content: "";
  height: 0;
  left: 27px;
  position: absolute;
  transform: skew(-15deg);
  width: 0;
}
.panel {
  flex-basis: 100vw;
  font-size: 1.4rem;
} /* background colours */
.panel {
  border-radius: 5px;
  box-shadow: 2px 2px 4px black;
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(5.5px);
  -webkit-backdrop-filter: blur(5.5px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.remove_button {
  top: -2px;
  position: absolute;
  right: 5px;
  background: transparent;
  border: transparent;
  font-size: 1.1rem;
  transform: skew(-15deg);
  padding: 0.4rem;
}
.add_button {
  margin-top: 2rem;
  border: transparent;
  border-radius: 5px;
  font-size: 1rem;
  background: rgba(99, 177, 255, 0.6);
  box-shadow: 1px 2px 4px black;
  padding: 1rem 5rem;
}
.add_button:hover {
  cursor: pointer;
}
select {
  border: transparent;
  padding: 0 1rem;
  font-size: 1rem;
  box-shadow: 1px 4px 2px rgba(14, 13, 13, 0.6);
}
select option:hover {
  background: rgb(144, 216, 255);
  cursor: pointer;
}
select option:selected {
  background: yellow;
}
/* width */
::-webkit-scrollbar {
  width: 20px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey;
  border-radius: 10px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.4);
  border-radius: 10px;
}
</style>