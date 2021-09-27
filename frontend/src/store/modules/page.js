import api from "../../api";

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
    }
  },

  // getters
  getters:{
  },

  // mutations
  mutations : {
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
  },

  // actions
  actions : {
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
  },

}
export default pageStore;