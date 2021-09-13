import Vue from "vue";
import Router from "vue-router";

// Routes
import paths from "./paths";

function route(path, view, name, children) {
  console.log(children)
  return {
    name: name || view,
    path: path,
    component: resolve => import(`@/views/${view}.vue`).then(resolve),
    children: children!=undefined?children:null
  };
}

Vue.use(Router);

// Create a new router
const router = new Router({
  mode: "history",
  routes:[
    {
      name: 'Login',
      path: '/',
      component: resolve => import(`@/views/Login.vue`).then(resolve)
    },
    {
      name: 'Main',
      path: '/main',
      component: resolve => import(`@/views/Main.vue`).then(resolve)
    },
    {
      name: 'Pages',
      path: '/pages/:title',
      component: resolve => import(`@/views/page/Page.vue`).then(resolve),
      children:[
        {
          path:"first",
          name:"BeforeCreate",
          component: resolve => import(`@/views/page/BeforeCreate.vue`).then(resolve),
        }
      ]
    },
  ]
  // routes: paths
  //   .map(path => route(path.path, path.view, path.name))
  // //   .concat([{ path: "*", redirect: "/" }]),
  // // scrollBehavior(to, from, savedPosition) {
  // //   if (savedPosition) {
  // //     return savedPosition;
  // //   }
  // //   if (to.hash) {
  // //     return { selector: to.hash };
  // //   }
  // //   return { x: 0, y: 0 };
  // // }
});

export default router;
