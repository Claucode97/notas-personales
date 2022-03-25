<template>
  <main>
    <h2>DETAILED NOTE</h2>

    <section>
      <article>
        <input id="title" v-model="modifiedNote.title" />
        <textarea
          id="text"
          v-model="modifiedNote.text"
          rows="8"
          cols="49"
        ></textarea>
      </article>
      <p>Selecciona la categoria</p>
      <select v-model="clickedCategory">
        <option disabled value="">{{ this.noteCategoryName }}</option>
        <option
          v-for="index in this.listOfCategories"
          :value="index"
          :key="index.id_cat"
        >
          {{ index.name }}
        </option>
      </select>
    </section>
    <br />
    <section>
      <button @click="goBack" class="button-save">Back</button>
      <button @click.prevent="modifyNote(modifiedNote)" class="save_button">
        Save
      </button>
      <router-link :to="{ name: 'NoteDetail' }" @click="removeNote"
        ><button>Remove</button></router-link
      >
    </section>
  </main>
</template>

<script>
import config from "../../config.js";
import Swal from "sweetalert2";

export default {
  name: "NoteDetail",
  data() {
    return {
      note: {},
      modifiedNote: {},
      loggedUser: "",
      listOfCategories: [],
      clickedCategory: "",
      noteCategoryName: "",
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
      //Carga los datos de la nota
      this.loggedUser = jsonUsuario.name;
      const response = await fetch(
        `${config.API_PATH}/notes` + "/" + this.$route.params.id,
        settings
      );
      this.note = await response.json();
      this.modifiedNote = JSON.parse(JSON.stringify(this.note));

      //Esto carga los datos de categorias
      const responseCategories = await fetch(`${config.API_PATH}/categories`);
      this.listOfCategories = await responseCategories.json();

      for (let category of this.listOfCategories) {
        if (category.id_cat == this.note.id_cat) {
          this.noteCategoryName = category.name;
        }
      }
    },
    goBack() {
      Swal.fire({
        title: 'Do you want to save the changes?',
        showConfirmButton:true,
        showDenyButton: true,
        
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
        this.modifyNote()
        this.$router.push("/notes")
        Swal.fire('Saved!', '', 'success')
      } 
      else if (result.isDenied) {
          Swal.fire('Changes are not saved', '', 'info')
          this.$router.push("/notes")
      }
})
    },
    removeNote() {
      Swal.fire({
        title: "ARE YOU SURE?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!",
      }).then(async (result) => {
        if (result.isConfirmed) {
          await fetch(
            `${config.API_PATH}/notes` + "/" + this.$route.params.id,
            { method: "DELETE" }
          );
          this.$router.push("/notes");
          Swal.fire("Deleted!", "Your file has been deleted.", "success");
        }
      });
    },

    isNoteModified() {
      if (this.clickedCategory.id_cat != undefined) {
        this.modifiedNote.id_cat = this.clickedCategory.id_cat;
      }

      if (
        this.note.title != this.modifiedNote.title ||
        this.note.text != this.modifiedNote.text ||
        this.note.id_cat != this.modifiedNote.id_cat
      ) {
        return true;
      }
    },
    isNoteEmpty() {
      if (this.modifiedNote.title === "" && this.modifiedNote.text === "") {
        return true;
      }
    },

    async modifyNote() {
      if (this.isNoteEmpty()) {
        Swal.fire("Error!", "Fill all the fields out, please!", "error");
      } else {
        if (this.isNoteModified()) {
          const settings = {
            method: "PUT",
            body: JSON.stringify(this.modifiedNote),
            headers: {
              "Content-Type": "application/json",
            },
          };

          await fetch(
            `${config.API_PATH}/notes` + "/" + this.$route.params.id,
            settings
          );
          this.loadData();
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Your work has been saved",
            showConfirmButton: false,
            timer: 1500,
          });
        } else {
          Swal.fire({
            position: "center",
            icon: "info",
            title: "Note has not been modifieded",
            showConfirmButton: false,
            timer: 1500,
          });
        }
      }
    },
  },
};
</script>
<style scoped>
main {
  text-align: center;
  width: 90vw;
}
input,
textarea {
  font-family: Arial, Helvetica, sans-serif;
  width: 90vw;
  border: 5px double gray;
  border-radius: 0.5em;
  font-size: 1em;
  padding-top: 10px;
  margin: 5px 0px 15px;
  color: black;
}

label {
  font-weight: bold;
}
</style>
