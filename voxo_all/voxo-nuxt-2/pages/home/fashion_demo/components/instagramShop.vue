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
                  <instagramShopCard v-for="i in 5" :key="i" />
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
  import instagramShopCard from "~/components/elements/cards/instagramShopCard/index.vue";
  import buttonAnimated from "~/components/elements/buttons/button_animated.vue";
  import VueSlickCarousel from "vue-slick-carousel";
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

  export default {
    components: {
      buttonAnimated,
      "vue-slick-carousel": VueSlickCarousel,
      instagramShopCard,
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