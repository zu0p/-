<template>
  <v-container>
    <div id="image-spinner" style="display:none; text-align: center">
      <v-progress-circular class="mb-5" :size="70" width="7" color="primary" indeterminate> </v-progress-circular>
      <br />
      <span v-if="!isKeywordExist && keywords.length > 0">첫 이미지 생성시 조금 걸릴 수 있어요!</span>
    </div>
    <v-row id="before-select">
      <v-row align="center" class="selector-item item1">
        <v-col>
          <v-btn icon class="text-none" depressed @click="onUploadButtonClick">
            <v-icon>mdi-plus-circle-outline</v-icon>
            <span> 직접 올리기 </span>
          </v-btn>
          <input ref="uploader" class="d-none" type="file" accept="image/*" @change="onFileChanged" />
        </v-col>
      </v-row>
      <v-row align="center" class="selector-item item2">
        <v-col>
          <v-btn icon @click="clickKeywordImage">
            <v-icon>mdi-image-outline</v-icon>
            <span v-if="!isKeywordExist && keywords.length > 0"> 이미지 처음 생성하기 </span>
            <span v-else> 이미지 생성하기 </span>
          </v-btn>
        </v-col>
      </v-row>
      <v-row align="center" class="selector-item item3">
        <v-col>
          <v-btn icon :disabled="isKeywordExist == false" @click="clickRecommendImage">
            <v-icon>mdi-face-man</v-icon>
            <span v-if="!isKeywordExist && keywords.length > 0"> 이 키워드를 처음 선택하신 분이에요! </span>
            <span v-else> 둘러보기 </span>
          </v-btn>
        </v-col>
      </v-row>
    </v-row>
    <v-row id="after-select" class="appear">
      <img :src="preview" class="img-fluid" />
    </v-row>
    <v-row id="create-image" style="display:none">
      <v-container>
        <div v-if="!$vuetify.breakpoint.xs">
          <v-row>
            <v-col>
              <img :src="createImage[0]" class="img-fluid" @click="selectKeywordImage" />
            </v-col>
            <v-col>
              <img :src="createImage[1]" class="img-fluid" @click="selectKeywordImage" />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <img :src="createImage[2]" class="img-fluid" @click="selectKeywordImage" />
            </v-col>
            <v-col>
              <img :src="createImage[3]" class="img-fluid" @click="selectKeywordImage" />
            </v-col>
          </v-row>
        </div>
        <div v-if="$vuetify.breakpoint.xs">
          <v-row>
            <img :src="createImage[0]" class="img-fluid" @click="selectKeywordImage" />
          </v-row>
          <v-row>
            <img :src="createImage[1]" class="img-fluid" @click="selectKeywordImage" />
          </v-row>
          <v-row>
            <img :src="createImage[2]" class="img-fluid" @click="selectKeywordImage" />
          </v-row>
          <v-row>
            <img :src="createImage[3]" class="img-fluid" @click="selectKeywordImage" />
          </v-row>
        </div>
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
const pageStore = "pageStore";

export default {
  name: "ImageSelectorItem",
  data() {
    return {
      image: null,
      imageSelect: false,
      preview: null,
      createImage: [],
    };
  },
  computed: mapState(pageStore, {
    keywords: (state) => state.store.selectedKeywords,
    isKeywordExist: (state) => state.store.isKeywordExist,
  }),
  methods: {
    ...mapActions(pageStore, ["setPageImg", "requestKeywordImage", "requestRecommendImage"]),

    onUploadButtonClick() {
      if (this.keywords.length <= 0) {
        alert("키워드를 선택하지 않았습니다!");
        return;
      }
      this.imageSelect = true;
      window.addEventListener(
        "focus",
        () => {
          this.imageSelect = false;
        },
        { once: true }
      );

      this.$refs.uploader.click();
    },
    onFileChanged(e) {
      this.image = e.target.files[0];

      var reader = new FileReader();
      reader.onload = (e) => {
        this.preview = e.target.result;
      };
      reader.readAsDataURL(this.image);

      // document.getElementById('before-select').style.animation='fade-out 1s'
      // document.getElementById('before-select').style.animationFillMode='forwards'
      document.getElementById("before-select").style.display = "none";

      // document.getElementById('before-select').classList.add('disappear')
      // document.getElementById('after-select').classList.add('appear')

      this.setPageImg(this.image);
    },
    clickKeywordImage() {
      if (this.keywords.length <= 0) {
        alert("키워드를 선택하지 않았습니다!");
        return;
      }
      document.getElementById("before-select").style.display = "none";
      document.getElementById("image-spinner").style.display = "block";
      // 이미지 처음 생성하기
      let param = {
        keyword: this.keywords,
      };
      this.requestKeywordImage(param).then((res) => {
        //난수 생성
        let arr = [];
        while (arr.length < 4) {
          const rand = Math.floor(Math.random() * res.data.length) + 1;
          var flag = false;
          for (let i = 0; i < arr.length; i++) {
            if (arr[i] == rand) {
              flag = true;
              break;
            }
          }
          if (!flag) arr.push(rand);
        }

        //res.data = [] -> 4개만 보여주기
        for (let i = 0; i < 4; i++) {
          let tmp = res.data[i].keyword;
          tmp += arr[i];
          // let tmp = 'chocolate'+(i+1)
          this.createImage.push(require(`@/images/keywords/${tmp}.jpg`));
        }
        document.getElementById("image-spinner").style.display = "none";
        document.getElementById("create-image").style.display = "block";
      });
    },
    selectKeywordImage(e) {
      const images = document.getElementsByClassName("img-fluid");

      for (var i = 0; i < images.length; i++) {
        images[i].style.border = "";
      }

      e.target.style.border = "3px solid cornflowerblue";
      this.image = e.target.src;

      this.setPageImg(this.image);
    },
    clickRecommendImage() {
      this.requestRecommendImage(this.keywords).then((res) => {
        for (let i = 0; i < 4; i++) {
          let tmp = res.data[i].url;
          this.createImage.push(require(`@/images/keywords/${tmp}.jpg`));
        }
        document.getElementById("before-select").style.display = "none";
        document.getElementById("create-image").style.display = "block";
      });
    },
  },
};
</script>

<style>
.selector-item {
  height: 22vh;
  border: 0.01rem solid gray;
  border-radius: 5px;
  margin: 2px 0 2px 0;
  text-align: center;
}

.disappear {
  visibility: hidden;
  width: 100%;
  height: 0vh;
  transition: all 0.3s;
}

.appear {
  visibility: visible;
  width: 100%;
  margin-top: 10px;
  transition: all 0.3s;
}
#image-spinner {
  position: absolute;
  left: 0;
  top: 40%;
  width: 100%;
  height: 100%;
}
</style>
