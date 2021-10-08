<template>
  <div>
    <img id="bg" src="../../images/night.jpg" />
    <v-container class="pageList" fullscreen>
      <div id="user-menu ">
        <user-menu />
      </div>
      <div id="diary-menu">
        <diary-menu />
      </div>
      <VueSlickCarousel class="pageList mt-10" v-bind="settings" ref="carousel" v-if="pages.length">
        <div v-for="(page, idx) in pages" :key="page.id">
          <v-card class="ma-1">
            <v-img
              :src="page.pageImage"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="330px"
              aspect-ratio="1"
              @mouseenter="Html2Text(page.pageContent, page.id)"
              @mouseover="page.isMouseOver = true"
              @mouseleave="page.isMouseOver = false"
            >
              <v-card-title>
                <v-row>
                  <v-col cols="6">
                    {{ page.pageTitle }}
                  </v-col>
                  <v-col cols="6">
                    <v-row justify="end" v-if="page.isMouseOver == true">
                      <v-btn icon style="z-index:1000" @click="clickEditPage(page)">
                        <v-icon color="white">mdi-pencil-outline</v-icon>
                      </v-btn>
                      <v-btn icon @click="clickDeletePage(page, idx)">
                        <v-icon color="white">mdi-trash-can-outline</v-icon>
                      </v-btn>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card-title>

              <v-expand-transition v-if="page.isMouseOver == true">
                <div class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal white--text">
                  <div :id="page.id" class="page-content "></div>
                </div>
              </v-expand-transition>
            </v-img>
          </v-card>
        </div>
      </VueSlickCarousel>

      <v-row>
        <main-footer />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import VueSlickCarousel from "vue-slick-carousel";
import MainFooter from "../../components/main/MainFooter.vue";
import UserMenu from "@/components/main/UserMenu.vue";
import DiaryMenu from "@/components/page/DiaryMenu.vue";
import DeleteDiary from "@/components/main/DeleteDiary.vue";
import { mapActions } from "vuex";
const pageStore = "pageStore";

export default {
  name: "Params",
  components: { VueSlickCarousel, DiaryMenu, MainFooter, UserMenu, DeleteDiary },
  props: {
    diaryId: {
      type: Number,
    },
  },
  data() {
    return {
      settings: {
        infinite: false,
        slidesToShow: 4,
        speed: 500,
        rows: 2,
        slidesToScroll: 3,
        arrows: true,
        dots: true,
      },
      cards: [
        { title: "Pre-fab homes", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg", pageContent: "설명입니다.1", isMouseOver: false },
        { title: "Favorite road trips", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg", pageContent: "설명입니다.2", isMouseOver: false },
        { title: "Best airlines", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg", pageContent: "설명입니다.3", isMouseOver: false },
        { title: "1", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg", pageContent: "설명입니다.4", isMouseOver: false },
        { title: "2", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg", pageContent: "설명입니다.5", isMouseOver: false },
        { title: "3", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg", pageContent: "설명입니다.6", isMouseOver: false },
        { title: "4", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg", pageContent: "설명입니다.7", isMouseOver: false },
        { title: "hello", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg", pageContent: "설명입니다.8", isMouseOver: false },
        { title: "6", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg", pageContent: "설명입니다.9", isMouseOver: false },
      ],
      pages: [],
      deleteDialog: false,
    };
  },
  created() {
    this.requestPageList(this.$route.params.diaryId)
      .then((res) => {
        if ((res.statusText = "OK")) {
          for (let i = 0; i < res.data.length; i++) {
            var arr = res.data[i];
            arr.isMouseOver = false;
            this.pages.push(arr);
          }
        }
      })
      .catch((e) => {
        console.log(e);
        if (e.response.status == 422) {
          alert("잘못된 요청입니다.");
          window.location("/main");
        }
      });
  },
  methods: {
    ...mapActions(pageStore, ["requestPageList", "requestDeletePage", "deletePage"]),
    pageClick(page) {
      alert(page.pageTitle);
      console.log(page);
    },
    mouseOver(card) {
      console.log(card.pageContent);
    },
    Html2Text(str, id) {
      const div = document.getElementById(id);
      div.innerHTML = str;
      // document.getElementById(id).appendChild(temp.firstChild);
      // document.getElementById(id).appendChild(str);
      // const replaceStr = str.replace(/<[^>]*>?/gm, "\n");
      // return replaceStr.replace(/\n$/gm, "");
    },
    clickEditPage(page) {
      // 수정페이지로 가
      this.$router.push({ name: "CreatePage", params: { isEdit: true, diaryId: page.diaryId, pageId: page.id } });
    },
    clickDeletePage(page, idx) {
      console.log(idx);
      const res = window.confirm("정말 이 일기를 삭제하실건가요?.\n삭제된 일기는 복구할 수 없습니다.");
      if (!res) return;
      const param = {
        diaryId: page.diaryId,
        pageId: page.id,
      };
      this.requestDeletePage(param)
        .then((res) => {
          if (res.statusText == "OK") {
            alert("일기가 삭제되었습니다.");
            this.pages.splice(idx, 1);
          }
        })
        .catch((e) => {
          console.log(e.response);
        });
    },
  },
};
</script>
<style scoped>
#bg {
  position: fixed;
  top: 0;
  left: 0;
  object-fit: cover;
  z-index: 1;
}
.pageList {
  z-index: 2;
  position: relative;
}
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.7;
  width: 100%;
  height: 200px;
}
#page-buttons {
  position: absolute;
  top: 24%;
  left: 80%;
}
.page-content {
  width: 70%;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 6; /* 텍스트를 자를 때 원하는 단위 ex) 3줄 */
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
