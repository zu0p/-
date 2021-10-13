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

const BASE_URL = "http://15.164.104.218/api/v1/users";
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
      (state.store.isLogin = false), (state.store.token = "");
      state.store.tokenType = "";
    },
  },

  // actions
  actions: {
    requestLogin({ commit }, users) {
      return axios.post(`${BASE_URL}/login`, users);
    },
    requestSignup({ commit }, users) {
      console.log(users);
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
    },
    updateProfileImage({ commit }, image) {
      const formdata = new FormData();
      formdata.append("profileImage", image);
      return instanceWithAuth.put(`${BASE_URL}/change-image`, formdata, { headers: { "Content-Type": "multipart/form-data" } });
    },
    deleteUserInfo({ commit }) {
      instanceWithAuth
        .delete(`${BASE_URL}/delete`)
        .then((res) => {
          if ((res.statusText = "OK")) {
            commit("RESET_TOKEN");
            alert("회원정보가 삭제되었습니다.\n그리더를 이용해주셔서 감사합니다");
            window.location = "/";
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response.status == 422) {
            alert("회원정보 수정 실패했습니다..");
          }
        });
    },
    updatePassword({ commit }, pwd) {
      return instanceWithAuth.put(`${BASE_URL}/change-password`, pwd);
    },
  },
};
export default userStore;
