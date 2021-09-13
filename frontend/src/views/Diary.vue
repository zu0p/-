<template>
  <v-container fullscreen>
    <!-- <v-row> -->
      <v-col id="diary-menu">
        <diary-menu />
      </v-col>
    <!-- </v-row> -->
    <v-row fullscreen class="diary-contents">
      <before-create v-if="pages.length==0" />
    </v-row>
  </v-container>
</template>

<script>
import DiaryMenu from '@/components/diary/DiaryMenu.vue'
import BeforeCreate from '../components/diary/BeforeCreate.vue'
export default {
  name:'Diary',
  data(){
    return{
      pages:[]
    }
  },
  components:{
    DiaryMenu,
    BeforeCreate
  },
  create(){
    console.log(this.$router.param.title)
  }
}
</script>

<style>
#diary-menu{
  position: relative;
  z-index: 3;
}
.diary-contents{
  position: relative;
  z-index: 1;
}
</style>