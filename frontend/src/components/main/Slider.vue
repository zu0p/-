<template>
    <v-container>
        <v-row justify="end" style="position:relative; z-index:2;">
            <v-dialog
            v-model="dialog"
            persistent
            max-width="600px"
            >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-bind="attrs" v-on="on" >
                        <v-icon :color="$vuetify.breakpoint.xs?'black':'white'" >mdi-plus-circle-outline</v-icon>
                    </v-btn>
                </template>
                <add-diary :isAdd="true" @closeAddDialog='onCloseAddDialog'/>
            </v-dialog>
        </v-row>
        <v-row class="slider">
            <v-col cols="1" sm="1" md="1" lg="1">
                <v-btn icon :color="$vuetify.breakpoint.xs?'black':'white'" class="button" @click="shiftLeft()">
                    <v-icon large>mdi-chevron-left</v-icon>
                </v-btn>
            </v-col>
            <v-col cols="10" sm="10" md="10" lg="10" class="cards-wrapper">
                <ul class="cards__container">
                    <li v-for="diary in diarys" :key="diary.id" class="box" :class="diary.hide">
                        <diary :diary="diary" w="12rem" h="20rem" />
                    </li>
                </ul>
            </v-col>
            <v-col cols="1" sm="1" md="1" lg="1">
                <v-btn icon :color="$vuetify.breakpoint.xs?'black':'white'" class="button" @click="shiftRight()">
                    <v-icon large>mdi-chevron-right</v-icon>
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Diary from './Diary.vue'
import AddDiary from './AddDiary.vue'
const diaryStore = 'diaryStore'

