<template>
  <div class="home"> 
    <h1>{{ greeting }}</h1>
    <section>
      <h3>User:</h3>
      <input type="text" />
      <h3>Password:</h3>
      <input type="password">
    </section>
    <button @click="onButtonClicked">LOGIN</button>
  </div>
</template>

<script>
import config from '@/config.js';
export default {
  name: 'Home',
  data() {
    return {
    greeting:"WELCOME TO NOTES",
    users:[],
    selectedUser: null,
    currentUser: localStorage.userName
    };
  },

  mounted(){
    this.loadData();
  },
  methods: {
    async loadData() {
  
    
    const response = await fetch(`${config.API_PATH}/user`)
    this.users = await response.json()
  
  },

  onButtonClicked(){
    localStorage.userId = this.selectedUser.id;
    localStorage.userName = this.selectedUser.name;
    this.$router.push ("/notes")
    }
  }
};
</script>

<style scoped>

h1 {
  background-color: rgba(183, 156, 236, 0.863);
  padding-top: 0.3rem;
  margin: 0;
}
h3 {
  font-size: 2rem;
}
button {
  margin-top: 2rem;
  font-size: 1.5rem;
  background-color: mediumpurple;
  border-radius: 10%;
}
section {
  margin-top: 3rem;
}
input {
  font-size: 1.3rem;
}
</style>
