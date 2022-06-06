<template>
  <section class="section-b-space">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="brand-slider">
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <div v-for="(image, index) in images" :key="index">
                <div class="brand-image">
                  <img
                    :src="'/_nuxt/assets/images/brand/' + image"
                    class="img-fluid"
                    alt="brand logo"
                  />
                </div>
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
    "vue-slick-carousel": VueSlickCarousel,
  },
  data() {
    return {
      images: ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "4.png"],
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: "10px",
        autoplay: true,
        // focusOnSelect: true,
        infinite: true,
        slidesToShow: 6,
        speed: 500,
        dots: true,
        responsive: [
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
