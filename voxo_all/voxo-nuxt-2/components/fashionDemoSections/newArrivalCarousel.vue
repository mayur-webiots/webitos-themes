<template>
  <section class="ratio_asos">
    <div class="container">
      <div class="row m-0">
        <div class="col-sm-12 p-0">
          <div class="title title-2 text-center">
            <h2>New Arrival</h2>
            <h5 class="text-color">Our collection</h5>
          </div>
          <div class="product-wrapper product-style-2 slide-4 p-0 light-arrow bottom-space">
            <vue-slick-carousel v-bind="settings" ref="brandCarousel">
              <div v-for="i in 5">
                <div class="product-box">
                  <div class="img-wrapper">
                    <div class="front">
                      <a href="product-left-sidebar.html" :class="isLoaded ? 'sliderBackground bg-size' : ''" :style="{
                          'background-image': 'url(' + imageFront + ')',
                        }">
                        <img src="~assets/images/fashion/product/front/1.jpg" class="bg-img" alt=""
                          :style="{ display: isLoaded ? 'none' : '' }" />
                      </a>
                    </div>
                    <div class="back">
                      <a href="product-left-sidebar.html" :class="isLoaded ? 'sliderBackground bg-size' : ''" :style="{
                          'background-image': 'url(' + imageBack + ')',
                        }">
                        <img src="~assets/images/fashion/product/back/1.jpg" class="bg-img" alt=""
                          :style="{ display: isLoaded ? 'none' : '' }" />
                      </a>
                    </div>
                    <div class="cart-wrap">
                      <ul>
                        <li>
                          <a href="javascript:void(0)" class="addtocart-btn" data-bs-toggle="modal"
                            data-bs-target="#addtocart">
                            <vue-feather type="shopping-bag"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a href="javascript:void(0)" data-bs-toggle="modal" data-bs-target="#quick-view">
                            <vue-feather type="eye"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a href="compare.html">
                            <vue-feather type="refresh-cw"></vue-feather>
                          </a>
                        </li>
                        <li>
                          <a href="wishlist.html" class="wishlist">
                            <vue-feather type="heart"></vue-feather>
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <productDetails />
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
  import productDetails from "./components/productDetails.vue";
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
  import VueFeather from "vue-feather";
  export default {
    components: {
      VueFeather,
      productDetails,
      "vue-slick-carousel": VueSlickCarousel,
    },
    data() {
      return {
        isLoaded: false,
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
    created() {
      this.isLoaded = true;
    },
  };
</script>

<style></style>