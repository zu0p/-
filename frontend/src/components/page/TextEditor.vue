<template>
  <v-container style="position: relative; width:100%; height: 100%;">
    <!-- text editor -->
    <v-row>
      <form>
        <div class="title-wrapper">
          <v-text-field
            v-model="title"
            color="blue darken-2"
            :rules="rules.title"
            label="Title"
            required
            style="position: relative; width:100%; height: 100%;"
          ></v-text-field>
        </div>
        
        <div class="text-editor-menu">
          <v-row>
            <v-col cols="2" sm="1" md="1" lg="1">
              <v-btn icon onclick="document.execCommand('bold')">
                <v-icon>mdi-format-bold</v-icon>
              </v-btn>
            </v-col>
            <v-col cols="2" sm="1" md="1" lg="1">
              <v-btn icon onclick="document.execCommand('Italic')">
                <v-icon>mdi-format-italic</v-icon>
              </v-btn>  
            </v-col>          
            <v-col cols="2" sm="1" md="1" lg="1">        
              <v-btn icon onclick="document.execCommand('Underline')">
                <v-icon>mdi-format-underline</v-icon>
              </v-btn>   
            </v-col>
            <v-col cols="2" sm="1" md="1" lg="1">
              <v-btn icon onclick="document.execCommand('justifyleft')">
                <v-icon>mdi-format-align-left</v-icon>
              </v-btn>
            </v-col>
            <v-col cols="2" sm="1" md="1" lg="1">
              <v-btn icon onclick="document.execCommand('justifycenter')">
                <v-icon>mdi-format-align-center</v-icon>
              </v-btn>
            </v-col>
            <v-col cols="2" sm="1" md="1" lg="1">
              <v-btn icon onclick="document.execCommand('justifyright')">
                <v-icon>mdi-format-align-right</v-icon>
              </v-btn>
            </v-col>
            <v-col cols="2" sm="2" md="2" lg="2">
              <select id="sel" @change="formatDoc('forecolor','color')" style="color: gray; margin: 3px 5px 0 3px;">
                <option class="heading" selected>color</option>
                <option value="#D81B09FF">Red</option>
                <option value="#0911BEFF">Blue</option>
                <option value="#075A14FF">Green</option>
                <option value="black">Black</option>
                <option value="white">White</option>
              </select>
            </v-col>
            <v-col cols="2" sm="2" md="2" lg="2">
              <select id="sel2" @change="formatDoc('fontSize','size')" style="color: gray; margin: 3px 0 0 3px">
                <option class="heading" selected>size</option>
                <option value="1">4px</option>
                <option value="2">8px</option>
                <option value="3">10px</option>
                <option value="4">12px</option>
                <option value="5">16px</option>
                <option value="6">20px</option>
                <option value="7">30px</option>
              </select>
            </v-col>
          </v-row>
        </div>
        <div class="content" name="content" :contenteditable="!isDisable" :v-bind="text"></div>
        <div style="text-align: right" id="keyword-btn">
          <v-btn depressed @click="keywordButtonClick">
            <v-icon color="pink">mdi-key-chain</v-icon>
            <span>키워드 분석</span>
          </v-btn>
        </div>
        <div style="text-align: right; display:none;" id="select-keyword">
          <v-container fluid style="position: relative; width:100%; height: 100%;">
            <v-row>
              <div style="text-align:left; font-size:12px;">
                <v-icon small>mdi-lightbulb-outline</v-icon>
                <span > 키워드를 선택해주세요</span>
              </div>
            </v-row>
            <v-row>
              <v-col v-for="i in keywords" v-bind:key="i">
                <v-checkbox 
                  v-model="checkbox"
                  color="info"
                  :label="i"
                  :value="i"
                  :disabled="isDisable"
                ></v-checkbox>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn 
                  class="done-btn" 
                  depressed 
                  :disabled="isDisable"
                  @click="selectKeywordButtonClick">
                  <span>완료</span>
                  <v-icon color="blue">mdi-check-bold</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </form>
    </v-row>

  </v-container>
</template>

<script>
import {mapActions} from 'vuex'
const pageStore = 'pageStore'

export default {
  name: 'TextEditor',
  components:{
  },
  data(){
    return{
      oDoc: document.getElementsByClassName('content')[0],
      color: '#1976D2FF',
      mask: '!#XXXXXXXX',
      menu: false,

      title:'',
      rules:{
        title:[
          v => !!v || '제목은 필수 입력사항입니다.'
        ]
      },
      text:'',
      checkbox:[],
      keywords:[],
      isDisable: false
    }
  },
  methods: {
    ...mapActions(pageStore, ['setPageTitle', 'setPageText', 'setIsKeywordSearch', 'requestKeyword', 'setSelectedKeywords', 'requestEmotion']),
    onUpdate (text) {
      this.text = text
    },
    keywordButtonClick(){
      // 타이틀, 텍스트 store저장
      this.text = document.getElementsByClassName('content')[0].innerHTML
      if(this.text.length==0){
        alert('텍스트를 입력하세요')
        return
      }
      this.setPageTitle(this.title)
      this.setPageText(this.text)

      let plainText = this.text.replace(/<[^>]*>/g, '') // html to plain text
      let info={
        writing: plainText
      }

      // 키워드 분석
      this.requestKeyword(info)
        .then(res=>{
          // console.log(res.data)
          // 키워드 분석해서 가져온 값 keywords에 채워넣기
          this.keywords = res.data
        })

      // 감정추출
      this.requestEmotion(info)
        .then(res=>{
          console.log('감정')
          console.log(res.data)
          let emo=['중립','긍정','부정']
          alert('감정추출결과: '+emo[res.data])
        })

      document.getElementById('keyword-btn').style.display='none'
      document.getElementById('select-keyword').style.display='block'
    },
    selectKeywordButtonClick(){
      if(this.checkbox.length==0){
        alert('키워드를 선택하세요')
        return
      }
      this.isDisable = true

      // select한 키워드들은 this.checkbox에 배열로 담겨있음
      this.setSelectedKeywords(this.checkbox)
      console.log(this.$store._modules.root._children.pageStore.state.store.selectedKeywords)
      
      // 키워드 선택했음(true)으로 바꿈
      this.setIsKeywordSearch()
      // console.log(this.checkbox)
    },
    formatDoc(sCmd, select) {
      let sValue
      if(select=='color')
        sValue = document.getElementById('sel').options[sel.selectedIndex].value
      else if(select=='size')
        sValue = document.getElementById('sel2').options[sel2.selectedIndex].value
      // console.log(sValue)
      document.execCommand(sCmd, false, sValue)
      document.getElementsByClassName('content')[0].focus()
    },
  }
}
</script>

<style>
.content{
  position: relative !important;
  height: 50vh !important;
  /* width: 50vh !important; */
  overflow: auto;
  border: 0.01rem solid gray;
  border-radius: 5px;
  margin: 0 0 10px 0;
}
.done-btn > v-icon{
 color: black;
}
.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat) > .v-input__control > .v-input__slot {
  box-shadow: none;
}
.v-text-field.v-text-field--solo .v-input__control input {
    caret-color: auto;
    color: gray;
}
</style>