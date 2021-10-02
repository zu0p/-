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
            class = "profile-image"
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
          <v-btn
            class="mx-2 profile-image-update"
            fab
            small
            dark
            color="light blue"
            @click="profileUpdateClick"
          >
            <v-icon>
              mdi-image-plus
            </v-icon>
          </v-btn>
          <input ref="uploader" class="d-none" type="file" accept="image/*" @change="profileUpdated" />
        </v-col>
      </v-row>
    </v-img>
    <v-form >
      <v-container v-if="!isPwdUpdate">
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
                v-if="!isUpdate"
                fab
                small
                text
                @click="isUpdate=!isUpdate"
              >
                <v-icon dark>
                  mdi-pencil
                </v-icon>
              </v-btn>
              <v-menu
               v-if="isUpdate"
                bottom
                left
                transition="slide-y-transition"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-dots-vertical</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item @click="isPwdUpdate=!isPwdUpdate">
                    <v-list-item-action>
                      <v-icon color = "green">mdi-key-outline</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>비밀번호 변경</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item @click="deleteClick">
                    <v-list-item-action>
                      <v-icon color = "red">mdi-delete-outline</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>회원정보 삭제</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-menu>
              
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
      <!-- 비밀번호 변경시 -->
      <v-container v-if="isPwdUpdate">
        <v-row justify = "center">
          <v-col cols = "9">
            <v-row align="center">
            <v-col cols = "8" class = 'mt-2'>
              <h4>비밀번호 변경</h4>
            </v-col>
            </v-row>
          </v-col>
          <v-col
            cols="8"
            class = 'pa-0'
          >
            <v-text-field
              v-model="pwd.modifyPwd"
              prepend-icon="mdi-shield-key-outline"
              color="teal accent-4"
              type = "password"
              label="변경 비밀번호"
              :rules="rules.pwdRule"
            ></v-text-field>
            <v-text-field
              v-model="pwd.modifyPwdConfirm"
              prepend-icon="mdi-shield-key"
              color="teal accent-4"
              type = "password"
              label="변경 비밀번호 확인"
              :rules="rules.pwdConfirmRule"
            ></v-text-field>
          </v-col>
          
        </v-row>
      </v-container>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions v-if="!isPwdUpdate">
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
       <v-btn v-if="isUpdate"
        color="blue-grey lighten-1"
        depressed
        dark
        @click="isUpdate=false"
      >
        <v-icon left>
          mdi-close-thick
        </v-icon>
        cancel
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
    <v-card-actions v-if="isPwdUpdate">
      <v-spacer></v-spacer>
      <v-btn 
        color="green"
        depressed
        dark
        @click="pwdChangeClick"
      >
        <v-icon left>
          mdi-update
        </v-icon>
        Change
      </v-btn>
       <v-btn 
        color="blue-grey lighten-1"
        depressed
        dark
        @click="closeClick"
      >
        <v-icon left>
          mdi-close-thick
        </v-icon>
        close
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
      imageSelect:false,
      isPwdUpdate: false,
      userInfo: {
        userEmail: "",
        userId: "",
        userPwd: "",
        userImage: "",
        userName: "",
        userNick: "",
        userPhone: "",
      },
      pwd:{
        modifyPwd: "",
        modifyPwdConfirm: "",
      },
      rules: {
        nickRule: [(v) => !!v || "닉네임 입력을 잊으셨군요"],
        nameRule: [(v) => !!v || "이름 입력을 잊으셨군요"],
        pwdRule: [
          (v) => !!v || "비밀번호 입력을 잊으셨군요",
          (v) => !(v && (v.length < 9 || v.length > 16)) || "8~16자 사이로 입력해주세요",
          (v) => {
            const replaceV = v.replace(/(\s*)/g, "");
            const eng = replaceV.search(/[a-zA-Z]/g);
            const num = replaceV.search(/[0-9]/gi);
            const spec = replaceV.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);
            if (num < 0 || eng < 0 || spec < 0) {
              return false || "영문, 숫자, 특수문자를 포함해야 해요";
            }
            return true;
          },
        ],
        pwdConfirmRule:[
          (v) => {
            if (v != this.pwd.modifyPwd) {
              return false || "비밀번호가 일치하지 않습니다.";
            }
            return true;
          },
        ],
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
            this.userInfo.userPwd = res.data.userPwd,
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
    ...mapActions(userStore, ["logout", "requestUserInfo", "updateUserInfo", "updateProfileImage", "deleteUserInfo", "updatePassword"]),
    closeClick() {
      this.isUpdate=false,
      this.imageSelect=false,
      this.isPwdUpdate=false,
      this.pwd.modifyPwd = "",
      this.pwd.modifyPwdConfirm = "",
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
    },
    deleteClick(){
      const res = window.confirm("회원정보 삭제 후엔 복구할 수 없습니다.\n정말로 삭제하시겠습니까?")
      if(res){
        this.deleteUserInfo()
      }
    },
    pwdChangeClick(){
      this.updatePassword(this.pwd).then((res) => {
          if ((res.statusText = "OK")) {
            this.isUpdate=false,
            this.isPwdUpdate=false,
            this.pwd.modifyPwd = "",
            this.pwd.modifyPwdConfirm = "",
            alert("비밀번호가 변경되었습니다.")
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response.status == 401) {
            alert("비밀번호 변경에 실패했습니다.");
          }
        });
    },
    profileUpdateClick() {
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
    profileUpdated(e) {
      this.userInfo.profileImage = e.target.files[0];
      console.log(this.userInfo.profileImage);

      var reader = new FileReader();
      reader.onload = (e) => {
        this.preview = e.target.result;
      };
      reader.readAsDataURL(this.userInfo.profileImage);

      // document.getElementById("before-select").style.display = "none";
    this.updateProfileImage(this.userInfo.profileImage).then((res) => {
          // 회원정보 수정 성공
          if ((res.statusText = "OK")) {
            alert("프로필 이미지를 변경했습니다")
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response.status == 422) {
            alert("프로필 이미지 변경 실패");
          }
        });

    },
  },
};
</script>

<style scoped>
.profile-image-update{
  z-index: -1;
  position:relative;
}
.profile-image-update{
  z-index: 1;
  position:relative;
}
</style>
