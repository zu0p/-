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
                        <h1
                          class="text-center display-2 text--accent-3"
                        >그리더</h1>
                        <h5
                          class="text-center"
                        >:당신의 글에 이미지를 더하다</h5>
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
                            v-model="state.form.id"
                            :rules="state.form.id"
                            prop="id"
                            dark
                            label="ID"
                            name="ID"
                            prepend-icon="mdi-account-circle white--text"
                            type="text"
                            color="teal accent-3"
                          />

                          <v-text-field
                            v-model="state.form.password"
                            :rules="state.form.password"
                            prop="password"
                            label="Password"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            dark
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
                        <h5
                          class="text-center"
                        >그리더와 함께하기</h5>
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
                        <h5
                          class="text-center"
                        >일기쓰러 가기</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step--">Sign in</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8">
                      <v-card-text class="mt-12 white--text">
                        <h1 class="text-center display-2 text--accent-3">그리더와 함께하기</h1>
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
                        <h4 class="text-center mt-4">Ensure your email for registration</h4>
                        <v-form class="form-c">
                          <v-text-field
                            v-model="state.form.name"
                            :rules="state.form.name"
                            prop="name"
                            label="Name"
                            name="Name"
                            prepend-icon="mdi-account-details white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                          />
                          <v-text-field
                            v-model="state.form.email"
                            :rules="state.form.email"
                            prop="email"
                            label="Email"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="teal accent-3"
                            dark
                          /> 
                          <!-- <v-btn rounded outlined dark @click="checkId">중복체크</v-btn> -->

                          <v-text-field
                            v-model="state.form.id"
                            :rules="state.form.id"
                            prop="id"
                            label="ID"
                            name="id"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            v-model="state.form.password"
                            :rules="state.form.password"
                            prop="password"
                            label="Password"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            v-model="state.form.nick"
                            :rules="state.form.nick"
                            prop="nick"
                            label="Nickname"
                            name="nick"
                            prepend-icon="mdi-alpha-n-circle white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            v-model="state.form.phone"
                            :rules="state.form.phone"
                            prop="phone"
                            label="Phone Number"
                            name="phone"
                            prepend-icon="phone"
                            type="text"
                            color="teal accent-3"
                            dark
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
import {reactive, onMounted, ref } from 'vue'
import { useStore } from 'vuex'

export default {
  props: {
  },
  data: () => ({
    step: 1
  }),
  setup() {
    const store = useStore()

    const loginForm = ref(null)

    const state = reactive({
      form: {
        id: '',
        password: '',
        nick: '',
        name: '',
        phone: '',
        email: '',
        userimage: '',
        evalid: true,
      },
      rules: {
        id: [
          { required: true, message: 'Please input ID', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ],
        nick: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ],
        name: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ],
        email: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ]
      },
    })

    onMounted(()=>{
    })

    const clickLogin = function () {
      loginForm.value.validate((valid)=>{
        if(valid){
          store.dispatch('root/requestLogin',{
            userId: state.form.id,
            userPwd: state.form.password
          }).then(function (result){
            alert("Success!","로그인 성공", "success")
            localStorage.setItem('jwt',result.data.accessToken)
            location.reload()
          })
          .catch(function () {
            alert('Fail','아이디와 비밀번호를 확인해주세요','error')
          })
        }
      })
    }

     const clickSignup = function () {
        if(validpwd() == false){
          // console.log("비밀번호 유효성 안맞음")
          state.form.evalid = false;
        }else{
          // console.log("비밀번호 유효성 "+ validpwd());
        }

        if(validemail() == false){
          // console.log("이메일 유효성 안맞음")
          state.form.evalid = false;
        }else{
          // console.log("이메일 유효성 "+validemail());
        }

        if(validid() == false){
          // console.log("아이디 유효성 안맞음")
          state.form.evalid = false;
        }else{
          // console.log("아이디 유효성 "+validid());
        }


        if(validpwd() && validemail() && validid() && validateCnumber())
          state.form.evalid = true;

        if (state.form.evalid==true) {
          store.dispatch('root/requestSignup',
          {
            userEmail: state.form.email,
            userName: state.form.name,
            userId: state.form.id,
            userPwd: state.form.password,
            userPhone: state.form.phone,
            userNick: state.form.nick,
            userImage: ''
          })
          .then(function (
          ) {
            alert("Succes!", "회원가입 성공", "success")
            location.reload()
          })
          .catch(function (err) {
            alert("Fail!", `${err}`, "error")
          })
        } else {
          alert("Fail!", "입력하신 정보가 유효한지 다시 확인해주세요.", "error")
        }
    }

    const validpwd = function (){
      var pw = state.form.password;
      var num = pw.search(/[0-9]/g);
      var eng = pw.search(/[a-z]/ig);
      var spe = pw.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);

      if(pw.length < 9 || pw.length > 16){
        alert("Fail!", "9자리 ~ 16자리 이내로 입력해주세요.", "error")
        return false;
        }
      if(pw.search(/₩s/) != -1){
        alert("Fail!", "비밀번호는 공백없이 입력해주세요.", "error")
        return false;
        }
      if(num < 0 || eng < 0 || spe < 0 ){
        alert("Fail!", "영문, 숫자, 특수문자를 혼합하여 입력해주세요.", "error")
        return false;
        }
      return true;
    }

    const validemail = function(){
      var email = state.form.email;
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }

    const validid = function(){
      var id = state.form.id;
      if(id.length > 16 || id == "")
        return false;
      return true;
    }

    const checkId = function(){
      store.dispatch('root/checkSignupId', { id: state.form.id })
      .then(function () {
        alert("Succes!", "사용가능한 아이디입니다.", "success")
      })
      .catch(function () {
        alert("Fail!", "사용중인 아이디입니다.", "info")
      })
    }


    return { loginForm, state, clickLogin, clickSignup, validpwd, validemail, validid, checkId }
  }
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
    background-repeat : no-repeat;
    background-size : cover;
  }
.elevation-12 {
  background-color: rgba( 255, 255, 255, 0.0 );
}
.back-opt {
  background-color: rgba( 255, 255, 255, 0.5 );
}
</style>