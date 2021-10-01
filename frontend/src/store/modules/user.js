import api from "../../api";
import axios from "axios";
import { setInterceptors } from "../interceptors";

function createInstance() {
  const instance = axios.create();
  return setInterceptors(instance);
}

// Token값과 특정 url을 붙여서 셋팅
function createInstanceWithAuth(url) {
  const instance = axios.create({
    baseURL: BASE_URL + `${url}`,
  });
  return setInterceptors(instance);
}

const BASE_URL = "http://j5d103.p.ssafy.io/api/v1/users";
const instanceWithAuth = createInstance();

const userStore = {
  namespaced: true,

  // initial state
  state: {
    store: {
      isLogin: false,
      token: "",
      tokenType: "",
    },
  },

  // mutations
  mutations: {
    SET_TOKEN(state, tokenObj) {
      state.store.token = tokenObj.access_token;
      state.store.tokenType = tokenObj.token_type;
      console.log(state.store.token + " : " + state.store.tokenType);
    },
    RESET_TOKEN(state) {
      state.store.token = "";
      state.store.tokenType = "";
    },
  },

  // actions
  actions: {
    requestLogin({ commit }, users) {
      return axios.post(`${BASE_URL}/login`, users);
    },
    requestSignup({ commit }, users) {
      return axios.post(`${BASE_URL}/signup`, users);
    },
    requestUserInfo({ commit }) {
      return instanceWithAuth.get(`${BASE_URL}/me`);
    },
    setToken({ commit }, tokenObj) {
      commit("SET_TOKEN", tokenObj);
    },
    logout({ commit }) {
      commit("RESET_TOKEN");
    },
    updateUserInfo({ commit }, user) {
      return instanceWithAuth.put(`${BASE_URL}/update`, user);
    }
  },
};
export default userStore;
