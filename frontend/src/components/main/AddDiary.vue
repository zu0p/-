<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Create New Diary</span>
    </v-card-title>
    <v-card-text>
      <v-container>
        <v-row>
          <v-col >
            <v-text-field
              label="Title*"
              required
              v-model="diary.diaryName"
            ></v-text-field>
          </v-col>          
        </v-row>

        <v-row>
          <v-col>
            <v-text-field
              label="Description*"
              hint="간단한 설명을 적어보세요"
              persistent-hint
              required
              v-model="diary.diaryDesc"
            ></v-text-field>
          </v-col>          
        </v-row>
        <v-row>
          <v-col>        
            <v-checkbox
              v-model="diary.diaryShare"
              label="Share Diary"
            ></v-checkbox>
          </v-col>
          <v-col>
            <v-file-input
              accept="image/*"
              label="Diary Cover Image*"
              v-model="diary.diaryImage"
            ></v-file-input>
          </v-col>
        </v-row>
      </v-container>
      <small>*indicates required field</small>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="blue darken-1"
        text
        @click="closeClick"
      >
        Close
      </v-btn>
      <v-btn
        color="blue darken-1"
        text
        @click="createClick"
      >
        Create
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'
const diaryStore = 'diaryStore'

export default {
  data(){
    return{
      diary:{
        diaryName: '',
        diaryImage: {},
        diaryDesc: '',
        diaryShare: false
      }
    }
  },
  updated(){
    // console.log(this.diary.diaryImage)
  },
  methods:{
    ...mapActions(diaryStore,['createDiary', 'addDiary']),
    closeClick(){
      this.$emit('closeAddDialog')
    },
    createClick(){
      console.log(this.diary)
      const form = new FormData()
      form.append('diaryName', this.diary.diaryName)
      form.append('diaryImage', this.diary.diaryImage)
      form.append('diaryDesc', this.diary.diaryDesc)
      form.append('diaryShare', this.diary.diaryShare)

      //actions 불러서 새로 생성
      this.createDiary(form)
        .then(res=>{
          console.log(res)
          this.addDiary(res.data)
          this.$emit('closeAddDialog')
        })
    }
  }
}
</script>

<style>

</style>