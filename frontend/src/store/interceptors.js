// import store from "../store";
// const tokenStore = this.$store._modules.root._children.userStore.state.store

export function setInterceptors(instance){
  instance.interceptors.request.use(
    function(config){
      const token = tokenStore.token
      const type = tokenStore.tokenType
      console.log(token)
      if(token)
        config.headers.Authorization = `${type} ${token}`
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