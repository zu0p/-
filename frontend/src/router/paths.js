export default [
  {
    path: "/main",
    view: "Main",
    name: "Main"
  },
  {
    path: "/",
    view: "Login",
    name: "Login"
  },
  {
    path: "/pages/:title",
    view: "pages",
    name: "Page",
    children:[
      {
        path:"/pages/:title/first",
        name:"BeforeCreate",
        view:"page/BeforeCreate",
      }
    ]
  },
];
