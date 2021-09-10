<template>
    <v-card 
        elevation="5" 
        class="diary-card" 
        :height="h"
        :width="w"
        @click="clickDiary"
    >
        <v-container fluid>
            <v-row class="card-contents">
                <v-col cols="1" sm="1" md="1" lg="1" id="diary-band" class="diary">
                </v-col>
                <v-col cols="11" sm="11" md="11" lg="11" class="diary">
                    <v-container>
                        <v-row>
                            {{diaryTitle}}
                        </v-row>
                        <v-row>
                            sub title?
                        </v-row>
                    </v-container>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    props:['title','w', 'h'],
    data(){
        return{
            diaryTitle: ''
        }
    },
    created(){
        this.diaryTitle = this.title
    },
    methods:{
        clickDiary(){
            //해당 title의 diary page로 이동
            console.log("click!"+this.diaryTitle)
            // this.$router.push({name: 'Diary', path: `/diary/${this.diaryTitle}`})

            this.$router.push({name: 'Diary', title: this.diaryTitle})
        }
    }
}
</script>

<style>
.diary-card{
    position: relative;
    z-index: 2;
}
.card-contents{
    height: 20rem;
}
.diary{
    max-width: 80%;
}
#diary-band{
    /* height: 350px; */
    height: 100%;
    background-color:rgb(48, 50, 61);
}
</style>