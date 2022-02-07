<template>
<section class="notes-list">
  <h1>{{notaspersonales}}</h1>
   <article
      class="note-item"
      v-for="note in notes_list" :key="note.id">
      <h2>{{ note.title }}</h2>
      <p>{{ note.text }}</p>
      <router-link :to="{name: 'NoteDetail',  params: {id: note.id}}" ><button>detaills</button></router-link>
    </article>
</section>
</template>

<script>
  export default {
  name: 'Notes',
  data() {
    return {
      notaspersonales:"NOTAS PERSONALES",
      notes_list:[]
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes')
      this.notes_list = await response.json()
    }
  }
}

</script>
<style scoped>

 h1 {
  font:arial;
  text-shadow: grey;
}
article{
  border: 2px solid rgb(23, 87, 10);
  border-radius: 1em;
  margin:1em;
  padding: 1px;
  text-align: left;
}

</style>