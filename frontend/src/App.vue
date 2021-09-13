<template>
  <!-- <div class="App">
    <div class="vertical-center">
      <div class="inner-block">
        <login-page />
      </div>
    </div>
  </div> -->

  <v-app id="app">
    <router-view />
  </v-app>

</template>

<script>
// import MainPage from './views/Main.vue';
import LoginPage from './views/Login.vue';
export default {
  name: 'App',
  components: { 
    LoginPage, 
    // MainPage 
  },
};
</script>
