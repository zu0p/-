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

const BASE_URL = "http://j5d103.p.ssafy.io/api/v1/music";
const instanceWithAuth = createInstance();

const musicStore = {
  namespaced: true,

  // initial state
  state: {
    store: {
    },
  },

  // mutations
  mutations: {
  },

  // actions
  actions: {
    requestMusicByText({ commit }, text) {
      return instanceWithAuth.post(`${BASE_URL}/recommend_by_text`, text);
    },
    requestMusicByPage({ commit }, info){
      return instanceWithAuth.get(`${BASE_URL}/recommend_by_page/${info.diaryId}/${info.pageId}`, info);
    }
  },
};
export default musicStore;
