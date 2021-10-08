import Vue from "vue";
import Vuex from "vuex";
import musicStore from './modules/music'
import pageStore from './modules/page'
import diaryStore from './modules/diary'
import userStore from './modules/user'
// import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

const root = new Vuex.Store({
  // state,
  // getters,
  // actions,
  modules: {
    pageStore: pageStore,
    diaryStore: diaryStore,
    userStore: userStore,
    musicStore: musicStore
  },
  // plugins: [
  //   createPersistedState()
  // ]
})

export default root