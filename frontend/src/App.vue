<template>
  <div class="App">
      <div class="vertical-center">
        <div class="inner-block">
          <login-page />
        </div>
      </div>
    </div>
    <!-- <main-page /> -->

</template>

<script>
// import MainPage from './views/Main.vue';
import LoginPage from './views/Login.vue';
export default {
  components: { LoginPage },
};
</script>
