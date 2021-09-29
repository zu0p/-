import $axios from 'axios'

export function requestLogin ({ state }, payload){
    const url = '/users/login'
    let body = payload
    return $axios.post(url, body)
}