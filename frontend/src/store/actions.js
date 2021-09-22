import $axios from 'axios'

//로그인
export function requestLogin ({ state }, payload){
    // console.log(state)
    const url = '/users/login'
    let body = payload
    return $axios.post(url, body)
}

//회원가입
export function requestSignup ({ state }, payload) {
    // console.log(state)
    const url = '/users/signup'
    let body = payload
    return $axios.post(url, body)
  }

//아이디 중복 체크
export function checkSignupId ( {state}, payload) {
    //console.log(state)
    const url = `users/create/${payload.id}`
    return $axios.get(url)
  }
  