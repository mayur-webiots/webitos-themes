<template>
  <div>
    <div class="product-box">
      <div class="img-wrapper">
        <div class="top-wishlist product-color">
          <a href="wishlist.html" class="heart-wishlist heart-color ms-auto">
            <i class="far fa-heart"></i>
          </a>
        </div>
        <div class="share share-box share-opacity">
          <span class="share-plus share-plus-color">+</span>
          <span>Share</span>
        </div>
        <a href="javascript:void(0)" class="text-center" :class="isLoaded ? 'sliderBackground bg-size' : ''" :style="{
            'background-image': 'url(' + image + ')',
          }">
          <img src="~assets/images/fashion/instagram/1.jpg" class="bg-img" alt=""
            :style="{ display: isLoaded ? 'none' : '' }" />
        </a>
      </div>
      <div class="insta-hover insta-spacing text-center">
        <div>
          <h5>New Offer -56% Discount</h5>
          <h3 class="text-hide">Women T-shirt From $35</h3>

          <buttonAnimated buttonClasses="btn btn-light-white" buttonContent="Shop Now"><i
              class="fas fa-chevron-right ms-2"></i></buttonAnimated>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import buttonAnimated from "~/components/elements/buttons/button_animated.vue";
  import VueSlickCarousel from "vue-slick-carousel";
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

  export default {
    components: {
      buttonAnimated,
      "vue-slick-carousel": VueSlickCarousel,
    },
    data() {
      return {
        isLoaded: false,
        image: "/_nuxt/assets/images/fashion/instagram/1.jpg",

        settings: {
          centerMode: true,
          centerPadding: "20px",
          focusOnSelect: true,
          infinite: true,
          slidesToShow: 5,
          speed: 500,
          dots: true,
          responsive: [
            {
              breakpoint: 1400,
              settings: {
                slidesToShow: 4,
                centerPadding: "10px",
                slidesToScroll: 4,
                infinite: true,
                dots: true,
              },
            },
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true,
              },
            },
            {
              breakpoint: 1000,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                initialSlide: 2,
              },
            },
          ],
        },
      };
    },
    created() {
      this.isLoaded = true;
    },
  };
</script>

<style></style>