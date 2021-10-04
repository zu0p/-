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
        name="content" contenteditable="false"
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
</template>

<script>
import {mapActions, mapState} from 'vuex'
import draggable from 'vuedraggable'
const pageStore = 'pageStore'
const diaryStore='diaryStore'
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
  // computed: mapState(diaryStore,{
  //   diaryId: state=>state.store.diaryId
  // }),
  // computed: mapState(pageStore,{
  //   pageText: state=>state.store.page_text,
  //   pageTitle: state=>state.store.page_title
  // }),
  computed:{
    ...mapState(pageStore, {
      pageText: state=>state.store.page_text,
      pageTitle: state=>state.store.page_title,
      pageImage: state=>state.store.page_img
    }),
    ...mapState(diaryStore,{
      diaryId: state=>state.store.diaryId
    })
  },
  mounted(){
    let ball = document.getElementById('ball')
    ball.addEventListener('dragstart', function() {
      return false;
    })
    
    this.text = this.pageText
    this.imgFile = this.pageImage
    // this.plainText = this.text.replace(/<[^>]*>/g, '')
    // console.log(this.plainText)
    // console.log(this.text)
    // console.log(this.imgFile)

    document.getElementById('ball').innerHTML = this.text

    if(typeof this.imgFile == 'string')
      this.preview = this.imgFile
    else{
      var reader = new FileReader();
      reader.onload = (e) => {
        this.preview = e.target.result;
      }
      reader.readAsDataURL(this.imgFile);
    }
  },
  methods:{
    ...mapActions(pageStore, ['requestCreateDiary']),
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
      const textbox = document.getElementById('ball')
      const textposition = textbox.getBoundingClientRect();

      const form = new FormData()
      form.append('diaryId', this.diaryId)
      form.append('pageTitle', this.pageTitle)
      form.append('pageContent', this.pageText)
      form.append('pageShare', false)
      form.append('pageImage', this.pageImage)
      form.append('top', textposition.y)
      form.append('left', textposition.x)

      this.requestCreateDiary(form)
        .then(res => {
          console.log(res)
        })
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