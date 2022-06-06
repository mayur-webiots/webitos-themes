<template>
  <div>
    <section class="ratio_square">
      <div class="container-fluid">
        <div class="row">
          <div class="col">
            <div class="title title-2 text-center">
              <h2>Instagram Shop</h2>
              <h5 class="text-color">New Collection</h5>
            </div>
            <div class="product-style-1 instagram-2 product-wrapper">
              <div class="insta-slider instagram-wrap">
                <vue-slick-carousel v-bind="settings" ref="brandCarousel">
                  <div v-for="i in 5">
                    <div class="product-box">
                      <div class="img-wrapper">
                        <div class="top-wishlist product-color">
                          <a
                            href="wishlist.html"
                            class="heart-wishlist heart-color ms-auto"
                          >
                            <i class="far fa-heart"></i>
                          </a>
                        </div>
                        <div class="share share-box share-opacity">
                          <span class="share-plus share-plus-color">+</span>
                          <span>Share</span>
                        </div>
                        <a href="javascript:void(0)" class="text-center">
                          <img
                            src="~assets/images/fashion/instagram/1.jpg"
                            class="bg-img"
                            alt=""
                          />
                        </a>
                      </div>
                      <div class="insta-hover insta-spacing text-center">
                        <div>
                          <h5>New Offer -56% Discount</h5>
                          <h3 class="text-hide">Women T-shirt From $35</h3>
                          <button
                            onclick="location.href = 'shop-left-sidebar.html';"
                            type="button"
                            class="btn btn-light-white"
                          >
                            Shop now <i class="fas fa-chevron-right ms-2"></i>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </vue-slick-carousel>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  components: {
    "vue-slick-carousel": VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        // dots: true,
        // dotsClass: "slick-dots custom-dot-class",
        // edgeFriction: 0.35,
        // infinite: false,
        // speed: 500,
        // slidesToShow: 1,
        // slidesToScroll: 1,
        // infinite: true,
        // autoplay: true,
        // autoplaySpeed: 3000,
        // pauseOnFocus: false,
        centerMode: true,
        centerPadding: "20px",
        focusOnSelect: true,
        infinite: true,
        slidesToShow: 5,
        speed: 500,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 5,
              slidesToScroll: 5,
              infinite: true,
              dots: true,
            },
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              initialSlide: 2,
            },
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
            },
          },
        ],
      },
    };
  },
};
</script>

<style></style>
