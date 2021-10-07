<template>
  <v-container>
      <v-row>
        <page-flip />
      </v-row>
  </v-container>
</template>

<script>
import PageFlip from '../../components/page/PageFlip.vue'
export default{
  name:'DetailView',
  props:['diaryId'],
  components:{
    PageFlip,
  },
  data(){
    return{
        id: null
    }
  },
  created(){   
  },
  methods:{

  }
}

</script>

<style>
</style>