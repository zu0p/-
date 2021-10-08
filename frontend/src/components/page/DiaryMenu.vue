<template>
  <v-container class="diary-menu-container">
    <v-row>
      <v-menu transition="fade-transition">
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="menu-button" icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-horizontal</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on" @click="goToHome()">
                  <v-icon>mdi-home</v-icon>
                </v-btn>
              </template>
              <span>home</span>
            </v-tooltip>
          </v-list-item>

          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on" @click="showDiaryList()">
                  <v-icon>mdi-border-all</v-icon>
                </v-btn>
              </template>
              <span>일기 목록 한눈에 보기</span>
            </v-tooltip>
          </v-list-item>

          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on" @click="showPages()">
                  <v-icon>mdi-book-open-page-variant-outline</v-icon>
                </v-btn>
              </template>
              <span>일기 한장씩 보기</span>
            </v-tooltip>
          </v-list-item>

          <v-list-item>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon v-bind="attrs" v-on="on" @click="writeNewPage()">
                  <v-icon>mdi-pencil-plus</v-icon>
                </v-btn>
              </template>
              <span>일기 추가</span>
            </v-tooltip>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
const diaryStore = "diaryStore";
export default {
  name: "DiaryMenu",
  computed: {
    ...mapState(diaryStore, {
      diaryId: (state) => state.store.diaryId,
    }),
  },
  methods: {
    goToHome() {
      // this.$router.push({name:'Main'})
      window.location = "/main";
    },
    showDiaryList() {
      this.$router.push({
        name: "PageList",
        params: { diaryId: this.diaryId },
      });
      // window.location = "/pageList";
    },
    showPages() {
      this.$router.push({name: 'DetailView', params:{diaryId: this.diaryId}})
    },
    writeNewPage() {
      this.$router.push({name:'CreatePage'})
    },
  },
};
</script>

<style>
.menu-button {
  background-color: gray;
  color: white;
  margin: 0 0 10px 0;
}
.menu-button:hover {
  background-color: white;
  color: gray;
  margin: 0 0 10px 0;
}
</style>
