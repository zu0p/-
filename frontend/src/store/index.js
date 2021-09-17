import Vue from "vue";
import Vuex from "vuex";
import state from './state'
import * as getters from './getters'
import * as actions from './actions'
// import data from "./modules/data";
// import app from "./modules/app";

Vue.use(Vuex);

const root = {
  state,
  getters,
  actions,
}

export default root
