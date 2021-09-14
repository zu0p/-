<template>
  <v-container fullscreen>
    <div class="overlay"></div>
    <div class="bg"></div>
    
    <div id="diary-menu">
      <diary-menu />
    </div>
    
    <v-row fullscreen class="diary-contents">
      <router-view />
    </v-row>
  </v-container>
</template>

<script>
import DiaryMenu from '@/components/page/DiaryMenu.vue'
export default {
  name:'Page',
  data(){
    return{
      pages:[]
    }
  },
  components:{
    DiaryMenu
  },
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
  z-index: 0;
}
.overlay{
  background-color: black;
  opacity: 0.6;
  min-width: 100%;
  height: 100vh;
  position: fixed;
  top:0;
  left: 0;
  z-index: 1;
}
#diary-menu{
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 3;
}
.diary-contents{
  position: relative;
  z-index: 2;
}
</style>