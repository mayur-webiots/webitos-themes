<template>
  <section class="product-slider overflow-hidden">
    <div>
      <div class="container">
        <div class="row g-3">
          <div class="col-lg-4" v-for="(items, index) in cards" :key="index">
            <div class="title-3 pb-4 title-border">
              <h2>{{ items.heading }}</h2>
              <h5 class="theme-color">{{ items.subHeading }}</h5>
            </div>
            <div class="product-slider round-arrow">
              <vue-slick-carousel v-bind="settings" ref="brandCarousel">
                <div v-for="j in 2">
                  <div class="row g-3">
                    <div class="col-lg-12 col-md-6 col-12" v-for="(card, index2) in items.children" :key="index2">
                      <div class="product-image">
                        <a href="product-left-sidebar.html">
                          <img :src="
                              require(`../../../../assets/images/furniture-images/product/${card.image}`)
                            " :alt="card.image" />
                        </a>
                        <div class="product-details">
                          <a href="product-left-sidebar.html">
                            <h6 class="font-light">card.description</h6>
                            <h3>{{ card.productName }}</h3>
                            <h4 class="font-light mt-1">
                              <del>${{ card.mrp }}</del>
                              <span class="theme-color">${{ card.price }}</span>
                            </h4>
                            <div class="cart-wrap">
                              <ul>
                                <li data-bs-toggle="tooltip" data-bs-placement="top" title="Buy">
                                  <a href="javascript:void(0)" class="addtocart-btn" data-bs-toggle="modal"
                                    data-bs-target="#addtocart">
                                    <vue-feather type="shopping-bag"></vue-feather>
                                  </a>
                                </li>
                                <li data-bs-toggle="tooltip" data-bs-placement="top" title="Quick View">
                                  <a href="javascript:void(0)" data-bs-toggle="modal" data-bs-target="#quick-view">
                                    <vue-feather type="eye"></vue-feather>
                                  </a>
                                </li>
                                <li data-bs-toggle="tooltip" data-bs-placement="top" title="Compare">
                                  <a href="compare.html">
                                    <vue-feather type="refresh-cw"></vue-feather>
                                  </a>
                                </li>
                                <li data-bs-toggle="tooltip" data-bs-placement="top" title="Wishlist">
                                  <a href="wishlist.html" class="wishlist">
                                    <vue-feather type="heart"></vue-feather>
                                  </a>
                                </li>
                              </ul>
                            </div>
                          </a>
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
    </div>
  </section>
</template>
<script>
  import VueSlickCarousel from "vue-slick-carousel";
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
  import VueFeather from "vue-feather";
  import { mapState } from "vuex";
  export default {
    components: {
      "vue-slick-carousel": VueSlickCarousel,
      VueFeather,
    },
    computed: {
      ...mapState({
        cards: (state) => state.popularCards.data,
      }),
    },
    data() {
      return {
        settings: {
          arrows: true,
          centerMode: true,
          centerPadding: "10px",
          infinite: true,
          slidesToShow: 1,
          speed: 500,
          responsive: [
            {
              breakpoint: 1000,
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