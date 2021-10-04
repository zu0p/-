module.exports = {
  publicPath: "/",
  devServer: {
    disableHostCheck: true,
    proxy: {
      "/api": {
        target: "http://localhost:8000/",
      },
    },
  },
  transpileDependencies: ["vuetify"],
};
