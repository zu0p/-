<template>
  <div class="book-section">
    <div class="container">
        <!-- <div class="right">
            <figure class="back" id="back-cover"></figure>
            <figure class="front" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/1.jpg);"></figure>
        </div>
        <div class="right">
            <figure class="back" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/1.jpg;"></figure>
            <figure class="front" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/2.jpg);"></figure>
        </div>
        <div class="right">
            <figure class="back" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/2.jpg);"></figure>
            <figure class="front" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/1.jpg);"></figure>
        </div>
        <div class="right">
            <figure class="back" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/1.jpg);"></figure>
            <figure class="front" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/2.jpg);"></figure>
        </div>
        <div class="right">
            <figure class="back" style="background-image: url(https://tympanus.net/Development/BookBlock/images/demo1/2.jpg);"></figure>
            <figure class="front" style="background-image: url(http://artisticdesigning.com/Drawings/Photoshopped/narendra_modi_caricature.jpg);"></figure>
        </div>
        <div class="right">
            <figure class="back" style="background-image: url('http://artisticdesigning.com/Drawings/Photoshopped/narendra_modi_caricature.jpg');"></figure>
            <figure class="front" id="cover">
                <h1>Diary Title</h1>
                <p>description</p>
            </figure>
        </div> -->
        <div class="right">
            <figure class="back" id="back-cover"></figure>
            <figure class="front" :style="{backgroundImage: `url(${pages[0].pageImage})`}"></figure>
        </div>
        <div class="right" v-for="(page, idx) in pages" :key="idx">
            <figure v-if="idx+1<pages.length" class="back" :style="{backgroundImage: `url(${pages[idx].pageImage})`}"></figure>
            <figure v-if="idx+1<pages.length" class="front" :style="{backgroundImage: `url(${pages[idx+1].pageImage})`}"></figure>
        </div>
        <div class="right">
            <figure class="back" :style="{backgroundImage: `url(${pages[pages.length-1].pageImage})`}"></figure>
            <figure class="front" id="cover">
                <h1>Diary Title</h1>
                <p>description</p>
            </figure>
        </div>
    </div>
    <div id="prev" @click="turnLeft"></div>
    <div id="next" @click="turnRight"></div>
    <br/>
  </div>
</template>

<script>
import {mapState} from 'vuex'
const pageStore = 'pageStore'
export default {
  data(){
    return{
      right:'',
      si:-1,
      z:1
    }
  },
  computed: mapState(pageStore,{
    pages: state=>state.store.pageList.reverse()
  }),
  mounted(){
    console.log(this.pages)
  },
  created(){
    setTimeout(() => { // HTMLCollection 길이가 0으로 나오는 문제 해결
      this.right = document.getElementsByClassName('right')
      this.si = this.right.length
    }, 0);
  },
  methods:{
    turnRight(){
      if(this.si>=1){
        this.si--
      }
      else{
        console.log('last page')
        // this.si=this.right.length-1
        // function sttmot(i){
        //   setTimeout(function(){this.right[i].style.zIndex="auto";},300) 
        // }
        // for(var i=0; i<this.right.length; i++){
        //   this.right[i].className='right' 
        //   sttmot(i)
        //   this.z=1
        // }
      }
      this.right[this.si].classList.add('flip')
      this.z++
      this.right[this.si].style.zIndex=this.z
    },
    turnLeft() {
      if(this.si<this.right.length){
        this.si++;
      }
      else{
        console.log('first page')
        // this.si=1;
        // for(var i=right.length-1;i>0;i--){
        //   right[i].classList.add('flip')
        //   right[i].style.zIndex=right.length+1-i
        // }
      }
      this.right[this.si-1].className='right'
      this.z++
      this.right[this.si-1].style.zIndex=this.z
      
      // setTimeout(function(){this.right[this.si-1].style.zIndex="auto";},350)
    }
  }
}
</script>

<style>
.book-section{
  height: 90vh;
  width: 100%;
  padding: 40px 0;
  text-align: center;
}
.book-section > .container{
  /* height: 400px;
  width: 500px; */
  height: 100%;
  width: 100%;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 2%;
  margin-bottom: 30px;
  perspective: 1200px;
}
.container > .right{
  position: absolute;
  height: 100%;
  width: 50%;
  transition: 0.7s ease-in-out;
  transform-style: preserve-3d;
}
.book-section > .container > .right{
  right:0;
  transform-origin: left;
  border-radius: 10px 0 0 10px;
}
.right > figure.front, .right > figure.back{
  margin: 0;
  height: 100%;
  width: 100%;
  position: absolute;
  left:0;
  top:0;
  background-size: 200%;
  background-repeat: no-repeat;
  backface-visibility: hidden;
  background-color: white;
  overflow: hidden;
}
.right > figure.front{
  background-position: right;
  border-radius: 0 10px 10px 0;
  box-shadow: 2px 2px 15px -2px rgba(0,0,0,0.2);
}
.right > figure.back{
  background-position: left;
  border-radius: 10px 0 0 10px;
  box-shadow: -2px 2px 15px -2px rgba(0,0,0,0.2);
  transform: rotateY(180deg);
}
.flip{
  transform: rotateY(-180deg);
}
.flip::before{
  content: "";
  position: absolute;
  top:0;
  left:0;
  z-index: 10;
  width: 100%;
  height: 100%;
  border-radius: 0 10px 10px 0;
  background-color: rgba(0,0,0,0.1);
}
.book-section > button{
  border: 2px solid #ef9f00;
  background-color: transparent;
  color: #ef9f00;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px;
  transition: 0.3s ease-in-out;
}
.book-section > button:focus, .book-section > button:active{
  outline: none;
}
.book-section > p{
  color: rgba(0,0,0,0.7);
  font-family: calibri;
  font-size: 24px;
}
.book-section > p > a{
  text-decoration: none;
  color: #ef9f00;
}
.book-section > button:hover{
  background-color: #ef9f00;
  color: #fff;
}
.front#cover, .back#back-cover{
  background-color: #ffcb63;
  font-family: calibri;
  text-align: left;
  padding: 0 30px;
}
.front#cover h1{
  color: #fff;
}
.front#cover p{
  color: rgba(0,0,0,0.8);
  font-size: 14px;
}

/* controls */
#prev, #next {
  position: absolute;
  width: 50%;
  height: 100%;
  z-index: 999;
}
#prev:hover, #next:hover {
  background: rgba(0,0,0,0.05);
  cursor: pointer;
}
#prev {
  top: 0;
  left: 0;
}
#next {
  top: 0;
  left: 50%;
}
</style>