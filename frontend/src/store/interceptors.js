// import userStore from './modules/user'
// console.log(userStore.state.store)
// // const tokenStore = this.$store._modules.root._children.userStore.state.store
// const tokenStore = userStore.state.store

// import store from '../store/index'
// console.log(store)
export function setInterceptors(instance){
  instance.interceptors.request.use(
    function(config){
      // const token = tokenStore.token
      // const type = tokenStore.tokenType
      const token = window.localStorage.getItem('access-token')
      // console.log(token)
      if(token)
        // config.headers.Authorization = `${type} ${token}`
        config.headers.Authorization = `Bearer ${token}`
      return config
    },
    function(err){
      return Promise.reject(err)
    }
  )

  //response interceptor
  instance.interceptors.response.use(
    function(res){
      return res
    },
    function(err){
      return Promise.reject(err)
    }
  )
  return instance
}