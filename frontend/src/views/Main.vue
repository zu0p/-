<template>
  <v-app>
    <v-container>
        <!-- header -->
        <v-row>
            <main-header />
        </v-row>

        <!-- contents -->
        <v-row>
            <v-container fluid>
                <v-row>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="12" md="12" lg="12">
                                <slider />
                            </v-col>
                        </v-row>
                    </v-container>
                </v-row>
                <!-- <v-row>
                    <v-flex>
                        <div>D</div>
                    </v-flex>
                </v-row> -->
            </v-container>
        </v-row>
        
        <v-row>
            <main-footer />
        </v-row>
    </v-container>
  </v-app>
</template>

<script>
// import MainNavbar from '@/components/main/MainNavbar.vue'
import MainHeader from '../components/main/MainHeader.vue'
import MainFooter from '../components/main/MainFooter.vue'
import {reactive} from 'vue'
import Slider from '../components/main/Slider.vue'

export default {
  components: { MainHeader, MainFooter, Slider },
  mounted(){
      console.log("hiyo")
  }
}
</script>

<style>
body{
    margin:0; 
    padding:0; 
    width:100%; 
    height:100%
}
.diary-container{
    display: flex;
    overflow-x: auto;
    width: 90%;
}
.diary-container::-webkit-scrollbar {
    display: none;
}
#slider{
    position: relative;
    z-index: 2;
}
</style>