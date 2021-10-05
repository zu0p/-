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
  props:['pDiaryId', 'pPageId'],
  data(){
    return{
      text: '',
      imgFile: {},
      preview: null,
      plainText: '',
      pageId: null,
      propsDiary: null
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
    // console.log(this.pDiaryId)
    if(this.pDiaryId){
      this.propsDiary = this.pDiaryId
      this.pageId = this.pPageId
    }

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
    ...mapActions(pageStore, ['requestCreateDiary', 'requestUpdatePage', 'requestPageList', 'setPageList', 'addPage', 'updatePage']),
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
      form.append('pageTitle', this.pageTitle)
      form.append('pageContent', this.pageText)
      form.append('pageShare', false)
      form.append('pageImage', this.pageImage)
      form.append('top', textposition.y)
      form.append('left', textposition.x)
      console.log(form)
      // 일기 수정
      if(this.propsDiary){
        form.append('diaryId', this.propsDiary)
        form.append('pageId', this.pageId)
        this.requestUpdatePage(form)
          .then(res=>{
            console.log(res)
            const newPage = {
              diaryId: this.propsDiary,
              id: this.pageId,
              top: textposition.y,
              left: textposition.x,
              pageTitle: this.pageTitle,
              pageContent: this.pageText,
              pageImage: this.pageImage,
              pageOwnerId: '',
              pageShare: false,
            }
            this.updatePage(newPage)

            this.$router.push({name:'DetailView'})
            // alert('수정이 완료되었습니다 홈으로 돌아갑니다')
            // window.location.href = `/main`
          })
      }

      // 일기 생성
      else{
        form.append('diaryId', this.diaryId)
        this.requestCreateDiary(form)
          .then(res => {
            // console.log(res)

            const newPage = {
              diaryId: this.diaryId,
              id: this.pageId,
              top: textposition.y,
              left: textposition.x,
              pageTitle: this.pageTitle,
              pageContent: this.pageText,
              pageImage: this.pageImage,
              pageOwnerId: '',
              pageShare: false,
            }
            this.addPage(newPage)

            this.$router.push({name:'DetailView'})
          })
      }
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