<template>
  <section class="category-section ratio_40">
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <div class="title title-2 text-center">
            <h2>Our Category</h2>
            <h5>Our collection</h5>
          </div>
        </div>
      </div>
      <div class="row gy-3">
        <div class="col-xxl-2 col-lg-3">
          <div class="category-wrap category-padding theme-bg-color">
            <div>
              <h2 class="light-text">Top</h2>
              <h2>Our Top</h2>
              <span>Categories</span>
            </div>
          </div>
        </div>
        <div class="col-xxl-10 col-lg-9">
          <div
            class="category-wrapper category-slider1 white-arrow product-wrapper"
          >
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <div v-for="i in 5" :key="i">
                <a
                  href="shop-left-sidebar.html"
                  class="category-wrap"
                  :class="isLoaded ? 'sliderBackground bg-size' : ''"
                  :style="{
                    'background-image': 'url(' + image + ')',
                  }"
                >
                  <img
                    src="~assets/images/flower/categories/1.jpg"
                    class="bg-img"
                    :style="{ display: isLoaded ? 'none' : '' }"
                    alt="category image"
                  />
                  <div class="category-content category-spacing">
                    <h3 class="theme-color">Yellow Rose</h3>
                    <span>Flowers</span>
                  </div>
                </a>
              </div>
            </vue-slick-carousel>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";

export default {
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
      isLoaded: false,
      image: "/_nuxt/assets/images/flower/categories/1.jpg",
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: "10px",
        // focusOnSelect: true,
        infinite: true,
        slidesToShow: 4,
        speed: 500,
        dots: false,
        responsive: [
          {
            breakpoint: 1400,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              infinite: true,
              dots: false,
            },
          },
          {
            breakpoint: 760,
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
