const swiper = new Swiper('.swiper', {

  autoplay: {
     delay: 3000,
     disableOnInteraction: false
   },

  // Optional parameters
  direction: 'horizontal',
  loop: true,
  speed: 1200,
  watchSlidesProgress: true,
  parallax: true,

  // If we need pagination
   pagination: {
      el: ".swiper-pagination",
      type: "fraction",
    },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

});