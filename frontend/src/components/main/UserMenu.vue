<template>
  <v-layout id="user-menu">
    <v-flex xs12 sm12 md12>
      <div class="text-right">
        <v-btn dark class="btn" text @click="clickUserInfo()">
          <v-icon dark left>mdi-account-circle-outline</v-icon>
          프로필
        </v-btn>
        <v-btn dark class="btn" text @click="clickLogout()">
          <v-icon dark left>mdi-close-thick </v-icon>
          로그아웃
        </v-btn>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";
const userStore = "userStore";
export default {
  name: "UserMenu",
  data() {
    return {
      userInfo: {
        userEmail: "",
        userId: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
        userPwd: "",
      },
    };
  },
  methods: {
    ...mapActions(userStore, ["logout", "requestUserInfo"]),
    clickUserInfo() {
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
    clickLogout() {
      this.logout();
      window.localStorage.removeItem("access-token");
      window.location = "/";
    },
  },
};
</script>

<style scoped>
body {
  font-family: "Roboto", sans-serif !important;
}
.welcome {
  color: white;
  position: relative;
  z-index: 2;
  text-align: center;
}
.btn {
  z-index: 2;
}
i.v-icon.v-icon {
  color: lightsteelblue;
}
</style>
