<template>
  <h1>DETAILED NOTE</h1>
  <article>
    <section>
      <label for="title">Note title: </label>
      <input name="title" v-model="modifiedNote.title" />
    </section>
    <section>
      <label for="description">Description: </label>
      <textarea
        id="text"
        v-model="modifiedNote.text"
        rows="8"
        cols="49"
      ></textarea>
    </section>

    <label>Category: </label>

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

    <br />

    <button @click="goBack" class="button-save">Back</button>
    <button @click.prevent="modifyNote(modifiedNote)" class="save_button">
      Save
    </button>
    <router-link :to="{ name: 'NoteDetail' }" @click="removeNote"
      ><button>Remove</button></router-link
    >
  </article>
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
        title: "Do you want to save the changes?",
        showConfirmButton: true,
        showDenyButton: true,
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          this.modifyNote();
          this.$router.push("/notes");
          Swal.fire("Saved!", "", "success");
        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
          this.$router.push("/notes");
        }
      });
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
            timer: 1200,

          });
          this.$router.push("/notes");
        } else {
          Swal.fire({
            position: "center",
            icon: "info",
            title: "Note has not been modified",
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
