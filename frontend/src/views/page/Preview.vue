<template>
  <v-container>
    <v-row>
      <v-col class="wrapper">
        <drag-and-drop />
      </v-col>
    </v-row>
  </v-container>  
</template>

<script>
import DragAndDrop from '../../components/page/DragAndDrop.vue'
export default {
  components: { DragAndDrop },

}
</script>

<style>
.wrapper{
  background-color: white;
  opacity: 0.8;
  margin: 0 5px 0 5px;
  position: relative;
  z-index: 2;
  height: 95vh;
}
</style>