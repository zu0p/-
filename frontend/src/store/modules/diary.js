import api from "../../api";
import axios from 'axios';
import { setInterceptors } from '../interceptors'

function createInstance(){
  const instance = axios.create()
  return setInterceptors(instance)
}

// Token값과 특정 url을 붙여서 셋팅
function createInstanceWithAuth(url) {
  const instance = axios.create({
    baseURL: BASE_URL+`${url}`,
  })
  return setInterceptors(instance)
}

const BASE_URL='http://j5d103.p.ssafy.io/api/v1/diary'
const instanceWithAuth = createInstance()

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
    diaryList:(state)=>{
      return state.store.diaryList
    }
  },

  // mutations
  mutations : {
    SET_DIARY_LIST(state, list){
      // console.log(state.store.diaryList)      
      state.store.diaryList = list.map((item, idx)=>{
        if(idx>=5){
          item.hide='box--hide'
        }
        else{
          item.hide=''
        }
        return item
      })      
    },
    ADD_DIARY(state, diary){
      if(state.store.diaryList.length>=5)
        diary.hide='box--hide'
      state.store.diaryList.push(diary)
      // console.log(state.store.diaryList)
    },
    DELETE_DIARY(state, id){
      const res = state.store.diaryList.filter(item => item.id != id)
      state.store.diaryList = res
    }
  },

  // actions
  actions : {
    // 다이어리 목록 조회
    getDiaryList({commit}){
      return instanceWithAuth.get(`${BASE_URL}/read`)
    },

    // store의 diaryList 초기화
    setDiaryList({commit}, list){
      commit('SET_DIARY_LIST', list)
    },

    // 다이어리 생성
    createDiary({commit}, diary){
      return instanceWithAuth.post(
        `${BASE_URL}/create`, 
        diary,
        {headers:{'Content-Type': 'multipart/form-data'}}
      )
    },

    // store의 diaryList에 추가
    addDiary({commit}, diary){
      commit('ADD_DIARY', diary)
    },
    
    // 다이어리 수정

    // 다이어리 삭제
    requestDeleteDiary({commit}, id){
      return instanceWithAuth.delete(`${BASE_URL}/delete`, id)
    },
    deleteDiary({commit}, id){
      commit('DELETE_DIARY', id)
    }
  },

}
export default diaryStore;