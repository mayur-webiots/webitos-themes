<template>
  <section class="pt-0 poster-section">
    <div class="poster-image slider-for custome-arrow classic-arrow">
      <vue-slick-carousel
        ref="c1"
        v-bind="settings"
        :asNavFor="$refs.c2"
        :focusOnSelect="true"
      >
        <div v-for="(image, index) in images" :key="index">
          <img
            :src="
              require(`../../../../assets/images/furniture-images/poster/${image}`)
            "
            class="img-fluid"
            alt=""
          />
          <!-- :src="'/_nuxt/assets/images/furniture-images/poster/' + image" -->
        </div>
      </vue-slick-carousel>
    </div>
    <div class="slider-nav image-show">
      <vue-slick-carousel
        v-bind="settings2"
        :style="{ height: '372px' }"
        ref="c2"
        :asNavFor="$refs.c1"
        :slidesToShow="3"
        :focusOnSelect="true"
      >
        <div
          v-for="(backgroundImage, index) in backgroundImages"
          :key="'A' + index"
        >
          <div class="poster-img">
            <img
              :src="
                require(`../../../../assets/images/furniture-images/poster/${backgroundImage}`)
              "
              class="img-fluid"
              :alt="backgroundImage"
            />
            <div class="overlay-color">
              <i class="fas fa-plus theme-color"></i>
            </div>
          </div>
        </div>
      </vue-slick-carousel>
    </div>

    <div class="left-side-contain">
      <div class="banner-left">
        <h4>Sale <span class="theme-color">35% Off</span></h4>
        <h1>New Latest <span>Furniture</span></h1>
        <p>BUY ONE GET ONE <span class="theme-color">FREE</span></p>
        <h2>
          $79.00 <span class="theme-color"><del>$65.00</del></span>
        </h2>
        <p class="poster-details mb-0">
          Lorem Ipsum is simply dummy text of the printing and typesetting
          industry.
        </p>
      </div>
    </div>

    <div class="right-side-contain">
      <div class="social-image">
        <h6>Facebook</h6>
      </div>

      <div class="social-image">
        <h6>Instagram</h6>
      </div>

      <div class="social-image">
        <h6>Twitter</h6>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  data() {
    return {
      images: ["1.png", "2.png", "3.png"],
      backgroundImages: ["t1.jpg", "t2.jpg", "t3.jpg"],
      settings: {
        dots: true,
        dotsClass: "slick-dots custom-dot-class",
        edgeFriction: 0.35,
        infinite: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
      },
      settings2: {
        centerMode: true,
        centerPadding: "30px",
        dots: true,
        infinite: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        vertical: true,
        verticalSwiping: true,
        swipeToSlide: true,
        arrows: true,
      },
    };
  },
  components: {
    "vue-slick-carousel": VueSlickCarousel,
  },
};
</script>

<style></style>