export default {
  components: { 
    Diary,
    AddDiary
  },
  data(){
    return{
    dialog:false,
    // diarys:[
    //             {
    //                 id: 1,
    //                 diaryName: 'hi',
    //                 diaryDesc: 'ddd',
    //                 diaryImg: 'ddd',
    //                 diaryShare: true
    //             },
    //             {
    //                 id: 2,
    //                 diaryName: 'hi',
    //                 diaryDesc: 'ddd',
    //                 diaryImg: 'ddd',
    //                 diaryShare: true
    //             },
    //             {
    //                 id: 3,
    //                 diaryName: 'hi',
    //                 diaryDesc: 'ddd',
    //                 diaryImg: 'ddd',
    //                 diaryShare: true
    //             },
    //             {
    //                 id: 4,
    //                 diaryName: 'hi',
    //                 diaryDesc: 'ddd',
    //                 diaryImg: 'ddd',
    //                 diaryShare: true
    //             },
    //         ]
    }
  },
  computed:{
    ...mapGetters(diaryStore, ['diaryList']),
    diarys(){
        return this.diaryList
    }, 
  },
  updated(){
      if(this.diarys.length >= 5){
          // .box 클래스에 n-th child 에 넣은 css를 처리하기 위해 css 클래스 네임 바꾸고
          for(let i = 0; i<this.diarys.length; i++){
            document.getElementsByClassName('box')[i].classList.add('over-five')
          }
      }
      else{
          for(let i = 0; i<this.diarys.length; i++){
            document.getElementsByClassName('box')[i].classList.remove('over-five')
          }
      }
  },
  beforeDestroy () {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, { passive: true })
  },
  mounted () {
    this.onResize()

    window.addEventListener('resize', this.onResize, { passive: true })

    // diary 리스트 불러와서 diarys 초기화
    this.getDiaryList()
        .then(res=>{
            this.setDiaryList(res.data)
            this.diarys
        })
    
      if(this.diarys.length >= 5){
          // .box 클래스에 n-th child 에 넣은 css를 처리하기 위해 css 클래스 네임 바꾸고
          for(let i = 0; i<this.diarys.length; i++){
            document.getElementsByClassName('box')[i].classList.add('over-five')
          }
      }
  },

  methods: {
    ...mapActions(diaryStore, ['getDiaryList', 'setDiaryList']),
    onResize () {
        this.isMobile = window.innerWidth < 600
        // if(this.isMobile)console.log("mobile")
    },
    shiftLeft: function() {
        const boxes = document.querySelectorAll(".box");
        const tmpNode = boxes[0];
        let isOverFive = boxes.length>=5?'over-five':''
        let lastIdx = boxes.length>=5?4:boxes.length-1

        boxes[0].className = `box move-out-from-left ${isOverFive}`;

        setTimeout(function() {

            if (boxes.length > 5) {
                tmpNode.classList.add("box--hide")
                boxes[5].className = `box move-to-position5-from-left ${isOverFive}`
                for(let i = 6; i<boxes.length; i++){
                    boxes[i].className = `box box--hide ${isOverFive}`
                }
            }
            // boxes[1].className = `box move-to-position1-from-left ${isOverFive}`
            // boxes[2].className = `box move-to-position2-from-left ${isOverFive}`
            // boxes[3].className = `box move-to-position3-from-left ${isOverFive}`
            // boxes[4].className = `box move-to-position4-from-left ${isOverFive}`
            boxes[0].remove();
            for(let i = 1; i<lastIdx; i++){
                boxes[i].className = `box move-to-position${i%5}-from-left ${isOverFive}`
            }
            document.querySelector(".cards__container").appendChild(tmpNode);

        }, 500);
    },
    shiftRight: function(){
        // console.log('next')
        const boxes = document.querySelectorAll(".box")
        let isOverFive = boxes.length>=5?'over-five':''
        let lastIdx = boxes.length>=5?4:boxes.length-1
        boxes[lastIdx].className = `box move-out-from-right ${isOverFive}`
        setTimeout(function() {
            const noOfCards = boxes.length;
            if (noOfCards > 5) {
                // boxes[4].className = "box box--hide over-five"
                for(let i = 4; i<boxes.length; i++){
                    boxes[i].className = "box box--hide over-five"
                }
            }

            const tmpNode = boxes[noOfCards - 1]
            tmpNode.classList.remove("box--hide")
            boxes[noOfCards - 1].remove()
            let parentObj = document.querySelector(".cards__container")
            parentObj.insertBefore(tmpNode, parentObj.firstChild)
            tmpNode.className = `box move-to-position1-from-right ${isOverFive}`
            // boxes[0].className = "box move-to-position2-from-right over-five";
            // boxes[1].className = "box move-to-position3-from-right over-five";
            // boxes[2].className = "box move-to-position4-from-right over-five";
            // boxes[3].className = "box move-to-position5-from-right over-five";
            for(let i = 0; i<lastIdx; i++){
                boxes[i].className = `box move-to-position${(i+2)%6}-from-right ${isOverFive}`
            }
        }, 500);
    },

    onCloseAddDialog(){
        this.dialog = false
    }
  }
}
</script>

<style>
.add-diary-wrapper{
    position: fixed;
    z-index: 2;
    margin: 0;
    left: 80%;
}
/* #add-diary{
    position: relative;
    z-index: 2;
} */
.slider {
    display: flex;
    justify-content: space-around;
    align-items: center;
    position: relative;
    z-index: 2;
}

.button {
    margin-left: 0 3%;
    width: 2rem;
    cursor: pointer;
    position: relative;
    z-index: 100;
}

.button--inactive {
    opacity: 0.2;
}

.button img {
    width: 60%;
}

.cards-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cards__container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 25rem;
}

.box {
    margin: 1.5rem;
    width: 12rem;
    height: 20rem;
    box-shadow: 0px 0px 2rem 0px #888888;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    /* transition: 1s all; */
}

.over-five:nth-child(2n) {
    transform: scale(0.85);
    z-index: -1;
}

.over-five:nth-child(2) {
  left: 5%;
}

.over-five:nth-child(4) {
  left: -5%;
}

