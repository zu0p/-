<template>
  <v-container>
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
          ></v-text-field>
        </div>
        
        <div class="text-editor-menu">
          <v-btn icon onclick="document.execCommand('bold')">
            <v-icon>mdi-format-bold</v-icon>
          </v-btn>
          <v-btn icon onclick="document.execCommand('Italic')">
            <v-icon>mdi-format-italic</v-icon>
          </v-btn>          
          <v-btn icon onclick="document.execCommand('Underline')">
            <v-icon>mdi-format-underline</v-icon>
          </v-btn>   
          <v-btn icon onclick="document.execCommand('justifyleft')">
            <v-icon>mdi-format-align-left</v-icon>
          </v-btn>
          <v-btn icon onclick="document.execCommand('justifycenter')">
            <v-icon>mdi-format-align-center</v-icon>
          </v-btn>
          <v-btn icon onclick="document.execCommand('justifyright')">
            <v-icon>mdi-format-align-right</v-icon>
          </v-btn>
          <!-- <select id="fontSize" width="50px">
            <option value="">글자 크기</option>
            <option value="3">10px</option>
            <option value="4">12px</option>
            <option value="5">16px</option>
            <option value="6">20px</option>
            <option value="7">30px</option>
          </select> -->
        </div>
        <div class="content" name="content" contenteditable="true" :v-bind="text"></div>
        <div style="text-align: right" id="keyword-btn">
          <v-btn depressed @click="keywordButtonClick">
            <v-icon color="pink">mdi-key-chain</v-icon>
            <span>키워드 분석</span>
          </v-btn>
        </div>
        <div style="text-align: right; display:none;" id="select-keyword">
          <v-container fluid>
            <v-row>
              <div style="text-align:left; font-size:12px;">
                <v-icon small>mdi-lightbulb-outline</v-icon>
                <sapn > 키워드를 선택해주세요</sapn>
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
      title:'',
      rules:{
        title:[
          v => !!v || '제목은 필수 입력사항입니다.'
        ]
      },
      text:'',
      checkbox:[],
      keywords:[
        'str1', 'str2', 'str3', 'str4', 'str5'
      ],
      isDisable: false
    }
  },
  methods: {
    ...mapActions(pageStore, ['setPageTitle', 'setPageText']),
    onUpdate (text) {
      this.text = text
    },
    keywordButtonClick(){
      // 타이틀, 텍스트 store저장
      this.text = document.getElementsByClassName('content')[0].innerHTML
      this.setPageTitle(this.title)
      this.setPageText(this.text)
      // console.log(this.$store)

      // 1. 키워드 분석해서 가져온 값 keywords에 채워넣기
      
      // 2.
      document.getElementById('keyword-btn').style.display='none'
      document.getElementById('select-keyword').style.display='block'
    },
    selectKeywordButtonClick(){
      this.isDisable = true
      // select한 키워드들은 this.checkbox에 배열로 담겨있음
    }
  }
}
</script>

<style>
.content{
  height: 50vh;
  overflow: auto;
  border: 0.01rem solid gray;
  border-radius: 5px;
  margin: 0 0 10px 0;
}
.done-btn > v-icon{
 color: black;
}
</style>