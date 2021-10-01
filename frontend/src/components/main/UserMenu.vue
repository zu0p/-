<template>
  <v-layout id="user-menu">
    <v-flex xs12 sm12 md12>
      <div class="text-right">
        <v-dialog v-model="dialog" persistent max-width="400px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn dark class="btn" v-bind="attrs" v-on="on" text>
              <v-icon dark left>mdi-account-circle-outline</v-icon>
              프로필
            </v-btn>
          </template>
          <user-profile :isAdd="true" @closeUserInfoDialog="onCloseUserInfoDialog" />
        </v-dialog>
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
import UserProfile from "./UserProfile.vue";
const userStore = "userStore";
export default {
  name: "UserMenu",
  components: {
    UserProfile,
  },
  data() {
    return {
      dialog: false,
      userInfo: {
        userEmail: "",
        userId: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
      },
    };
  },
  methods: {
    ...mapActions(userStore, ["logout", "requestUserInfo"]),

    clickLogout() {
      this.logout();
      window.localStorage.removeItem("access-token");
      window.location = "/";
    },
    onCloseUserInfoDialog() {
      this.dialog = false;
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
