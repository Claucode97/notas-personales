<template>
<h1>Note detail: {{$route.params.id}}</h1>
  <ul>
      <li>Title: {{note.title}}</li>
      <li>Text: {{note.text}}</li>
  </ul>
</template>

<script>
  export default {
  name: 'NoteDetail',
  data() {
    return {
    note:{}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/notes/' + this.$route.params.id )
      this.note = await response.json()
      
    }
  },


}

</script>
<style scoped>
article{
  width: 300px;
  height: 200px;
  border: solid 5px;
  background: violet;
  color:darkmagenta;
}
</style>