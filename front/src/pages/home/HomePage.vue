<template>
  <div class="home">
    <h1>{{ greeting }}</h1>
    <section>
      <h3>User:</h3>
      <input type="text" v-model="user" />
      <h3>Password:</h3>
      <input type="password" v-model="password" />
    </section>
    <button @click="onButtonClicked">LOGIN</button>
  </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";
export default {
  name: "Home",
  data() {
    return {
      greeting: "WELCOME TO NOTES",
      user: "",
      password: "",
      localUser: useStorage("user", {}),
    };
  },

  mounted() {},
  methods: {
    async onButtonClicked() {
      const response = await login(this.user, this.password);
      const loginStatus = response.status;
      const loginUser = await response.json();
      console.log(loginStatus);
      if (response.status === 401) {
        alert("unauthorized");
      } else {
        this.localUser = loginUser;
        localStorage.setItem("user", JSON.stringify(this.localUser));
        this.$router.push("/notes");
      }
    },
  },
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
