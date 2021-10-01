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

const BASE_URL='http://j5d103.p.ssafy.io/api/v1/page'
const instanceWithAuth = createInstance()

const pageStore = {
  namespaced: true,

  // initial state
  state : {
    store:{
      page_id: "",
      page_img: null,
      page_text: "",
      page_title: "",
      isKeywordSearch: false,
      selectedKeywords: [],
      pageList:[]
    }
  },

  // getters
  getters:{
  },

  // mutations
  mutations : {
    SET_PAGE_LIST(state, pages){
      state.store.pageList = pages
    },
    SET_PAGE_ID(state, id){
      state.store.page_id = id
    },

    SET_PAGE_IMG(state, img){
      state.store.page_img = img
      console.log(state.store.page_img)
    },

    SET_PAGE_TEXT(state, text){
      state.store.page_text = text
    },

    SET_PAGE_TITLE(state, title){
      state.store.page_title = title
    },

    GET_PAGE_IMG(state){
      return state.store.page_img
    },

    SET_IS_KEYWORD_SEARCH(state){
      state.store.isKeywordSearch = !state.store.isKeywordSearch
    },

    SET_SELECTED_KEYWORDS(state, selected){
      state.store.selectedKeywords = selected
    },
  },

  // actions
  actions : {
    requestPageList({commit},diaryId){
      return instanceWithAuth.get(`${BASE_URL}/read/${diaryId}`)
    },
    setPageList({commit}, pages){
      commit('SET_PAGE_LIST', pages)
    },
    setPageId({commit}, id){
      commit('SET_PAGE_ID', id)
    },

    setPageImg({commit}, img){
      commit('SET_PAGE_IMG', img)
    },

    setPageText({commit}, text){
      commit('SET_PAGE_TEXT', text)
    },

    setPageTitle({commit}, title){
      commit('SET_PAGE_TITLE', title)
    },

    getPageImg({commit}){
      return commit('GET_PAGE_IMG')
    },

    setIsKeywordSearch({commit}){
      commit('SET_IS_KEYWORD_SEARCH')
    },

    // 키워드 분석
    requestKeyword({commit}, info){
      return axios.post('http://13.124.43.16:8998/keyword_extraction', info)
    },
    setSelectedKeywords({commit}, selected){
      commit('SET_SELECTED_KEYWORDS', selected)
    },
    // 키워드 선택
    requestKeywordImage({commit}, key){
      console.log(key)
      return axios.get(
        "http://13.124.43.16:8998/image",
        {
          params: encodeURI(key)
        }
      )
    },
    // 감정 추출
    requestEmotion({commit}, info){
      return axios.post('http://3.35.52.211:8999/emotion', info)
    }
  },

}
export default pageStore;