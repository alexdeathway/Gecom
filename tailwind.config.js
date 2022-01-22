module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: false, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
  }
  //tailwindcss  build ./static/css/tailwind.css -o ./static/css/style.css && cleancss -o ./static/css/style.min.css ./static/css/style.css