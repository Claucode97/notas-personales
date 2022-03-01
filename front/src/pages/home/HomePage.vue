<template>
  <div class="home"> 
    <h1>{{ personalnotes }}</h1>
    <section>
      <select v-model="selectedUser">
        <option :value="null" disable>Select User</option>
        <option v-for="user in users" :value="user" :key="user.id">
            {{ user.name }}
          </option>
      </select>
    </section>
    <button @click="onButtonClicked"> Ver mis notas</button>
    
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    personalnotes:"WELCOME",
    users:[],
    selectedUsers: null,
    };
  },

  mounted(){
    this.loadData();
  },
methods: {
  async loadData() {
    this.users = [
      {
        id: "user-1",
        name:"Pepa",
      },
      {
        id:"user-2",
        name:"Pepe",
      },
    ];
  },

  onButtonClicked(){
    localStorage.userId = this.selectedUser.id;
    localStorage.userName = this.selectedUser.name;
    this.$root.$forceUpdate();
    this.$router.push ("/notes")
    }
  }
};
</script>

<style scoped>

h1 {
    font-family: Arial, Helvetica, sans-serif;
    border: 5px double gray;
    border-radius: 1em;
    font-size: 30px;
    margin-top: 80px;
    text-align: center;
    text-transform: capitalize; 
}

</style>
