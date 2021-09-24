import Vue from "vue";
import Vuex from "vuex";
import state from './state'
import * as getters from './getters'
import * as actions from './actions'
import pageStore from './modules/page'
import diaryStore from './modules/diary'
import userStore from './modules/user'
// import data from "./modules/data";
// import app from "./modules/app";

Vue.use(Vuex);

const root = new Vuex.Store({
  state,
  getters,
  actions,
  modules: {
    pageStore: pageStore,
    diaryStore: diaryStore,
    userStore: userStore
  }
})

export default root
