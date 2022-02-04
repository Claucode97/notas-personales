<template>
<h1>Note detail: {{$route.params.id}}</h1>
  <ul>
      <li>Title: {{note.title}}</li>
      <li>Text: {{note.text}}</li>
  </ul>
</template>

<script>
  export default {
  name: 'noteDetail',
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
<<<<<<< HEAD
      const response = await fetch('http://localhost:5000/api/notes/' + this.$route.params.id )
=======
      const response = await fetch('http://localhost:5000/api/notes', + this.id)
>>>>>>> 389ca6186e6cde06ab8297cf1cde2f1148ba58f0
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