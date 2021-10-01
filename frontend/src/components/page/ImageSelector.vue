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
import {mapActions} from 'vuex'
const pageStore = 'pageStore'
export default {
  name: 'ImageSelector',
  methods: {
    ...mapActions(pageStore, ['setIsKeywordSearch']),
    previewButtonClick(){
      let key = this.$store._modules.root._children.pageStore.state.store.isKeywordSearch
      let img = this.$store._modules.root._children.pageStore.state.store.page_img
      if(key && img!=null){ // 키워드 분석 했고 && 이미지도 선택해야 프리뷰로 넘어감
        this.setIsKeywordSearch() //키워드 다시 false로
        // routing to preview page
        // check image validatioin
        this.$router.push({name:'Preview'})
      }
      else{
        alert('글을 작성하고 이미지를 선택하세요!')
      }
    }
  }
}
</script>

<style>

</style>