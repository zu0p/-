<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Create New Diary</span>
    </v-card-title>
    <v-card-text>
      gdgd
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeClick">
        Close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      userInfo: {
        userEmail: "",
        userId: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
      },
    }
  }, 
  mounted(){
     this.requestUserInfo()
        .then((res) => {
          // 회원정보 조회 성공
          if ((res.statusText = "OK")) {
            this.userInfo = res.data;
            console.log(this.userInfo);
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response.status == 401) {
            alert("회원정보 조회 실패했습니다..");
          }
        });
  },
  methods: {
    ...mapActions(userStore, ["logout", "requestUserInfo"]),
    closeClick() {
      this.$emit("closeUserInfoDialog");
    },
  },
};
</script>

<style></style>
