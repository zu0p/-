<template>
  <v-container id="preview-wrapper" ref="wrapper">
    <img id="img-bg" :src="preview" />
    <v-row style="height:95%">
      <div
        id="ball"
        draggable
        @dragstart="dragStart"
        @drag="dragging"
        @dragend="dragEnd"
        name="content"
        contenteditable="false"
        :style="{ top: cordY + 'px', left: cordX + 'px' }"
      ></div>
    </v-row>
    <v-row>
      <v-btn color="blue-grey" @click="clickWritePage">
        <v-icon color="white">mdi-application-edit-outline</v-icon>
        <span style="color:white;">DONE</span>
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
import draggable from "vuedraggable";
const pageStore = "pageStore";
const diaryStore = "diaryStore";
export default {
  components: {
    draggable,
  },
  props: ["pDiaryId", "pPageId"],
  data() {
    return {
      text: "",
      imgFile: {},
      preview: null,
      plainText: "",
      pageId: null,
      propsDiary: null,
      cordY: 200,
      cordX: 200,
      divY: 0,
      divX: 0,
      draging: false,
    };
  },

  computed: {
    ...mapState(pageStore, {
      pageText: (state) => state.store.page_text,
      pageTitle: (state) => state.store.page_title,
      pageImage: (state) => state.store.page_img,
    }),
    ...mapState(diaryStore, {
      diaryId: (state) => state.store.diaryId,
    }),
  },
  mounted() {
    if (this.pDiaryId) {
      this.propsDiary = this.pDiaryId;
      this.pageId = this.pPageId;
    }

    let ball = document.getElementById("ball");
    ball.addEventListener("dragstart", function() {
      return false;
    });

    this.text = this.pageText;
    this.imgFile = this.pageImage;

    document.getElementById("ball").innerHTML = this.text;

    if (typeof this.imgFile == "string") this.preview = this.imgFile;
    else {
      var reader = new FileReader();
      reader.onload = (e) => {
        this.preview = e.target.result;
      };
      reader.readAsDataURL(this.imgFile);
    }
  },
  methods: {
    ...mapActions(pageStore, ["requestCreateDiary", "requestUpdatePage", "requestPageList", "setPageList", "addPage", "updatePage"]),

    async convertURLtoFile(url) {
      const response = await fetch(url);
      const data = await response.blob();
      const ext = url.split(".").pop(); // url 구조에 맞게 수정할 것
      const filename = url.split("/").pop(); // url 구조에 맞게 수정할 것
      const metadata = { type: `image/${ext}` };
      return new File([data], filename, metadata);
    },

    ifUrlString(textposition) {
      this.convertURLtoFile(this.pageImage).then((res) => {
        const form = new FormData();
        form.append("pageTitle", this.pageTitle);
        form.append("pageContent", this.pageText);
        form.append("pageShare", false);
        form.append("pageImage", res);
        form.append("top", textposition.y);
        form.append("left", textposition.x);

        for (var pair of form.entries()) {
          console.log(pair[0] + ", " + pair[1]);
        }
        console.log(res);

        if (this.propsDiary) {
          form.append("diaryId", this.propsDiary);
          form.append("pageId", this.pageId);
          this.requestUpdatePage(form).then((res) => {
            console.log(res);
            const newPage = {
              diaryId: this.propsDiary,
              id: this.pageId,
              top: textposition.y,
              left: textposition.x,
              pageTitle: this.pageTitle,
              pageContent: this.pageText,
              pageImage: res.data.pageImage,
              pageOwnerId: "",
              pageShare: false,
            };
            this.updatePage(newPage);

            this.$router.push({ name: "DetailView" });
            // alert('수정이 완료되었습니다 홈으로 돌아갑니다')
            // window.location.href = `/main`
          });
        }

        // 일기 생성
        else {
          form.append("diaryId", this.diaryId);
          this.requestCreateDiary(form).then((res) => {
            console.log(res);

            const newPage = {
              diaryId: this.diaryId,
              id: res.data.id,
              top: textposition.y,
              left: textposition.x,
              pageTitle: this.pageTitle,
              pageContent: this.pageText,
              pageImage: res.data.pageImage,
              pageOwnerId: "",
              pageShare: false,
            };
            this.addPage(newPage);

            this.$router.push({ name: "DetailView" });
          });
        }
      });
    },

    clickWritePage() {
      // 이미지+텍스트+위치 create page
      const textbox = document.getElementById("ball");
      const textposition = textbox.getBoundingClientRect();
      console.log(typeof this.pageImage);
      if (typeof this.pageImage == "string") {
        this.ifUrlString(textposition);
        return;
      }

      // console.log(typeof this.pageImage);
      const form = new FormData();
      form.append("pageTitle", this.pageTitle);
      form.append("pageContent", this.pageText);
      form.append("pageShare", false);
      form.append("pageImage", this.pageImage);
      form.append("top", textposition.y);
      form.append("left", textposition.x);
      console.log(this.pageImage);
      // console.log(form)
      // 일기 수정
      if (this.propsDiary) {
        form.append("diaryId", this.propsDiary);
        form.append("pageId", this.pageId);
        this.requestUpdatePage(form).then((res) => {
          console.log(res);
          const newPage = {
            diaryId: this.propsDiary,
            id: this.pageId,
            top: textposition.y,
            left: textposition.x,
            pageTitle: this.pageTitle,
            pageContent: this.pageText,
            pageImage: res.data.pageImage,
            pageOwnerId: "",
            pageShare: false,
          };
          this.updatePage(newPage);

          this.$router.push({ name: "DetailView" });
          // alert('수정이 완료되었습니다 홈으로 돌아갑니다')
          // window.location.href = `/main`
        });
      }

      // 일기 생성
      else {
        form.append("diaryId", this.diaryId);
        this.requestCreateDiary(form).then((res) => {
          console.log(res);

          const newPage = {
            diaryId: this.diaryId,
            id: res.data.id,
            top: textposition.y,
            left: textposition.x,
            pageTitle: this.pageTitle,
            pageContent: this.pageText,
            pageImage: res.data.pageImage,
            pageOwnerId: "",
            pageShare: false,
          };
          this.addPage(newPage);

          this.$router.push({ name: "DetailView" });
        });
      }
    },
    dragStart(e) {
      let ball = document.getElementById("ball");

      let width = (window.innerWidth - this.$refs.wrapper.clientWidth) / 2;
      let height = (window.innerHeight - this.$refs.wrapper.clientHeight) / 2;
      var img = new Image();

      e.dataTransfer.setDragImage(img, 0, 0);
      this.divX = e.pageX - ball.getBoundingClientRect().left + width;
      this.divY = e.pageY - ball.getBoundingClientRect().top + height;
      this.draging = true;
    },
    dragging(e) {
      this.cordY = e.pageY - this.divY;
      this.cordX = e.pageX - this.divX;
    },
    dragEnd(e) {
      this.draging = false;
      this.cordY = e.pageY - this.divY;
      this.cordX = e.pageX - this.divX;
    },
  },
};
</script>

<style>
/* #ball {
  min-width: 50px;
  min-width: 50px;
  text-align: center;
  border: 3px dashed yellow;
  z-index: 100;
  position: absolute;
  top: 50%;
  left: 50%;
} */
#img-bg {
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;

  width: 100%;
  height: 90%;

  background-position: center;
  background-size: cover;
}

#preview-wrapper {
  width: 100% !important;
  height: 100% !important;
}
#mydiv {
  display: inline-block;
  position: absolute;
  z-index: 9;
  text-align: center;
  overflow: auto;
}

#ball {
  width: fit-content;
  position: absolute;
  text-align: center;
  overflow: auto;
  z-index: 9;
  padding: 10px;
  cursor: move;
  z-index: 10;
  border: 3px dashed yellow;
}
/* #preview-wrapper{
  position: absolute;
  z-index: -1;
  left: 0;
  top: 0;
  width: 100vh;
  height: 100vh;
  margin: 0;
  min-height: 100%;
  background-position: center;
  background-size: cover;
} */
/* :style="`background-image: url(${preview})`" id="preview-wrapper" */
</style>
