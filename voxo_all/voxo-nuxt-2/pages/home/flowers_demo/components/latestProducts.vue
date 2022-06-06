<template>
  <section class="ratio_asos">
    <div class="container p-sm-0">
      <div class="row m-0">
        <div class="col-sm-12 p-0">
          <div class="title title-2 text-center">
            <h2>Latest Product</h2>
            <h5>Our Collection</h5>
          </div>
          <div class="product-wrapper slide-5_1">
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <latestProductsCard v-for="i in 6" :key="i" :image="image" />
            </vue-slick-carousel>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import latestProductsCard from "~/components/elements/cards/latestProductsCard/index.vue";
export default {
  components: {
    VueSlickCarousel,
    latestProductsCard,
  },
  data() {
    return {
      image: "/_nuxt/assets/images/flower/product/1.jpg",
      imageBack: "/_nuxt/assets/images/flower/product/1.jpg",
      settings: {
        arrows: false,
        centerPadding: "10px",
        infinite: false,
        slidesToShow: 5,
        speed: 500,
        dots: true,
        responsive: [
          {
            breakpoint: 1200,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              infinite: false,
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
