<template>
  <v-container class="diary-menu-container">
    <v-row>
      <v-menu transition="fade-transition">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="menu-button"
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-horizontal</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon 
                  v-bind="attrs"
                  v-on="on"
                  @click="goToHome()"
                >
                  <v-icon>mdi-home</v-icon>
                </v-btn>
              </template>
              <span>home</span>
            </v-tooltip>
          </v-list-item>

          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon 
                  v-bind="attrs"
                  v-on="on"
                  @click="showDiaryList()"
                >
                  <v-icon>mdi-border-all</v-icon>
                </v-btn>
              </template>
              <span>diary list</span>
            </v-tooltip>
          </v-list-item>
          
          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon 
                  v-bind="attrs"
                  v-on="on"
                  @click="goEditDiary()"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>edit diary</span>
            </v-tooltip>
          </v-list-item>

          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon 
                  v-bind="attrs"
                  v-on="on"
                  @click="goDeleteDiary()"
                >
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </template>
              <span>delete diary</span>
            </v-tooltip>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-row>
  </v-container>

</template>

<script>
export default {
  name: 'DiaryMenu',
  methods:{
    goToHome(){
      this.$router.push({name:'Main'})
    },
    showDiaryList(){

    },
    goEditDiary(){

    },
    goDeleteDiary(){

    }
  }
}
</script>

<style>
.menu-button{
  background-color: gray;
  color: white;
  margin: 0 0 10px 0;
}
.menu-button:hover{
  background-color: white;
  color: gray;
  margin: 0 0 10px 0;
}
</style>