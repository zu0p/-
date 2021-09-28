<template>
  <v-container>
    <div class="book">
      <h1>page1</h1>
      <p>마우스를 올려주세요</p>
    </div>
    <!-- <div class="book">
      <h1>page2</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et, tenetur.</p>
    </div>   -->
  </v-container>
</template>

<script>
export default{
  name:'DetailView',
  data(){
    return{
    }
  },
  created(){
  },
  methods:{

  }
}
</script>

<style>
section{
  margin:50px auto;
  position:relative;
  width: 200px;height: 200px;
  perspective: 1000px;
}
.book{
  position:absolute;
  width: 200px; height: 250px;
  text-align: center;
  box-shadow: 5px 5px 15px #333;
}
.book:nth-child(1){
  background: #abc;
  transform-origin: left center;
  transition: 2s;
  z-index:1;
}
.book:nth-child(2){
  background: #cba;
  transform-origin: left center;
  transition: 2s;   
  z-index:2;
}
.book:nth-child(1):hover{
  transform: rotateY(-180deg);
  background: #666;
}
</style>