<template>
  <div class="right">    
     
    <div class="page_content_text" v-bind:id="'pct_' + idx" contenteditable="false"></div>
    <figure class="back" :style="{backgroundImage: `url(${nextImage})`}"></figure>
    <figure class="front" :style="{backgroundImage: `url(${curImage})`}"></figure>

    <div id="page-buttons">
      <v-btn icon style="z-index:1000">
          <v-icon color="blue darken-3">mdi-pencil-outline</v-icon>
      </v-btn>
      <!-- <v-btn icon style="z-index:1000" @click="clickDeletePage">
          <v-icon color="red darken-3">mdi-trash-can-outline</v-icon>
      </v-btn> -->
      <v-dialog
      v-model="deleteDialog"
      persistent
      max-width="290"
      >
          <template v-slot:activator="{ on, attrs }">
              <v-btn icon  v-bind="attrs" v-on="on">
                  <v-icon color="red darken-3">mdi-trash-can-outline</v-icon>
              </v-btn>
          </template>
          <!-- <delete-diary :id="curDiary.id" @cancelDeleteDialog="onDeleteDialog"/> -->
      </v-dialog>
    </div>
  </div>
</template>

<script>
export default {
  props: ['curImage', 'nextImage', 'page', 'idx'],
  data(){
    return{
    }
  },
  mounted(){
    // console.log(this.page.pageContent)
    const textbox = document.getElementById(`pct_${this.idx}`)
    textbox.innerHTML = this.page.pageContent
    textbox.style.left = this.page.left.toString()+"px"
    textbox.style.top = this.page.top.toString()+"px"
    console.log(textbox)

    console.log(this.page.left+" "+textbox.style.left)
  },
  methods:{
    clickDeletePage(e){
      e.stopPropagation()
      console.log("delete click")
    }
  }
}
</script>

<style>
.page_content_text{
  position: fixed !important;
}
#page-buttons{
  position: absolute;
  top: 5%;
  left: 80%;
}
</style>