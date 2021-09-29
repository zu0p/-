<template>
  <v-app id="inspire">
    <v-content class="back-img">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6">
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
                            dark
                            label="ID"
                            name="ID"
                            prepend-icon="mdi-account-circle white--text"
                            type="text"
                            color="teal accent-3"
                          />

                          <v-text-field
                            
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
                            label="Name"
                            name="Name"
                            prepend-icon="mdi-account-details white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                          />
                          <v-text-field
                            label="Email"
                            name="Email"
                            prepend-icon="email"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            id="id"
                            label="ID"
                            name="id"
                            prepend-icon="person"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            id="password"
                            label="Password"
                            name="password"
                            prepend-icon="lock"
                            type="password"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            id="nick"
                            label="Nickname"
                            name="nick"
                            prepend-icon="mdi-alpha-n-circle white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            id="phone"
                            label="Phone Number"
                            name="phone"
                            prepend-icon="phone"
                            type="text"
                            color="teal accent-3"
                            dark
                          />

                          <v-text-field
                            id="userImage"
                            label="User Image"
                            name="userImage"
                            prepend-icon="mdi-image-area white--text"
                            type="text"
                            color="teal accent-3"
                            dark
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn rounded color="grey accent-3">SIGN UP</v-btn>
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
import {reactive, onMounted } from 'vue'
import { useStore } from 'vuex'
import swal from 'sweetalert'

export default {
  props: {
  },
  data: () => ({
    step: 1
  }),
  setup() {
    const store = useStore()

    const state = reactive({
      form: {
        id: '',
        password: '',
        nick: '',
        name: '',
        phone: '',
        email: '',
        userimage: '',
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
            swal("Success!","로그인 성공", "success")
            localStorage.setItem('jwt',result.data.accessToken)
            location.reload()
          })
          .catch(function () {
            swal('Fail','아이디와 비밀번호를 확인해주세요','error')
          })
        }
      })
    }

    return { state, clickLogin}
  }
};
</script>

<style scoped>
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