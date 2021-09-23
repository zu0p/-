import api from "../../api";
import axios from "axios";

const BASE_URL='http://j5d103.p.ssafy.io/api/v1'

const diaryStore = {
  namespaced: true,

  // initial state
  state : {
    store:{
      diaryList: []
    }
  },

  // getters
  getters:{
    getDiaryList(state){
      return state.store.diaryList
    }
  },

  // mutations
  mutations : {
    SET_DIARY_LIST(state, list){
      state.store.diaryList = list
    }
  },

  // actions
  actions : {
    getDiaryList({commit}){
      let list = axios.get(`${BASE_URL}/diary/read`)
      commit('SET_DIARY_LIST', list)
      console.log(list)
    }
  },

}
export default diaryStore;