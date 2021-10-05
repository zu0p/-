<template>
  <div>
    <img id="bg" src="../../images/night.jpg" />
    <v-container class="pageList" fullscreen>
      <div id="user-menu">
        <user-menu />
      </div>
      <div id="diary-menu">
        <diary-menu />
      </div>
      <VueSlickCarousel class="pageList" v-bind="settings" ref="carousel" v-if="pages.length">
        <div v-for="page in pages" :key="page.id">
          <v-card class="ma-1">
            <v-img
              :src="page.pageImage"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="330px"
              aspect-ratio="1"
              @click="pageClick(page)"
              @mouseover="page.isMouseOver = true"
              @mouseleave="page.isMouseOver = false"
            >
              <v-card-title v-text="page.pageTitle"></v-card-title>
              <v-expand-transition>
                <div v-if="page.isMouseOver == true" class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal white--text">
                  {{ Html2Text(page.pageContent) }}
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
import { mapActions } from "vuex";
const pageStore = "pageStore";

export default {
  name: "Params",
  components: { VueSlickCarousel, DiaryMenu, MainFooter, UserMenu },
  props: {
    diaryId: {
      type: Number,
    },
  },
  data: () => ({
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
  }),
  created() {
    this.requestPageList(this.$route.params.diaryId)
      .then((res) => {
        if ((res.statusText = "OK")) {
          for (let i = 0; i < res.data.length; i++) {
            var arr = res.data[i];
            arr.isMouseOver = false;
            this.pages.push(arr);
          }
          // this.pages = res.data;
          console.log(this.pages);
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
    ...mapActions(pageStore, ["requestPageList"]),
    pageClick(page) {
      alert(page.pageTitle);
      console.log(this.diaryId);
    },
    mouseOver(card) {
      console.log(card.pageContent);
    },
    Html2Text(str) {
      return str.replace(/<[^>]*>?/gm, "");
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
</style>
