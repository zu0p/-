<template>  
  <v-container>
    <v-row id="detail-view-wrapper">
        <div class="page" id="first">
            <div class="back">
                <div class="outer">
                    <div class="content">
                        <img :src="prevImg">
                    </div>
                </div>
            </div>
        </div>
        <div class="page" id="second">
            <div class="front">
                <div class="outer">
                    <div class="content">
                        <img :src="prevImg">
                    </div>
                </div>
            </div>
            <div class="back" id="third">
                <div class="outer">
                    <div class="content">
                        <div class="helper-class-to-make-bug-visbile">
                            <img :src="nextImg">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="page" id="fourth">
            <div class="front">
                <div class="outer">
                    <div class="content">
                        <img :src="nextImg">
                    </div>
                </div>
            </div>
        </div>

        <v-row id="prev" @click="goPrevImg"></v-row>
        <v-row id="next" @click="goNextImg"></v-row>
    </v-row>
  </v-container>
</template>

<script>
import {mapState} from 'vuex'
const pageStore = 'pageStore'
export default {
  data(){
    return{
      curPageIdx: 0,
      // prevImg:"https://tympanus.net/Development/BookBlock/images/demo1/1.jpg",
      // nextImg:"https://tympanus.net/Development/BookBlock/images/demo1/2.jpg"
      prevImg:"",
      nextImg:""
    }
  },
  computed: mapState(pageStore,{
    pages: state=>state.store.pageList
  }),
  mounted(){
    console.log(this.pages[0].pageImage)

    this.prevImg = this.pages[this.curPageIdx].pageImage
    this.nextImg = this.pages[this.curPageIdx+1].pageImage
  },
  methods:{
    goPrevImg() {
      this.curPageIdx--
      let second = document.getElementById('second');
      second.style.msTransform = "rotateY(0deg)";
      second.style.webkitTransform = "rotateY(0deg)";
      second.style.transform = "rotateY(0deg)";
    },
    realNext(){
      console.log('start')
      this.curPageIdx++
      console.log(this.curPageIdx)
      this.prevImg = this.pages[this.curPageIdx].pageImage
      this.nextImg = this.pages[this.curPageIdx+1].pageImage
      console.log(this.prevImg)

      // const pageDocu = document.getElementById('detail-view-wrapper')
      // let curPage = document.createElement('div')
      // curPage.className = 'page'
      // curPage.id = 'first'
      // curPage.innerHTML = `
      //       <div class="back">
      //           <div class="outer">
      //               <div class="content">
      //                   <img src="${this.prevImg}">
      //               </div>
      //           </div>
      //       </div>
      // `
      // let newPage = document.createElement('div')
      // newPage.className = 'page'
      // newPage.id = 'second'
      // newPage.innerHTML=`
      //       <div class="front">
      //           <div class="outer">
      //               <div class="content">
      //                   <img src="${this.prevImg}">
      //               </div>
      //           </div>
      //       </div>
      //       <div class="back" id="third">
      //           <div class="outer">
      //               <div class="content">
      //                   <div class="helper-class-to-make-bug-visbile">
      //                       <img src="${this.nextImg}">
      //                   </div>
      //               </div>
      //           </div>
      //       </div>`
      
      // let newPageFourth = document.createElement('div')
      // newPageFourth.className = 'page'
      // newPageFourth.id = 'fourth'
      // newPageFourth.innerHTML = `
      //       <div class="front">
      //           <div class="outer">
      //               <div class="content">
      //                   <img src="${this.nextImg}">
      //               </div>
      //           </div>
      //       </div>
      // `
      // let prev = document.createElement('v-row')
      // prev.id='prev'
      // prev.onclick=this.goPrevImg

      // let next = document.createElement('v-row')
      // next.id='next'
      // next.onclick=this.goNextImg
      
      // pageDocu.innerHTML=''
      // pageDocu.appendChild(curPage)
      // pageDocu.appendChild(newPage)
      // pageDocu.appendChild(newPageFourth)
      // pageDocu.appendChild(prev)
      // pageDocu.appendChild(next)
    },
    goNextImg() {
      let second = document.getElementById('second');
      second.style.msTransform = "rotateY(-180deg)";
      second.style.webkitTransform = "rotateY(-180deg)";
      second.style.transform = "rotateY(-180deg)";
      console.log("done ani")

      setTimeout(this.realNext(), 4000)
    }
  }
}
</script>

<style>

#detail-view-wrapper {
    width: 100%;
    height: 90vh;
    position: relative;

    z-index: 100;
    -webkit-perspective: 1300px;
    perspective: 1300px;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
}

.page {
	position: absolute;
	-webkit-transform-style: preserve-3d;
	transform-style: preserve-3d;
	-webkit-transition-property: -webkit-transform;
	transition-property: transform;

	width: 50%;
	height: 100%;
	left: 50%;
	-webkit-transform-origin: left center;
	transform-origin: left center;
}

#first,
#first .back {
	-webkit-transform: rotateY(180deg);
	transform: rotateY(180deg);
}

#first {
    z-index: 102;
}
#second {
    z-index: 103;
    transition: transform 0.8s ease-in-out;
}
#third .content {
    width: 400px;
}
#fourth {
    z-index: 101;
}

.page > div,
.outer,
.content,
.helper-class-to-make-bug-visbile {
	position: absolute;
	height: 100%;
	width: 100%;
	top: 0;
	left: 0;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
}

.page > div {
	width: 100%;
	-webkit-transform-style: preserve-3d;
	transform-style: preserve-3d;
}

.back {
	-webkit-transform: rotateY(-180deg);
	transform: rotateY(-180deg);
}

.outer {
	width: 100%;
	overflow: hidden;
    z-index: 999;
}

/* problematic class: `.content` */
.content {
    width: 200%;
    background: white;
}


.front .content {
	left: -100%;
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