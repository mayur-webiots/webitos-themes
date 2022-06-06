<template>
  <section class="home-section home-style-2 pt-0">
    <div class="container-fluid p-0">
      <div class="slick-2 dot-dark">
        <vue-slick-carousel v-bind="settings" ref="brandCarousel">
          <div v-for="i in 3">
            <div class="home-slider">
              <div class="home-wrap row m-0">
                <div class="col-xxl-3 col-lg-4 p-0 d-lg-block d-none">
                  <div class="home-left-wrapper">
                    <div>
                      <h2>Raw Ham Colorblock T-shirt</h2>

                      <div class="d-flex">
                        <ul class="rating p-0 me-2">
                          <li>
                            <i class="fas fa-star theme-color"></i>
                          </li>
                          <li>
                            <i class="fas fa-star theme-color"></i>
                          </li>
                          <li>
                            <i class="fas fa-star theme-color"></i>
                          </li>
                          <li>
                            <i class="fas fa-star theme-color"></i>
                          </li>
                          <li>
                            <i class="fas fa-star theme-color"></i>
                          </li>
                        </ul>
                        <h6 class="text-light">( 5040 Review )</h6>
                      </div>

                      <p>
                        The international hoodies with excellent durable fabric,
                        not to heavy but simply PERFECT for Indian summer.
                      </p>
                      <h3>$49.55 <span class="theme-color">$49.55</span></h3>
                      <ul class="selection-wrap">
                        <li>
                          <div class="dark-select">
                            <select class="form-select">
                              <option selected>Size</option>
                              <option value="1">S</option>
                              <option value="2">M</option>
                              <option value="3">L</option>
                              <option value="4">XL</option>
                            </select>
                            <i class="fas fa-chevron-down"></i>
                          </div>
                        </li>
                        <li>
                          <div class="dark-select">
                            <select class="form-select">
                              <option selected>Color</option>
                              <option value="1">Black</option>
                              <option value="2">White</option>
                              <option value="3">Blue</option>
                              <option value="4">Gray</option>
                            </select>
                            <i class="fas fa-chevron-down"></i>
                          </div>
                        </li>
                        <li>
                          <div class="dark-select">
                            <select class="form-select">
                              <option selected>Qty</option>
                              <option value="1">1</option>
                              <option value="2">2</option>
                              <option value="3">3</option>
                              <option value="4">4</option>
                            </select>
                            <i class="fas fa-chevron-down"></i>
                          </div>
                        </li>
                      </ul>
                      <div class="add-btn">
                        <a href="cart.html" class="btn btn-white"
                          >Add to cart</a
                        >
                        <a
                          href="javascript:void:(0)"
                          class="btn btn-solid-default ms-2"
                        >
                          <i class="fas fa-heart"></i>
                        </a>
                      </div>
                      <div class="share-icons">
                        <span>share with</span>
                        <ul class="share-icons p-0">
                          <li>
                            <a
                              target="_blank"
                              href="https://www.facebook.com/sharer/sharer.php?u=#url"
                            >
                              <img
                                src="~assets/images/social-icon/4.png"
                                class="img-fluid"
                                alt="social icon"
                              />
                            </a>
                          </li>
                          <li>
                            <a href="https://www.google.co.in/">
                              <img
                                src="~assets/images/social-icon/5.png"
                                class="img-fluid"
                                alt="social icon"
                              />
                            </a>
                          </li>
                          <li>
                            <a href="http://www.twitter.com/share">
                              <img
                                src="~assets/images/social-icon/6.png"
                                class="img-fluid"
                                alt="social icon"
                              />
                            </a>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="col-xxl-9 col-lg-8 p-0 left-content"
                  :class="isLoaded ? 'sliderBackground bg-size' : ''"
                  :style="{
                    'background-image':
                      'url(/_nuxt/assets/images/fashion/slider/1.jpg)',
                  }"
                >
                  <img
                    src="~assets/images/fashion/slider/1.jpg"
                    class="bg-img"
                    alt=""
                    :style="{ display: isLoaded ? 'none' : '' }"
                  />
                  <div class="home-content row">
                    <div class="col-xxl-4 col-lg-4 col-md-4 col-sm-5 col-6">
                      <h3>Sale <span class="theme-color">70% OFF</span></h3>
                      <h1 data-animation-in="fadeInUp">New Tranding Fashion</h1>
                      <h6
                        class="mb-4"
                        data-animation-in="fadeInUp"
                        data-delay-in="0.4"
                      >
                        BUY ONE GET ONE <span class="theme-color">FREE</span>
                      </h6>
                      <div
                        class="discover-block"
                        data-animation-in="fadeInUp"
                        data-delay-in="0.7"
                      >
                        <div class="d-flex">
                          <a
                            href="javascript:void(0)"
                            class="play-icon theme-bg-color"
                          >
                            <i class="fas fa-play"></i>
                          </a>
                          <div class="discover-content">
                            <h4 class="theme-color mb-1">Discover</h4>
                            <h6>Our Collection</h6>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </vue-slick-carousel>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
export default {
  components: {
    "vue-slick-carousel": VueSlickCarousel,
  },
  data() {
    return {
      isLoaded: false,
      image: "/_nuxt/assets/images/fashion/slider/1.jpg",
      settings: {
        dots: true,
        dotsClass: "slick-dots custom-dot-class",
        edgeFriction: 0.35,
        infinite: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        autoplay: false,
        autoplaySpeed: 3000,
        pauseOnFocus: false,
      },
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style lang="scss">
@import "~assets/scss/demo2.scss";
// @import "~assets/scss/demo2_dark.scss";
</style>
