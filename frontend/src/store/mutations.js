import Cookies from "js-cookie";

export function SET_ACCESS_TOKEN (state, user) {
	// console.log("SET_ACCESS_TOKEN: "+ user);
  state.accessToken = Cookies.get("accessToken");
  if(user){
    (state.user=user);
  }
}

export function LOGIN (state, payload) {
	Cookies.set("accessToken",payload["auth-token"]);
  state.accessToken=payload["auth-token"];
  state.user=payload["user"];
}