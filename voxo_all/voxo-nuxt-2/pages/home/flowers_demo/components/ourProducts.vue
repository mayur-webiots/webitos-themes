<template>
  <section>
    <div class="container">
      <div class="row gy-lg-0 gy-5">
        <div class="col-lg-8">
          <div class="title title-2 text-center">
            <h2>Our Product</h2>
            <h5>Just For You</h5>
          </div>
          <div class="product-wrapper slide-three ratio_asos">
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <latestProductsCard v-for="i in 6" :key="i" :image="image" />
            </vue-slick-carousel>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="title title-2 text-lg-start text-md-center">
            <h2>Most Popular</h2>
            <h5>Our Collection</h5>
          </div>
          <div class="product-slider round-arrow1">
            <vue-slick-carousel v-bind="settings2" ref="brandCarousel">
              <div v-for="i in 2">
                <div class="row g-3">
                  <div class="col-lg-12 col-md-6 col-12" v-for="j in 5">
                    <div class="product-image">
                      <a href="product-left-sidebar.html">
                        <img src="~assets/images/flower/product/1.jpg" alt="" />
                      </a>
                      <div class="product-details">
                        <h6 class="font-light">Fully Confirtable</h6>
                        <a href="product-left-sidebar.html" class="">
                          <h3>Beautiful and Fresh Bookey</h3>
                        </a>
                        <h4 class="font-light mt-1">
                          <del>$49.00</del>
                          <span class="theme-color">$35.50</span>
                        </h4>
                      </div>
                    </div>
                  </div>
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
  import latestProductsCard from "~/components/elements/cards/latestProductsCard/index.vue";
  export default {
    components: { latestProductsCard, VueSlickCarousel },
    data() {
      return {
        image: "/_nuxt/assets/images/flower/product/1.jpg",
        imageBack: "/_nuxt/assets/images/flower/product/1.jpg",
        settings: {
          arrows: false,
          centerPadding: "10px",
          infinite: false,
          slidesToShow: 3,
          speed: 500,
          responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                infinite: false,
              },
            },
          ],
        },
        settings2: {
          arrows: true,
          centerPadding: "10px",
          infinite: true,
          slidesToShow: 1,
          speed: 500,
          responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
              },
            },
          ],
        },
      };
    },
  };
</script>
<style></style>