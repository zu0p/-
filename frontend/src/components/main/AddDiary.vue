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
            ></v-text-field>
          </v-col>          
        </v-row>
        <v-row>
          <v-col>        
            <v-checkbox
              v-model="isPublic"
              label="Public diary"
            ></v-checkbox>
          </v-col>
          <v-col>
            <v-file-input
              accept="image/*"
              label="Diary Cover Image*"
              v-model="cover"
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
export default {
  data(){
    return{
      isPublic: false,
      cover: {}
    }
  },
  updated(){
    console.log(this.cover)
  },
  methods:{
    closeClick(){
      this.$emit('closeAddDialog')
    },
    createClick(){
      //actions 불러서 새로 생성
    }
  }
}
</script>

<style>

</style>