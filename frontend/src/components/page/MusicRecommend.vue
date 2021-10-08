<template>
  <v-container>
    <v-row>
      <v-col>
        
        
        <!-- <v-icon color="white">mdi-refresh</v-icon> -->
        <div>
          추천 음악
        </div>
        <audio id="text-recomm-music" controls autoplay loop>
          <source :src="page.textMusic" type="audio/wav">
        </audio>
      </v-col>
      <!-- <v-col>
        감정기반 추천
        <audio id="emotion-recomm-music" controls loop>
          <source :src="page.emotionMusic" type="audio/wav">
        </audio>
      </v-col> -->
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