<template>
  <v-card>
    <template v-slot:progress>
      <v-progress-linear
        absolute
        color="green lighten-3"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>
    <v-img
      height="200"
      src="../../images/draw.png"
    >
      <v-row
        align="center"
        justify="center"
        class = "mt-3"
      >
        <v-col class="text-center">
          <v-avatar v-if="userInfo.userImage"
            color="white"
            size="150"
          >
           <img src = {{ userInfo.userImage }}>
          </v-avatar>
          <v-avatar class = "avatar" v-else
            size="150"
            color="white"
            
          >
          <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png">
          </v-avatar>
        </v-col>
      </v-row>
    </v-img>
    <v-form>
      <v-container>
        <v-row justify = "center">
          <v-col cols = "9">
            <v-row align="center" justify="center">
            <v-col cols = "6" class = 'mt-2'>
              <h4>회원 정보</h4>
            </v-col>
            <v-col cols = "4">
            </v-col>
            <v-col cols = "2">
              <v-btn
                class="mx-2"
                fab
                small
                text
                @click="isUpdate=!isUpdate"
              >
                <v-icon dark>
                  mdi-pencil
                </v-icon>
              </v-btn>
            </v-col>
            </v-row>
          </v-col>
          <v-col
            cols="8"
            class = 'pa-0'
          >
            <v-text-field
              :disabled="!isUpdate"
              v-model="userInfo.userName"
              prepend-icon="mdi-account-details --text"
              color="teal accent-4"
              label="Name"
              :rules="rules.nameRule"
            ></v-text-field>
          </v-col>
          <v-col
            cols="8"
            class = 'pa-0'
          >
            <v-text-field
              :disabled="!isUpdate"
              v-model="userInfo.userEmail"
              prepend-icon="mdi-email-outline"
              color="teal accent-4"
              label="E-mail"
              :rules="rules.emailRule"
            ></v-text-field>
          </v-col>
          <v-col
            cols="8"
            class = 'pa-0'
          >
            <v-text-field
              :disabled="!isUpdate"
              v-model="userInfo.userNick"
              prepend-icon="mdi-alpha-n-circle --text"
              color="teal accent-4"
              label="NickName"
              :rules="rules.nickRule"
            ></v-text-field>
          </v-col>
          <v-col
            cols="8"
            class = 'pa-0'
          >
            <v-text-field
              :disabled="!isUpdate"
              v-model="userInfo.userPhone"
              prepend-icon="mdi-cellphone-wireless"
              color="teal accent-4"
              label="Phone"
              :rules="rules.phoneRule"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      
      <v-spacer></v-spacer>
      <v-btn v-if="isUpdate"
        color="blue"
        depressed
        dark
        @click="updateClick"
      >
        <v-icon left>
          mdi-update
        </v-icon>
        Update
      </v-btn>
      <v-btn v-else
        color="blue-grey lighten-1"
        depressed
        dark
        @click="closeClick"
      >
        <v-icon left>
          mdi-close-thick
        </v-icon>
        Close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
const userStore = "userStore";
export default {
  data() {
    return {
      isUpdate:false,
      userInfo: {
        userEmail: "",
        userId: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
      },
      rules: {
        nickRule: [(v) => !!v || "닉네임 입력을 잊으셨군요"],
        nameRule: [(v) => !!v || "이름 입력을 잊으셨군요"],
        phoneRule: [
          (v) => !!v || "전화번호 입력을 잊으셨군요",
          (v) => {
            const replaceV = v.replace(/(\s*)/g, "");
            const phonePattern = /^\d{3}-\d{3,4}-\d{4}$/;
            return phonePattern.test(replaceV) || "전화번호 형식이 아닌가봐요";
          },
        ],
        emailRule: [
          (v) => !!v || "이메일 입력을 잊으셨군요",
          (v) => {
            const replaceV = v.replace(/(\s*)/g, "");
            const emailPattern = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/;
            return emailPattern.test(replaceV) || "이메일 형식이 아닌가봐요";
          },
        ],
      },
    }
  }, 
  created(){
    this.requestUserInfo()
        .then((res) => {
          // 회원정보 조회 성공
          if ((res.statusText = "OK")) {
            this.userInfo.userEmail = res.data.userEmail,
            this.userInfo.userImage = res.data.userImage,
            this.userInfo.userName = res.data.userName,
            this.userInfo.userNick = res.data.userNick,
            this.userInfo.userPhone = res.data.userPhone
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
    ...mapActions(userStore, ["logout", "requestUserInfo", "updateUserInfo"]),
    closeClick() {
      this.$emit("closeUserInfoDialog");
    },
    updateClick(){
      this.updateUserInfo(this.userInfo).then((res) => {
          // 회원정보 수정 성공
          if ((res.statusText = "OK")) {
            this.isUpdate=false
            alert("회원정보 수정 성공")
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response.status == 422) {
            alert("회원정보 수정 실패했습니다..");
          }
        });
    }
  },
};
</script>

<style scoped>
.avatar {
                  border: 1px solid;
                  
}
</style>
