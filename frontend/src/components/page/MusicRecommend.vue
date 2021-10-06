<template>
  <v-container>
    <v-row>
      <v-col>
        
        텍스트기반 추천
        <!-- <v-icon color="white">mdi-refresh</v-icon> -->
        
        <audio id="text-recomm-music" controls autoplay loop>
          <source :src="page.music" type="audio/wav">
        </audio>
      </v-col>
      <v-col>
        새로고침
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  props:['page'],
  created(){
  },
  methods:{
  }
}
</script>

<style>

</style>