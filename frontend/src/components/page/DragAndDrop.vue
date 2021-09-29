<template>
  <v-container>
    <v-row id="preview-wrapper">
    <div id="ball" style="width:40px" @mousedown="drag($event)">
    <v-icon>mdi-billiards</v-icon>
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
import draggable from 'vuedraggable'
export default {
  components:{
    draggable
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
        ball.style.left = x - shiftX + 'px'
        ball.style.top = y - shiftY + 'px'
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
  mounted(){
    let ball = document.getElementById('ball')
    ball.addEventListener('dragstart', function() {
      return false;
    })
  }
}
</script>

<style>

</style>