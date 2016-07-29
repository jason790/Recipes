module.exports = {
  entry: "src/js/main.js",
  output: {
    path: __dirname,
    filename: "main.js",
    publicPath: "/static/js/"
  },
  module: {
    loaders: [
      {
        loader: "jsx-loader?insertPragma==React.DOM&harmony"
      }
    ]
  },
  externals: {
    "react": "react"
  },
  resolve: {
    extensions: [
      "", ".js", ".jsx",
    ]
  }
}
