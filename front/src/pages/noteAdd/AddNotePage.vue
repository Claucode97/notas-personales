<template>
  <main id="notes-page">
    <section>
      <h1>{{ pageTitle }}</h1>
    </section>
    <section id="notes-flex-container">
      <article id="note-item">
        <form v-on:submit.prevent="addNewNote" action="">
          <section>
            <input
              v-model="noteTitle"
              type="text"
              name="title-form"
              placeholder="type the title here"
            />
            <textarea
              v-model="noteDescription"
              name="text-form"
              rows="8"
              cols="50"
              placeholder="type the description"
            ></textarea>

            <div class="select">
              <p>Select category:</p>
              <select class="selectFount" v-model="selectedCategory">
                <option value="null">Select category</option>
                <option
                  v-for="index in this.listOfCategories"
                  :value="index"
                  :key="index.id_cat"
                >
                  {{ index.name }}
                </option>
              </select>
            </div>
          </section>
        </form>
        <router-link :to="{ name: 'Notes' }"
          ><button class="button-save">VOLVER</button></router-link
        >
        <button @click.prevent="addNewNote" class="button-save">SAVE</button>
      </article>
    </section>
  </main>
</template>

<script>
import config from "@/config.js";
import Swal from "sweetalert2";
window.Swal = Swal;
import { v4 as uuidv4 } from "uuid";

export default {
  name: "AddNote",
  data() {
    return {
      pageTitle: "New note",
      noteTitle: "",
      noteDescription: "",
      listOfCategories: [],
      selectedCategory: null,
    };
  },
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      //Categorias
      const responseCategories = await fetch(`${config.API_PATH}/categories`);
      this.listOfCategories = await responseCategories.json();
    },

    isValidData() {
      if (this.noteTitle != "" && this.noteDescription != "") {
        return true;
      } else {
        return false;
      }
    },
    addNewNote() {
      if (this.isValidData()) {
        let usuario = localStorage.getItem("user");
        let jsonUsuario = JSON.parse(usuario);

        let nextId = uuidv4();
        if (this.selectedCategory === null) {
          this.selectedCategory = { id_cat: "cat-0", name: "No category" };
        }
        let newNote = {
          id: nextId,
          title: this.noteTitle,
          text: this.noteDescription,
          user_id: jsonUsuario.id,
          id_cat: this.selectedCategory.id_cat,
        };
        console.log(newNote);
        const settings = {
          method: "POST",
          body: JSON.stringify(newNote),
          headers: {
            "Content-Type": "application/json",
            Authorization: jsonUsuario.id,
          },
        };
        console.log(settings);
        fetch(`${config.API_PATH}/notes`, settings);
        Swal.fire({
          position: "center",
          icon: "success",
          title: "Your note has been saved",
          showConfirmButton: false,
          timer: 1500,
        });
        //Esto redirige a la página principal de todas las notas, justo despues de añadir una nueva
        // Si no queremos la redirección, sólo hay que borrar la línea de abajo
        this.$router.push("/notes");
      } else {
        Swal.fire({
          position: "center",
          icon: "error",
          title: "Error! Fill all the fields out, please!",
          showConfirmButton: false,
          timer: 1500,
        });
      }

      this.noteTitle = "";
      this.noteDescription = "";
    },
  },
};
</script>

<style scoped>
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

input,
textarea {
  width: 85vw;
  border: 5px double gray;
  border-radius: 0.5em;
  margin-bottom: 20px;
  font-family: Arial, Helvetica, sans-serif;
}

h1 {
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
  margin-top: 30px;
  margin-right: 10px;
  padding: 5px 10px;
  font-size: 20px;
}

.select {
  display: flex;
  justify-content: center;
}

select {
  font-size: 1rem;
}
</style>
