<template>
  <v-container>
    <v-row style="margin-top:15px">
      <h5>이미지 선택</h5>
    </v-row>
    <!-- 이미지 선택-->
    <v-row>
      <router-view />
      <v-col style="text-align:right">
      <v-btn depressed @click="previewButtonClick">
        <span>미리보기</span>
      </v-btn>
      </v-col>
    </v-row>
  </v-container>  
</template>

<script>
export default {
  name: 'ImageSelector',
  methods: {
    previewButtonClick(){
      // routing to preview page
      // check image validatioin
      this.$router.push({name:'Preview'})
    }
  }
}
</script>

<style>

</style>