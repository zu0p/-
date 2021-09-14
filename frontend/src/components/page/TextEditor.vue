<template>
  <v-container>
    <!-- title -->
    <!-- <v-row>
      <v-text-field
        v-model="title"
        color="blue darken-2"
        :rules="rules.title"
        label="Title"
        required
      ></v-text-field>
    </v-row> -->

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
        <div class="content" name="content" contenteditable="true"></div>
        <div style="text-align: right">
          <v-btn depressed>
            <v-icon color="pink">mdi-account-heart-outline</v-icon>
            <span>감정분석</span>
          </v-btn>
        </div>
      </form>
    </v-row>

  </v-container>
</template>

<script>

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
      text:''
    }
  },
  methods: {
    onUpdate (text) {
      this.text = text
    }
  }
}
</script>

<style>
.content{
  height: 60vh;
  overflow: auto;
  border: 0.01rem solid gray;
  border-radius: 5px;
  margin: 0 0 10px 0;
}
</style>