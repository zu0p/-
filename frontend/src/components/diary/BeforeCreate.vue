<template>
  <v-container>
    <div class="overlay"></div>
    <div class="bg"></div>
    <v-row >
      <!-- <img id="bg" src="@/images/night.jpg" /> -->
      <v-row align="center" class="before-contents">
        <v-col id="guide" cols="10" sm="10" md="10" lg="10">
          <div v-if="!$vuetify.breakpoint.xs">
            <v-row>
              <span><h2>아직 일기를 작성하지 않으셨군요</h2></span>
            </v-row>
            <v-row>
              <span><h3>일기를 작성해 보시겠어요?</h3></span>
            </v-row>
          </div>
          <div v-if="$vuetify.breakpoint.xs">
            <v-row>
              <span><h4>아직 일기를</h4></span>
            </v-row>
            <v-row>
              <span><h4>작성하지 않으셨군요</h4></span>
            </v-row>
            <v-row>
              <span><h5>일기를 작성해 보시겠어요?</h5></span>
            </v-row>
          </div>
        </v-col>
        <v-col cols="2" sm="2" md="2" lg="2">
          <v-btn icon x-large id="createDiaryBtn" @click="createDiary">
            <v-icon x-large color="white">mdi-chevron-right</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-row>
  </v-container> 
</template>

<script>
export default {
  name:'BeforeCreate',
  methods:{
    createDiary(){
      
    }
  }
}
</script>

<style>

.bg{
  background-image: url('../../images/night.jpg');
  min-width: 100%;
  height: 100vh;
  position: fixed;
  top:0;
  left: 0;
  z-index: -1;
}
.overlay{
  background-color: black;
  opacity: 0.7;
  min-width: 100%;
  height: 100vh;
  position: fixed;
  top:0;
  left: 0;
  z-index: 0;
}
#guide{
  color: white;
  text-align: right;
}
.before-contents{
  height: 70vh;
  position: relative;
  z-index: 1;
}
#createDiaryBtn:hover{
  background-color: gray;
}
</style>