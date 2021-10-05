<template>
  <v-container>
    <v-row class="wrapper">
      <v-col>
        <drag-and-drop :pDiaryId="pDiaryId" :pPageId="pPageId" />
      </v-col>
    </v-row>
  </v-container>  
</template>

<script>
import DragAndDrop from '../../components/page/DragAndDrop.vue'
export default {
  components: { DragAndDrop },
  props:['pDiaryId', 'pPageId'],
  mounted(){
    // console.log(this.pDiaryId)
  }
}
</script>

<style>
.wrapper{
  background-color: white;
  /* opacity: 0.8; */
  margin: 0 5px 0 5px;
  position: relative;
  z-index: 2;
  height: 95vh !important;
}
</style>