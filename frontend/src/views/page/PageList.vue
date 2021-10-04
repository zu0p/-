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
      <VueSlickCarousel class="pageList" v-bind="settings">
        <div v-for="card in cards" :key="card.title">
          <v-card class="ma-1">
            <v-img
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="330px"
              aspect-ratio="1"
              @click="pageClick(card)"
              @mouseover="card.isMouseOver = true"
              @mouseleave="card.isMouseOver = false"
            >
              <v-card-title v-text="card.title"></v-card-title>
              <v-expand-transition>
                <div v-if="card.isMouseOver == true" class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal text-h2 white--text">
                  $14.99
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

export default {
  components: { VueSlickCarousel, DiaryMenu, MainFooter, UserMenu },
  data: () => ({
    settings: {
      infinite: false,
      slidesToShow: 4,
      speed: 500,
      rows: 2,
      slidesToScroll: 4,
      arrows: true,
      dots: true,
    },
    icons: ["mdi-rewind", "mdi-play", "mdi-fast-forward"],
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
    transparent: "rgba(255, 255, 255, 0)",
  }),

  methods: {
    pageClick(card) {
      alert(card.title);
    },
    mouseOver(card) {
      console.log(card.pageContent);
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
