module.exports = (grunt) ->

  grunt.loadNpmTasks("grunt-contrib-watch")
  grunt.loadNpmTasks("grunt-babel")
  grunt.loadNpmTasks("grunt-contrib-coffee")
  grunt.loadNpmTasks("grunt-contrib-uglify")
  grunt.loadNpmTasks("grunt-contrib-copy")
  grunt.loadNpmTasks("grunt-contrib-concat")
  grunt.loadNpmTasks("grunt-contrib-sass")
  grunt.loadNpmTasks("grunt-contrib-cssmin");

  # Initialize the configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON("package.json")

    sass:
      default:
        options:
          style: "compressed"
          sourcemap: true
        files: [
          "recipes/static/css/style.css": "src/css/style.scss"
        ]

    cssmin:
      options:
        shorthandCompacting: false,
        roundingPrecision: -1
      target:
        files:
          "recipes/static/css/style.css": ["recipes/static/css/style.css"]

    babel:
      options:
        sourceMap: true,
        presets: ["es2015", "react"]
        plugins: ["transform-react-jsx"]
      jsx:
        files: [
          expand: true
          cwd: "src/js"
          src: "*.js"
          dest: "recipes/static/js"
          ext: ".js"
        ]

    watch:
      sass:
        files: [
          "src/css/style.scss"
        ]
        tasks: ["sass"]
      babel:
        files: [
          "src/js/main.js"
        ]
        tasks: ["babel:jsx"]

    concat:
      dev:
        src: [
          "recipes/static/lib/google/analytics.js",
          "recipes/static/lib/facebook/pixel.js",
          "recipes/static/lib/facebook/sdk.js",
          "recipes/static/lib/jquery/dist/jquery.min.js",
          "recipes/static/lib/react/react.min.js",
          "recipes/static/lib/react/react-dom.min.js",
          # "bower_components/babel/browser.min.js",
          # "src/js/main.js"
          "recipes/static/js/main.js"
          # "js/react-app.js"
        ]
        dest: "src/js/app.js.concat"

    uglify:
      options:
        compress: true
        mangle: false
        sourceMap: false
      target:
        src: "src/js/app.js.concat"
        dest: "recipes/static/js/app.js"

    copy:
      main:
        files: [
          {
            src: "recipes/static/css/style.css",
            dest: "recipes/static/css/style.css",
            filter: "isFile"
          }
          {
            src: "src/css/style.css.map",
            dest: "recipes/static/css/style.css.map",
            filter: "isFile"
          }
        ]


    # Allow certain options
    options:
      browser: true
      boss: true
      immed: false
      eqnull: true
      evil: true
      globals: {}

  grunt.registerTask "dist", ["babel", "sass", "concat:dev", "cssmin", "uglify", "copy:main"]
  grunt.registerTask "default", ["babel", "concat:dev", "copy", "watch"]
