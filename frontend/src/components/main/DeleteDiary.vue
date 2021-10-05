<template>
  <v-card>
    <v-card-title class="text-h5">
      정말 이 {{name}}를 삭제하실건가요?
    </v-card-title>
    <v-card-text>
      삭제된 {{name}}는 복구할 수 없습니다.
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        text
        @click="clickCancel"
      >
        cancel
      </v-btn>

      <v-dialog
        transition="dialog-top-transition"
        max-width="600"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-model="dialog"
            v-bind="attrs"
            v-on="on"
            color="red darken-3"
            text
          >
            delete
          </v-btn>
        </template>
        <template :v-slot:default="dialog">
          <v-card color="red darken-3">
            <v-container>
              <v-row>
                <v-col cols="1">
                  <v-icon color="white">mdi-alert-circle-outline</v-icon>
                </v-col>
                <v-col style="color:white;">
                {{name}} <strong>삭제</strong>가 완료 되었습니다.
                </v-col>
                <v-col align="right">
                  <v-btn
                    text
                    color="white"
                    @click="clickDelete"
                  >
                    close
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </template>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'
const diaryStore = 'diaryStore'
const pageStore = 'pageStore'
export default {
  props:['id', 'isPage', 'diaryId'],
  data(){
    return{
      dialog: false,
      name: ''
    }
  },
  mounted(){
    if(this.isPage){
      this.name = '일기'
    }
    else this.name = '다이어리'
  },
  methods:{
    ...mapActions(diaryStore, ['requestDeleteDiary', 'deleteDiary']),
    ...mapActions(pageStore, ['requestDeletePage', 'deletePage']),
    clickCancel(){
      this.$emit('cancelDeleteDialog')
    },
    clickDelete(){
      this.dialog = false

      // 페이지 제거일 때
      if(this.isPage){
        // console.log('일기 제거')
        // console.log(this.diaryId)
        const param={
          "diaryId": this.id,
          "pageId": this.diaryId
        }
        this.requestDeletePage(param)
          .then(res=>{
            if(res.statusText=='OK'){
              // console.log(res)
              // console.log(this.diaryId)
              this.deletePage(this.diaryId)
            }
            

            // dialog 닫기
            this.$emit('cancelDeleteDialog')
          })
          .catch(e=>{
            console.log(e.response)
          })
      }

      // 다이어리 제거일 때
      else{
        // console.log('다이어리 제거')
        const param={
          "diaryId": this.id
        }
        this.requestDeleteDiary(param)
          .then(res=>{
            // console.log(res)
            if(res.statusText=='OK')
              this.deleteDiary(this.id)

            // dialog 닫기
            this.$emit('cancelDeleteDialog')
          })
          .catch(e=>{
            console.log(e.response)
          })
      }
    }
  }
}
</script>

<style>

</style>