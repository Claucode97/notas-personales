<template>
  <div class="home">
    <h1>{{ greeting }}</h1>
    <section>
      <h3>User:</h3>
      <input type="text" v-model="user" />
      <h3>Password:</h3>
      <input type="password" v-model="password" />
    </section>
    <button v-on:keyup.enter="onButtonClicked" @click="onButtonClicked">
      LOGIN
    </button>
  </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";
import Swal from "sweetalert2";
window.Swal = Swal;
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

      if (loginStatus === 401) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: "Password or user incorrect!",
          footer: "Please type it again.",
        });
      } else {
        const auth = await response.json();
        this.auth = auth;
        this.$router.push("/notes");
      }
    },
  },
};
</script>

<style scoped>
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
