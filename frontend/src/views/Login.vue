<template>
  <v-app id="inspire">
    <v-content class="back-img">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="17" sm="10" md="7">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12 white--text">
                        <h1 class="text-center display-2 text--accent-3">그리더</h1>
                        <h5 class="text-center">:당신의 글에 이미지를 더하다</h5>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fab fa-facebook-f</v-icon>
                          </v-btn>

                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fab fa-google-plus-g</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fab fa-linkedin-in</v-icon>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Ensure your ID for registration</h4>
                        <v-form>
                          <v-text-field
                            dark
                            label="ID"
                            name="ID"
                            prepend-icon="mdi-account-circle white--text"
                            type="text"
                            color="teal accent-3"
                            v-model="login.userId"
                          />

                          <v-text-field
                            label="Password"
                            name="password"
                            prepend-icon="mdi-lock-outline"
                            type="password"
                            color="teal accent-3"
                            dark
                            v-model="login.userPwd"
                            @keyup.enter="clickLogin"
                          />
                        </v-form>
                        <h3 class="text-center mt-4">Forgot your password ?</h3>
                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn rounded color="grey accent-3" @click="clickLogin">SIGN IN</v-btn>
                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="back-opt accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Welcome!!!</h1>
                        <h5 class="text-center">그리더와 함께하기</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step++">SIGN UP</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="back-opt accent-3">
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">Welcome Back!</h1>
                        <h5 class="text-center">일기쓰러 가기</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step--">Sign in</v-btn>
                      </div>
                    </v-col>

                    <!-- 회원가입 -->
                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12 white--text">
                        <h1 class="text-center display-2 text--accent-3">그리더와 함께하기</h1>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fa-facebook-f</v-icon>
                          </v-btn>

                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fab fa-google-plus-g</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="white" outlined>
                            <v-icon>fab fa-linkedin-in</v-icon>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Ensure your email for registration</h4>
                        <v-form ref="form" class="form-c">
                          <v-text-field
                            id="id"
                            label="ID"
                            name="id"
                            prepend-icon="mdi-account"
                            type="text"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userId"
                            :rules="rules.idRule"
                          />

                          <v-text-field
                            id="password"
                            label="Password"
                            name="password"
                            prepend-icon="mdi-lock-outline"
                            type="password"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userPwd"
                            :rules="rules.pwdRule"
                          />
                          <v-text-field
                            label="Name"
                            name="Name"
                            prepend-icon="mdi-account-details white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userName"
                            :rules="rules.nameRule"
                          />
                          <v-text-field
                            label="Email"
                            name="Email"
                            prepend-icon="mdi-email-outline"
                            type="text"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userEmail"
                            :rules="rules.emailRule"
                          />

                          <v-text-field
                            id="nick"
                            label="Nickname"
                            name="nick"
                            prepend-icon="mdi-alpha-n-circle white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userNick"
                            :rules="rules.nickRule"
                          />

                          <v-text-field
                            id="phone"
                            label="Phone Number"
                            name="phone"
                            prepend-icon="mdi-cellphone-wireless"
                            type="text"
                            color="teal accent-3"
                            dark
                            required
                            v-model="form.userPhone"
                            :rules="rules.phoneRule"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn rounded color="grey accent-3" @click="clickSignup">SIGN UP</v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from "vuex";
const userStore = "userStore";
// import {reactive, onMounted } from 'vue'
// import { useStore } from 'vuex'

export default {
  props: {},
  data() {
    return {
      step: 1,
      state: "ins",
      login: {
        userId: "",
        userPwd: "",
      },
      form: {
        userId: "",
        userPwd: "",
        userNick: "",
        userName: "",
        userPhone: "",
        userEmail: "",
        userImage: "",
      },
      rules: {
        idRule: [(v) => !!v || "아이디 입력을 잊으셨군요"],
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
      pwdChk: "",
    };
  },
  methods: {
    ...mapActions(userStore, ["requestSignup", "requestLogin", "setToken"]),
    clickLogin() {
      this.requestLogin(this.login)
        .then((res) => {
          if (res.status != 200) {
            console.log("로그인실패");
          }
          // 로그인 성공 시
          if ((res.statusText = "OK")) {
            // token 저장
            let tokenObj = {
              access_token: res.data.access_token,
              token_type: res.data.token_type,
            };
            this.setToken(tokenObj);
            window.localStorage.setItem("access-token", tokenObj.access_token);

            // main으로 라우팅
            this.$router.push({ name: "Main" });
          }
        })
        .catch((e) => {
          if (e.response.status == 401) {
            alert("아이디 혹은 비밀번호가 틀렸습니다.");
            this.login.userId = "";
            this.login.userPwd = "";
          }
        });
    },
    clickSignup() {
      const validate = this.$refs.form.validate();
      if (validate) {
        this.requestSignup(this.form)
          .then((res) => {
            if (res.statusText == "OK") {
              alert("회원가입 성공");
              window.location = "/";
            }
          })
          .catch((e) => {
            console.log(e);
          });
      }
    },
  },

  //   setup() {
  //     const store = useStore()

  //     const state = reactive({
  //       form: {
  //         id: '',
  //         password: '',
  //         nick: '',
  //         name: '',
  //         phone: '',
  //         email: '',
  //         userimage: '',
  //       },
  //     })

  //     onMounted(()=>{
  //     })

  //     const clickLogin = function () {
  //       loginForm.value.validate((valid)=>{
  //         if(valid){
  //           store.dispatch('root/requestLogin',{
  //             userId: state.form.id,
  //             userPwd: state.form.password
  //           }).then(function (result){
  //             alert("Success!","로그인 성공", "success")
  //             localStorage.setItem('jwt',result.data.accessToken)
  //             location.reload()
  //           })
  //           .catch(function () {
  //             alert('Fail','아이디와 비밀번호를 확인해주세요','error')
  //           })
  //         }
  //       })
  //     }

  //     return { state, clickLogin}
  //   }
};
</script>

<style scoped>
h3 {
  font-size: 18px;
}
h4 {
  font-size: 15px;
}
h5 {
  font-size: 12px;
}
.back-img {
  background-image: url("../images/sy.png");
  min-height: 100vh;
  display: flex;
  background-repeat: no-repeat;
  background-size: cover;
}
.elevation-12 {
  background-color: rgba(255, 255, 255, 0);
}
.back-opt {
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
