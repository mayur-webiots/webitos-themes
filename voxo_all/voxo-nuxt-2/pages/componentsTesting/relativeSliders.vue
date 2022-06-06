<template>
  <div>
    <div class="container">
      <VueSlickCarousel
        v-bind="settings"
        ref="c1"
        :asNavFor="$refs.c2"
        :focusOnSelect="true"
      >
        <div v-for="i in 4" :key="i">
          <h3>{{ i }}</h3>
        </div>
      </VueSlickCarousel>
    </div>
    <div class="container">
      <VueSlickCarousel
        v-bind="settings2"
        ref="c2"
        :asNavFor="$refs.c1"
        :slidesToShow="1"
        :focusOnSelect="true"
        :style="{ height: '372px' }"
      >
        <div v-for="i in 4" :key="i">
          <h3>{{ i }}</h3>
        </div>
      </VueSlickCarousel>
    </div>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
      settings: {
        dots: true,
        dotsClass: "slick-dots custom-dot-class",
        edgeFriction: 0.35,
        infinite: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
      },
      settings2: {
        centerMode: true,
        centerPadding: "30px",
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        vertical: true,
        verticalSwiping: true,
        swipeToSlide: true,
      },
    };
  },
};
</script>

<style></style>
