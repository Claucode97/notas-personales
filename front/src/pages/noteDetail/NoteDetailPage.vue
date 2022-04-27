<template>
  <main>
    <h1>DETAILED NOTE</h1>
    <article>
      <section>
        <label for="title">Note title: </label>
        <input name="title" v-model="this.modifiedNote.title" />
      </section>
      <section class="desc">
        <label for="description">Description: </label>
        <textarea
          id="text"
          v-model="this.modifiedNote.text"
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
      <div class="tags">
        <p v-for="tag in note.tags" :key="tag.note_id">
          {{ tag.tag }}
        </p>
      </div>
      <div class="buttons">
        <button @click="goBack" class="back-button">Back</button>
        <button @click.prevent="modifyNote(modifiedNote)" class="save_button">
          Save
        </button>

        <button @click="removeNote" class="remove_button">Remove</button>
      </div>
    </article>
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
    this.getNoteTags();
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
    async getNoteTags() {
      const response = await fetch(
        "http://localhost:5000/api/tags/" + this.$route.params.id
      );
      let data = await response.json();
      this.note.tags = data;
    },
    goBack() {
      if (this.isNoteEmpty()) {
        Swal.fire("Error!", "Fill all the fields out, please!", "error");
      } else {
        if (this.isNoteModified()) {
          Swal.fire({
            title: "The note have changes. Do you want to save them?",
            showConfirmButton: true,
            showDenyButton: true,
          }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
              this.modifyNote();
              this.$router.push("/notes");
            } else if (result.isDenied) {
              Swal.fire("Changes are not saved", "", "info");
              this.$router.push("/notes");
            }
          });
        } else {
          this.$router.push("/notes");
        }
      }
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
      if (this.modifiedNote.title === "" || this.modifiedNote.text === "") {
        return true;
      } else {
        return false;
      }
    },

    async modifyNote() {
      if (this.isNoteEmpty() == true) {
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
          let id = this.note.id;
          await fetch(`${config.API_PATH}/notes` + "/" + id, settings);

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
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");

* {
  font-family: Poppins;
  overflow: no-scroll;
}
main {
  margin-top: 2rem;
}
.tags {
  display: flex;
}
.tags .tag {
  margin: 0.5rem;
}
input {
  font-size: 1.5rem;
  background: rgba(255, 255, 255, 0.35);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
.desc textarea {
  font-size: 1.5rem;
  background: rgba(255, 255, 255, 0.35);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
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
  width: 8rem;
  height: 4rem;
  font-size: 1.5rem;
}
.save_button {
  border: transparent;
  background: rgba(0, 225, 255, 0.35);
  box-shadow: 0 4px 5px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
.back-button {
  border: transparent;
  background: rgba(247, 0, 255, 0.35);
  box-shadow: 0 4px 5px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
.remove_button {
  border: transparent;
  background: rgba(255, 0, 0, 0.35);
  box-shadow: 0 4px 5px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}
.tags {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.tags p {
  font-size: 1.2rem !important;
  margin-left: 0.5rem;
}
@media screen and (max-width: 600px) {
  .remove_button {
    width: 5rem;
    height: 5%;
    font-size: 1rem !important;
    margin-top: 5.5rem;
  }
}
</style>
