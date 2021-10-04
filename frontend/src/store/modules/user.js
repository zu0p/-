import api from "../../api";
import axios from "axios";

const BASE_URL='http://j5d103.p.ssafy.io/api/v1/users'

const userStore = {
  namespaced: true,

  // initial state
  state : {
    store:{
      isLogin: false,
      token: '',
      tokenType: ''
    }
  },

  // mutations
  mutations : {
    SET_TOKEN(state, tokenObj){
      state.store.token = tokenObj.access_token
      state.store.tokenType = tokenObj.token_type
      console.log(state.store.token+" : "+state.store.tokenType)
    }
  },

  // actions
  actions : {
    requestLogin({commit}, users){
      return axios.post(`${BASE_URL}/login`, users)
    },
    requestSignup({commit}, users){
      return axios.post(`${BASE_URL}/signup`, users)
    },
    setToken({commit}, tokenObj){
      commit('SET_TOKEN', tokenObj)
    }
  },

}
export default userStore;