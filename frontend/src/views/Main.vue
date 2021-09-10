<template>
  <v-app>
    <!-- <main-header />
    <main-navbar />
    <v-content>
        <div class="diary-container">
            <diary />
            <diary />
            <diary />
            
        </div>
        
    </v-content>
    <main-footer /> -->
    
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
                            <v-col cols="0" sm="2" md="2" lg="2">
                            </v-col>
                            <v-col cols="12" sm="8" md="8" lg="8">
                                <!-- <diary /> -->
                                <!-- <v-slide-group
                                    class="pa-4"
                                    center-active
                                    show-arrows
                                    id="slider"
                                    >
                                    <v-slide-item
                                        v-for="n in 5"
                                        :key="n"
                                    >
                                        <diary />
                                    </v-slide-item>
                                    </v-slide-group> -->
                                <slider />
                            </v-col>
                            <v-col cols="0" sm="2" md="2" lg="2">
                            </v-col>
                        </v-row>
                    </v-container>
                </v-row>
                <v-row>
                    <v-flex>
                        <div>D</div>
                    </v-flex>
                </v-row>
            </v-container>
        </v-row>
        <v-row>
            <main-footer />
        </v-row>
    </v-container>
  </v-app>
</template>

<script>
import MainNavbar from '@/components/main/MainNavbar.vue'
import MainHeader from '../components/main/MainHeader.vue'
import MainFooter from '../components/main/MainFooter.vue'
import Diary from '../components/main/Diary.vue'
import {reactive} from 'vue'
import Slider from '../components/main/Slider.vue'

export default {
  components: { MainNavbar, MainHeader, MainFooter, Diary, Slider },
  setup(){
    const state = reactive({
        diarys:[
            {id:1},
            {id:2},
            {id:3}
        ]
    })
    return {state}
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