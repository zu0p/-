import Vue from "vue";
import Router from "vue-router";

// Routes
import paths from "./paths";

function route(path, view, name, children) {
  console.log(children);
  return {
    name: name || view,
    path: path,
    component: (resolve) => import(`@/views/${view}.vue`).then(resolve),
    children: children != undefined ? children : null,
  };
}

Vue.use(Router);

// Create a new router
const router = new Router({
  mode: "history",
  routes: [
    {
      name: "Login",
      path: "/",
      component: (resolve) => import(`@/views/Login.vue`).then(resolve),
    },
    {
      name: "Main",
      path: "/main",
      component: (resolve) => import(`@/views/Main.vue`).then(resolve),
    },
    {
      name: "PageList",
      path: "/pageList",
      component: (resolve) => import(`@/views/page/PageList.vue`).then(resolve),
    },
    {
      name: "Pages",
      path: "/pages",
      component: (resolve) => import(`@/views/page/Page.vue`).then(resolve),
      children: [
        {
          path: "first",
          name: "BeforeCreate",
          component: (resolve) => import(`@/views/page/BeforeCreate.vue`).then(resolve),
        },
        {
          path: "create",
          name: "CreatePage",
          component: (resolve) => import(`@/views/page/CreatePage.vue`).then(resolve),
          props: true,
          children: [
            {
              path: "imageSelect",
              name: "ImageSelect",
              component: (resolve) => import(`@/components/page/ImageSelectorItem.vue`).then(resolve),
            },
          ],
        },
        {
          path: "preview",
          name: "Preview",
          component: (resolve) => import(`@/views/page/Preview.vue`).then(resolve),
          props: true
        },
        {
          path: "detailView",
          name: "DetailView",
          component: (resolve) => import(`@/views/page/DetailView.vue`).then(resolve),
          props: true
        },
      ],
    },
  ],
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
