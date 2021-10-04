<template>
  <v-container>
      <v-row>
        <page-flip />
      </v-row>
      <v-row>
      </v-row>
  </v-container>
</template>

<script>
import PageFlip from '../../components/page/PageFlip.vue'
export default{
  name:'DetailView',
  components:{
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