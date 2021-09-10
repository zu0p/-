<template>
 <div>
    <v-layout row wrap class="navbar">
        <v-flex xs12 sm6 md4 class="box sample1">
            <div>test1</div>
        </v-flex>
        <v-flex xs12 sm6 md4 class="box sample2">
            <div>test2</div>
        </v-flex>
        <v-flex xs12 sm6 md4 class="box sample3">
            <div>test3</div>
        </v-flex>
    </v-layout>
  </div> 
</template>

<script>
export default {

}
</script>

<style>

.box{
    display: block;
}
.navbar{
    position: fixed;
    z-index: 2;
    color: white;
    margin-right: 0 !important;
    margin-left: 0 !important;
}
</style>