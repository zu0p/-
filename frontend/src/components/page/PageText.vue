<template>

  <div class="page_content_text" v-bind:id="'pct_' + idx" contenteditable="false"></div>

</template>

<script>
export default {
  data(){
    return{
    }
  },
  props: ['page', 'idx', 'isFront'],
  mounted(){
    // console.log(this.isFront)
    const textbox = document.getElementById(`pct_${this.idx}`)
    // console.log(textbox)
    if(this.page.pageContent===undefined){
      textbox.style.display='none'
    }
    else{
      textbox.innerHTML = this.page.pageContent
      textbox.style.left = this.page.left.toString()+"px"
      textbox.style.top = this.page.top.toString()+"px"    
    }
    
    
  },
}
</script>

<style>

.page_content_text{
  position: fixed !important;
  display: none;
}
</style>