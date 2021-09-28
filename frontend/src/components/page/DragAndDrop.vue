<template>
  <v-container id="preview-wrapper"> 
    <img id="img-bg" :src="preview"/>
    <v-row style="height:95%">
    <div  style="width:40px" >
      <div 
        id="ball"
        @mousedown="drag($event)" 
        draggable="true" 
        @dragstart.prevent
        name="content" contenteditable="true"
        >
      </div>
    </div>
    </v-row>
    <v-row>
      <v-btn color="blue-grey" @click="clickWritePage">
        <v-icon color="white">mdi-application-edit-outline</v-icon>
        <span style="color:white;">DONE</span>
      </v-btn>
    </v-row>
  </v-container>
  <!-- <v-container>
    <draggable>
      <v-textarea>
      </v-textarea>
    </draggable>
  </v-container> -->
</template>

<script>
import {mapActions} from 'vuex'
import draggable from 'vuedraggable'
const pageStore = 'pageStore'
export default {
  components:{
    draggable
  },
  data(){
    return{
      text: '',
      imgFile: {},
      preview: null,
      plainText: ''
    }
  },
  mounted(){
    let ball = document.getElementById('ball')
    ball.addEventListener('dragstart', function() {
      return false;
    })
    
    console.log('mounted')
    const pageStore = this.$store._modules.root._children.pageStore.state.store
    this.text = pageStore.page_text
    this.imgFile = pageStore.page_img
    this.plainText = this.text.replace(/<[^>]*>/g, '')
    console.log(this.plainText)
    console.log(this.text)
    console.log(this.imgFile)

    document.getElementById('ball').innerHTML = this.text

    var reader = new FileReader();
    reader.onload = (e) => {
      this.preview = e.target.result;
    }
    reader.readAsDataURL(this.imgFile);
  },
  created(){

  },
  methods:{
    drag(e){
      console.log("mouse down")
      let ball = document.getElementById('ball')
      ball.style.position = 'absolute'
      ball.style.zIndex = 100

      document.getElementById('preview-wrapper').append(ball)

      let shiftX = e.clientX-ball.getBoundingClientRect().left
      let shiftY = e.clientY-ball.getBoundingClientRect().top

      moveAt(e.pageX, e.pageY)
      function moveAt(x,y){
        console.log(e.clientX+" + " + e.clientY)
        console.log(shiftX+" + " + shiftY)
        // ball.style.left = x -300 + 'px'
        // ball.style.top = y - 25 + 'px'

        ball.style.left = x - e.clientX + 'px'
        ball.style.top = y - e.clientY + 'px'
      }
      function moveMouse(e){
        moveAt(e.pageX, e.pageY)
      }
      document.addEventListener('mousemove', moveMouse)

      ball.onmouseup = function(){
        document.removeEventListener('mousemove', moveMouse)
        ball.onmouseup = null
      }
    },

    clickWritePage(){
      // 이미지+텍스트+위치 create page
    }
  },
}
</script>

<style>
#ball{
  min-width: 50vh;
  min-height: 50vh;
  max-width: 80vh;
  max-height: 80vh;
}

#img-bg{
  position: absolute;
  z-index: -1;
  top:0;
  left: 0;
  
  width: 100%;
  height: 90%;

  background-position: center;
  background-size: cover;
}

#preview-wrapper{

  width: 100% !important;
  height: 100% !important;
}
/* #preview-wrapper{
  position: absolute;
  z-index: -1;
  left: 0;
  top: 0;
  width: 100vh;
  height: 100vh;
  margin: 0;
  min-height: 100%;
  background-position: center;
  background-size: cover;
} */
/* :style="`background-image: url(${preview})`" id="preview-wrapper" */
</style>