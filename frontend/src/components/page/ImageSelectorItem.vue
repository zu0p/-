<template>
  <v-container>
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
            <span> 이미지 생성하기 </span>
          </v-btn>
        </v-col>
      </v-row>
      <v-row align="center" class="selector-item item3">
        <v-col>
          <v-btn icon>
            <v-icon>mdi-face-man</v-icon>
            <span> 둘러보기 </span>
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
  }),
  methods: {
    ...mapActions(pageStore, ["setPageImg", "requestKeywordImage"]),
    onUploadButtonClick() {
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
      console.log(this.image);

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
      // selectedKeyword 가져와서 이미지 요청
      // console.log(this.keywords[0])
      if (this.keywords.length <= 0) {
        alert("키워드를 선택하지 않았습니다!");
      } else {
        // this.createImage =[
        //       "https://tympanus.net/Development/BookBlock/images/demo1/1.jpg",
        //       "https://tympanus.net/Development/BookBlock/images/demo1/2.jpg",
        //       "https://tympanus.net/Development/BookBlock/images/demo1/2.jpg",
        //       "https://tympanus.net/Development/BookBlock/images/demo1/1.jpg",
        //     ]
        //     document.getElementById('before-select').style.display='none'
        //     document.getElementById('create-image').style.display='block'
        let param = {
          keyword: this.keywords[0],
        };
        this.requestKeywordImage(param).then((res) => {
          console.log(res.data);
          //res.data = [] -> 4개만 보여주기
          for (let i = 0; i < 4; i++) {
            console.log(res.data)
            // let tmp = res.data[i].url;
            let tmp = 'chocolate'+(i+1)
            console.log(tmp);
            this.createImage.push(require(`@/images/keywords/${tmp}.jpg`));
          }
          console.log(this.createImage);
          document.getElementById("before-select").style.display = "none";
          document.getElementById("create-image").style.display = "block";
        });
      }
    },
    selectKeywordImage(e) {
      console.log(e.target.src);
      this.image = e.target.src;

      this.setPageImg(this.image);
    },
  },
};
</script>

<style>
.selector-item {
  height: 20vh;
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
</style>