.over-five:nth-child(4n + 1) {
    transform: scale(0.75);
    z-index: -2;
}

.over-five:nth-child(1) {
  left: 15%;
}

.over-five:nth-child(5) {
  left: -15%;
}

.card__text-content {
    text-align: center;
    width: 75%;
}

.card__title {
    padding: 1rem;
}

.box--hide {
    display: none;
}

.move-out-from-left {
    animation: moveOutLeft 0.5s ease-in-out;
}

.move-out-from-right {
    animation: moveOutRight 0.5s ease-in-out;
}

.move-to-position5-from-left {
    animation: moveToP5Left 0.5s ease-in-out;
}

.move-to-position4-from-left {
    animation: moveToP4Left 0.5s ease-in-out;
}

.move-to-position3-from-left {
    animation: moveToP3Left 0.5s ease-in-out;
}

.move-to-position2-from-left {
    animation: moveToP2Left 0.5s ease-in-out;
}


.move-to-position1-from-left{
    animation: moveToP1Left 0.5s ease-in-out;
}

.move-to-position5-from-right{
    animation: moveToP5Right 0.5s ease-in-out;
}
.move-to-position4-from-right{
    animation: moveToP4Right 0.5s ease-in-out;
}
.move-to-position3-from-right{
    animation: moveToP3Right 0.5s ease-in-out;
}
.move-to-position2-from-right{
    animation: moveToP2Right 0.5s ease-in-out;
}
.move-to-position1-from-right{
    animation: moveToP1Right 0.5s ease-in-out;
}

@keyframes moveOutLeft {
    0% {
        transform: scale(0.75) translateX(0%);
        opacity: 1;
    }
    50% {
        transform: scale(0.5) translateX(-150%);
        opacity: 0.5;
    }
    100% {
        transform: scale(0.25) translateX(0%);
        opacity: 0;
    }
}

@keyframes moveOutRight {
    0% {
        transform: scale(0.75) translateX(0%);
        opacity: 1;
    }
    50% {
        transform: scale(0.5) translateX(150%);
        opacity: 0.5;
    }
    100% {
        transform: scale(0.25) translateX(0%);
        opacity: 0;
    }
}


@keyframes moveToP5Left {
    from {
        transform: scale(0.75) translateX(100%);
    }
    to {
        transform: scale(0.75) translateX(0);
    }
}

@keyframes moveToP4Left {
    from {
        transform: scale(0.75) translateX(100%);
    }
    to {
        transform: scale(0.85) translateX(0);
    }
}

@keyframes moveToP3Left {
    from {
        transform: scale(0.85) translateX(100%);
    }
    to {
        transform: scale(1) translateX(0);
    }
}

@keyframes moveToP2Left {
    from {
        transform: scale(1) translateX(100%);
    }
    to {
        transform: scale(0.85) translateX(0);
    }
}

@keyframes moveToP1Left {
    from {
        transform: scale(0.85) translateX(100%);
    }
    to {
        transform: scale(0.75) translateX(0);
    }
}


@keyframes moveToP1Right {
    from {
        transform: scale(0.75) translateX(-100%);
    }
    to {
        transform: scale(0.75) translateX(0);
    }
}

@keyframes moveToP2Right {
    from {
        transform: scale(0.75) translateX(-100%);
    }
    to {
        transform: scale(0.85) translateX(0);
    }
}

@keyframes moveToP3Right {
    from {
        transform: scale(0.85) translateX(-100%);
    }
    to {
        transform: scale(1) translateX(0);
    }
}

@keyframes moveToP4Right {
    from {
        transform: scale(1) translateX(-100%);
    }
    to {
        transform: scale(0.85) translateX(0);
    }
}

@keyframes moveToP5Right {
    from {
        transform: scale(0.85) translateX(-100%);
    }
    to {
        transform: scale(0.75) translateX(0);
    }
}

</style>