<template>
  <v-container>
    <v-row id="before-select">
      <v-row align="center" class="selector-item item1">
        <v-col>
          <v-btn icon class="text-none" depressed @click="onUploadButtonClick">
            <v-icon>mdi-plus-circle-outline</v-icon>
            <span> 직접 올리기 </span>        
          </v-btn>
          <input
            ref="uploader"
            class="d-none"
            type="file"
            accept="image/*"
            @change="onFileChanged"
          >
        </v-col>
      </v-row>
      <v-row align="center" class="selector-item item2">
        <v-col>
          <v-btn icon>
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
    <v-row id="after-select" class="appear" >
      <img :src="preview" class="img-fluid" />
    </v-row>     
  </v-container>
</template>

<script>
export default {
  name: 'ImageSelectorItem',
  data(){
    return{
      image: null,
      imageSelect:false,
      preview: null
    }
  },
  methods:{
    onUploadButtonClick(){
      this.imageSelect = true
      window.addEventListener('focus', () => {
        this.imageSelect = false
      }, { once: true })

      this.$refs.uploader.click()
    },
    onFileChanged(e){
      this.image = e.target.files[0]
      // console.log(this.image)
      var reader = new FileReader();
      reader.onload = (e) => {
        this.preview = e.target.result;
      }
      reader.readAsDataURL(this.image);

      // document.getElementById('before-select').style.animation='fade-out 1s'
      // document.getElementById('before-select').style.animationFillMode='forwards'
      document.getElementById('before-select').style.display='none'
      
      // document.getElementById('before-select').classList.add('disappear')
      // document.getElementById('after-select').classList.add('appear')
    }
  }
}
</script>

<style>
.selector-item{
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

.appear{
  visibility: visible;
  width: 100%;
  margin-top: 10px;
  transition: all 0.3s;
}

</style>