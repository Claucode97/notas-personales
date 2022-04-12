<template>
  <h1>{{ pageTitle }}</h1>
  <article>
    <form v-on:submit.prevent="addNewNote" action="">
      <section>
        <label for="title-form">Note title: </label>
        <input
          v-model="noteTitle"
          type="text"
          name="title-form"
          placeholder="type the title here"
        />
      </section>
      <section>
        <label for="description">Description: </label>
        <textarea
          v-model="noteDescription"
          name="text-form"
          rows="8"
          cols="50"
          placeholder="type the description"
        ></textarea>
      </section>

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
    </form>
    <button @click="goBack">Back</button>
    <button @click.prevent="addNewNote">Save</button>
  </article>
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

    goBack() {
      if (this.isValidData()) {
        Swal.fire({
          title: "The note have changes. Do you want to save them?",
          showConfirmButton: true,
          showDenyButton: true,
        }).then((result) => {
          /* Read more about isConfirmed, isDenied below */
          if (result.isConfirmed) {
            this.addNewNote();
            this.$router.push("/notes");
            Swal.fire("Saved!", "", "success");
          } else if (result.isDenied) {
            Swal.fire("Changes are not saved", "", "info");
            this.$router.push("/notes");
          }
        });
      } else {
        this.$router.push("/notes");
      }
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
        const settings = {
          method: "POST",
          body: JSON.stringify(newNote),
          headers: {
            "Content-Type": "application/json",
            Authorization: jsonUsuario.id,
          },
        };
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
        this.getTagsFromNoteDescription(newNote);
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

    getTagsFromNoteDescription(note) {
      let tags = this.noteDescription.replace("\n", " ").split(" ");
      for (let tag in tags) {
        console.log(tag);
      }
      let objHashtag = { tag: tags, note_id: note.id };

      const settings = {
        method: "POST",
        body: JSON.stringify(objHashtag),
        headers: {
          "Content-Type": "application/json",
          Authorization: note.user_id,
        },
      };
      fetch(`${config.API_PATH}/tags`, settings);
    },
  },
};
</script>

<style scoped>
select {
  font-size: 1rem;
  height: 2rem;
}
article {
  font-size: 1.2rem;
}
section {
  display: flex;
  flex-direction: column;
  margin: 0.5rem 4rem;
}
label {
  text-align: left;
}
button {
  margin: 2rem 1rem;
  width: 5rem;
  height: 2rem;
  font-size: 1rem;
}
</style>
