<template>
    <v-card 
        elevation="5" 
        class="diary-card" 
        :height="h"
        :width="w"
        @click="clickDiary"
    >   
        <v-container fluid class="diary-wrapper" :style="`background-image: url(${curDiary.diaryImage})`"> 
            <v-row class="card-contents">
                <v-col cols="1" sm="1" md="1" lg="1" id="diary-band" class="diary">
                </v-col>
                <v-col cols="11" sm="11" md="11" lg="11" class="diary">  
                    <v-row id="buttons" justify="end">
                        <!-- 수정 form dialog -->
                        <v-dialog
                        v-model="editDialog"
                        persistent
                        max-width="290"
                        >
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn icon v-bind="attrs" v-on="on">
                                    <v-icon color="blue darken-3">mdi-pencil-outline</v-icon>
                                </v-btn>
                            </template>
                            <add-diary :isAdd="false" :id="curDiary.id" @closeAddDialog='onCloseEditDialog'/>
                        </v-dialog>

                        <!-- 삭제 확인 dialog -->
                        <v-dialog
                        v-model="deleteDialog"
                        persistent
                        max-width="290"
                        >
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn icon  v-bind="attrs" v-on="on">
                                    <v-icon color="red darken-3">mdi-trash-can-outline</v-icon>
                                </v-btn>
                            </template>
                            <delete-diary :id="curDiary.id" @cancelDeleteDialog="onDeleteDialog"/>
                        </v-dialog>
                    </v-row>

                    <!-- 다이어리 제목과 설명 -->
                    <v-container mt-5>        
                        <v-row>
                            <h3 style="color:white;">{{curDiary.diaryName}}</h3>
                        </v-row>
                        <v-row>
                            <p style="color:white;">{{curDiary.diaryDesc}}</p>
                            {{curDiary.id}}
                        </v-row>
                    </v-container>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
import AddDiary from './AddDiary.vue'
import DeleteDiary from './DeleteDiary.vue'
import { mapActions } from 'vuex'
const pageStore='pageStore'
const diaryStore='diaryStore'

export default {
    components: { 
        DeleteDiary,
        AddDiary,
    },
    props:['diary','w', 'h'],
    data(){
        return{
            curDiary: null,
            diaryTitle: '',
            deleteDialog: false,
            editDialog: false
        }
    },
    created(){
        this.curDiary = this.diary
        // this.diaryTitle = this.title
    },
    methods:{
        ...mapActions(pageStore, ['requestPageList', 'setPageList']),
        ...mapActions(diaryStore, ['setDiaryId']),
        clickDiary(){
            this.setDiaryId(this.curDiary.id)
            //해당 title의 diary page로 이동
            // console.log("click!"+this.diaryTitle)
            this.requestPageList(this.curDiary.id)
                .then(res=>{
                    // console.log(res)

                    if(res.data.length==0){
                        // 선택한 diary에 page가 하나도 없으면 
                        // => beforeCreate(path: /diary/:id/first)로 라우팅
                        this.$router.push({path:`pages/${this.curDiary.diaryName}/first`})
                    }
                    else{
                        // 페이지 저장
                        this.setPageList(res.data)
                        // console.log(this.$store._modules.root._children.pageStore.state.store.pageList)
                        this.$router.push({path:`pages/${this.curDiary.diaryName}/detailView`})
                    }
                })
        },
        // editClick(e){
        //     e.stopPropagation()
        // },
        onDeleteDialog(){
            this.deleteDialog = false
        },
        onCloseEditDialog(){
            this.editDialog = false
        }
    }
}
</script>

<style>
.diary-wrapper{
    margin: 0;
    padding: 0;
}
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
#buttons{
    position: relative;
    z-index: 100;
}
</style>