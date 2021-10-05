<template>
    <v-layout id="header-wrapper">
        <v-flex xs12 sm12 md12>
            <!-- <div class="img-wrapper"> -->
                <img id="bg" src="@/images/night.jpg" />
            <!-- </div> -->
            <div class="header-title">
                <h1 class="title"><b>그리더</b></h1>
                <p class="sub-title">: 당신의 <b>글</b>에 <b>이</b>미지를 <b>더</b>하다</p>
                <div class="outer"><hr /></div>
            </div>
        </v-flex>
    </v-layout>
</template>

<script>
export default {

}
</script>

<style>
.header-title{
    margin: 60px 0 10px 0;
    z-index: 2;
    position: relative;
}
.title{
    font-size: 3rem !important;
    font-weight: 500;
    line-height: 2rem;
    letter-spacing: .0125em !important;
    font-family: "Roboto",sans-serif !important;
    color: white;
    position: relative;
    z-index: 2;
    text-align: center;
}
.sub-title{
    color: white;
    position: relative;
    z-index: 2;
    text-align: center;
}
.outer{
    display: flex;
    margin: 60px 0 0 0;
}
hr{
    size: 5px;
    color: white;
    position: relative;
    z-index: 2;
    width: 90%;
    margin: 0 auto;
}
#header-wrapper{
    width: 100%;
}
.img-wrapper{
    /* width: 100%;
    height: 50%; */
    overflow: hidden;
    position: relative;
    padding-top: 56.25%;
    z-index: 1;
}
#bg{
    position: fixed;
    top:0;
    left:0;
    max-width: 100%;
    height: auto;
    z-index: 1;
}
</style>