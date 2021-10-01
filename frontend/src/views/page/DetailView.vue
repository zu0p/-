<template>
  <v-container>
      <v-row>
        <!-- <detail-page /> -->
        <page-flip />
      </v-row>
      <v-row>
      </v-row>
  </v-container>
</template>

<script>
import DetailPage from '../../components/page/DetailPage.vue'
import PageFlip from '../../components/page/PageFlip.vue'
export default{
  name:'DetailView',
  components:{
    DetailPage,
    PageFlip,
  },
  data(){
    return{
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