<template>
  <section>
    <div class="container-fluid">
      <div class="row">
        <div class="col">
          <div class="title-3 text-center">
            <h2>Instagram Shop</h2>
            <h5 class="theme-color">New Collection</h5>
          </div>
          <div class="product-style-1">
            <div class="product-wrapper insta-slider instagram-wrap">
              <vue-slick-carousel v-bind="settings">
                <div v-for="(image, index) in imageList" :key="index">
                  <div class="product-box product-box1">
                    <div class="img-wrapper">
                      <div class="top-wishlist">
                        <a
                          href="javascript:void(0)"
                          class="heart-wishlist ms-auto"
                        >
                          <i class="far fa-heart"></i>
                        </a>
                      </div>
                      <a href="javascript:void(0)" class="text-center">
                        <img
                          :src="
                            require(`../../../../assets/images/furniture-images/shop/${image}`)
                          "
                          class="img-fluid"
                          alt=""
                        />
                      </a>
                    </div>
                    <div class="insta-hover insta-hover-gradient text-center">
                      <div>
                        <h2>Women</h2>
                        <h5>New Offer -56% Discount</h5>
                        <h3 class="brand-name">Latest Night Lamp From $35</h3>
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
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";

export default {
  components: { VueSlickCarousel },
  data() {
    return {
      imageList: ["1.png", "2.png", "3.png", "4.png", "2.png", "1.png"],
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
};
</script>

<style></style>
