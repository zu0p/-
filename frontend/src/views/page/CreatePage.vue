<template>
  <v-container style="position:relative; witdh: 100%; height: 100%">
    <v-row v-if="!$vuetify.breakpoint.xs">
      <v-col class="wrapper">
        <text-editor :pDiaryId="diaryId" :pPageId="pageId"/>
      </v-col>

      <v-col class="wrapper">
        <image-selector :pDiaryId="diaryId" :pPageId="pageId"/>
      </v-col>
    </v-row>
    <v-row v-if="$vuetify.breakpoint.xs" style="height:auto;">
      <v-col class="wrapper">
        <text-editor :pDiaryId="diaryId" :pPageId="pageId"/>
        <image-selector :pDiaryId="diaryId" :pPageId="pageId"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ImageSelector from '../../components/page/ImageSelector.vue'
import TextEditor from '../../components/page/TextEditor.vue'
export default {
  props:['isEdit', 'diaryId', 'pageId'],
  name: 'CreatePage',
  components: {
    TextEditor,
    ImageSelector,
  },
  data(){
    return{
      imageSelect: false,
    }
  },
  created(){ 
    console.log(this.title+"created")
    //이건 나중에 watch로 바꿔야하나 => 선택하면 emit으로 받아서 this.imageSelect를 바꿔주고 그때 routing해도 되겠다 초기에는 무조건 false니까
    // if(!this.imageSelect)this.$router.push({name: 'ImageSelect'})
  },
  methods:{
  }
}
</script>

<style>
.wrapper{
  background-color: white;
  opacity: 0.8;
  margin: 0 5px 0 5px;
  position: relative;
  z-index: 2;
  height: auto;
}
</style>