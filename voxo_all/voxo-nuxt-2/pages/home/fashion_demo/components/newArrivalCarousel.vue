<template>
  <section class="ratio_asos">
    <div class="container">
      <div class="row m-0">
        <div class="col-sm-12 p-0">
          <div class="title title-2 text-center">
            <h2>New Arrival</h2>
            <h5 class="text-color">Our collection</h5>
          </div>
          <div
            class="product-wrapper product-style-2 slide-4 p-0 light-arrow bottom-space"
          >
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <div v-for="i in 5">
                <arrivalProductsCard
                  :imageBack="imageBack"
                  :imageFront="imageFront"
                />
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
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import arrivalProductsCard from "~/components/elements/cards/arrivalProductsCard/index.vue";
export default {
  components: {
    arrivalProductsCard,
    "vue-slick-carousel": VueSlickCarousel,
  },
  data() {
    return {
      imageFront: "/_nuxt/assets/images/fashion/product/front/1.jpg",
      imageBack: "/_nuxt/assets/images/fashion/product/back/1.jpg",
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: "10px",

        // focusOnSelect: true,
        infinite: true,
        slidesToShow: 4,
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
