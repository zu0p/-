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
      diaryList: [],
      diaryId: null,
      diaryTitle: '',
      diaryDesc: ''
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
    SET_DIARY_ID(state, id){
      state.store.diaryId = id
    },
    SET_DIARY_TITLE_AND_DESC(state, info){
      for(let i = 0 ;i<state.store.diaryList.length; i++){
        if(state.store.diaryList[i].id == info.id){
          state.store.diaryTitle = info.title
          state.store.diaryDesc = info.desc
          break
        }
      }
    },
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
    UPDATE_DIARY(state, diary){
      const res = state.store.diaryList.map(item => {
        if(item.id == diary.diaryId)
          item.diaryName = diary.modifyName
      })
    },
    DELETE_DIARY(state, id){
      const res = state.store.diaryList.filter(item => item.id != id)
      state.store.diaryList = res
      // console.log(state.store.diaryList)
    }
  },

  // actions
  actions : {
    setDiaryId({commit}, id){
      commit('SET_DIARY_ID', id)
    },
    setDiaryTitleAndDesc({commit}, info){
      commit('SET_DIARY_TITLE_AND_DESC', info)
    },
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
    requestDiaryInfo({commit}, id){
      return instanceWithAuth.get(`${BASE_URL}/read/${id}`)
    },
    requestUpdateDiary({commit}, diary){
      return instanceWithAuth.put(`${BASE_URL}/update`, diary)
    },
    updateDiary({commit},diary){
      commit('UPDATE_DIARY', diary)
    },
    // 다이어리 삭제
    requestDeleteDiary({commit}, id){
      return instanceWithAuth.delete(
        `${BASE_URL}/delete`,
        {
          data: id
        }
      )
    },
    deleteDiary({commit}, id){
      commit('DELETE_DIARY', id)
    },
  },

}
export default diaryStore;