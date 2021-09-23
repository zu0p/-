<template>
  <v-container>
    <img id="img-bg" :src="preview"/>
    <v-row id="preview-wrapper">
    <div  style="width:40px" >
      <!-- <v-icon 
        id="ball"
        @mousedown="drag($event)" 
        draggable="true" 
        @dragstart.prevent
        >
        mdi-billiards
      </v-icon> -->
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
      preview: null
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
  max-width: 100%;
  
}
</style>