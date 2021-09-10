<template>
  <v-container>
    diary {{$route.params.title}}
  </v-container>
</template>

<script>
export default {
  create(){
    // console.log(this.$router.param.title)
  }
}
</script>

<style>

</style>