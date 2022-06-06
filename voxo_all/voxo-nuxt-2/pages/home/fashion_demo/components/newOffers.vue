<template>
  <div>
    <section class="banner-style-2 offer-banner">
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="title title-2 text-center">
              <h2>New Offers</h2>
              <h5 class="text-color">Just For You</h5>
            </div>
          </div>
        </div>
        <div class="row gy-4">
          <div class="col-lg-6 ratio2_1">
            <div class="collection-banner p-right text-right">
              <a
                href="shop-left-sidebar.html"
                class="banner-img"
                :class="isLoaded ? 'sliderBackground bg-size' : ''"
                :style="{
                  'background-image': 'url(' + image4 + ')',
                }"
              >
                <img
                  src="~assets/images/fashion/banner/4.jpg"
                  class="bg-img"
                  alt=""
                  :style="{ display: isLoaded ? 'none' : '' }"
                />
              </a>
              <div class="banner-text">
                <div class="banner-content">
                  <span class="span-top"
                    >New <span class="theme-color">Collections</span></span
                  >
                  <h2>
                    New Red Jackets from <span class="theme-color">$48</span>
                  </h2>
                  <buttonAnimated
                    buttonClasses="btn btn-solid-default"
                    headerLocation="/shop/shop_left_sidebar"
                    buttonContent="Shop Now"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="row gy-4">
              <div class="col-lg-12 ratio_40">
                <div class="collection-banner p-left banner-title">
                  <a
                    href="shop-left-sidebar.html"
                    class="banner-img"
                    :class="isLoaded ? 'sliderBackground bg-size' : ''"
                    :style="{
                      'background-image': 'url(' + image5 + ')',
                    }"
                  >
                    <img
                      src="~assets/images/fashion/banner/5.jpg"
                      class="bg-img"
                      alt=""
                      :style="{ display: isLoaded ? 'none' : '' }"
                    />
                  </a>
                  <div class="banner-text">
                    <div class="banner-content">
                      <h3 class="h-bottom">
                        New Hoodies from <span class="theme-color">$34</span>
                      </h3>

                      <buttonAnimated
                        buttonContent="Shop Now"
                        buttonClasses="btn btn-solid-default"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-sm-6 ratio2_3" v-for="i in 2">
                <div class="collection-banner p-center text-center">
                  <a
                    href="shop-left-sidebar.html"
                    class="banner-img"
                    :class="isLoaded ? 'sliderBackground bg-size' : ''"
                    :style="{
                      'background-image': 'url(' + image6 + ')',
                    }"
                  >
                    <img
                      src="~assets/images/fashion/banner/6.jpg"
                      class="bg-img"
                      alt=""
                      :style="{ display: isLoaded ? 'none' : '' }"
                    />
                  </a>
                  <a href="shop-left-sidebar.html" class="contain-banner">
                    <div class="banner-content with-bg">
                      <h3 class="mb-1">New jacket</h3>
                      <span>Discount -70%</span>
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import buttonAnimated from "~/components/elements/buttons/button_animated.vue";
export default {
  components: { buttonAnimated },
  data() {
    return {
      image4: "/_nuxt/assets/images/fashion/banner/4.jpg",
      image5: "/_nuxt/assets/images/fashion/banner/5.jpg",
      image6: "/_nuxt/assets/images/fashion/banner/6.jpg",
      image7: "/_nuxt/assets/images/fashion/banner/7.jpg",
      isLoaded: false,
    };
  },
  created() {
    this.isLoaded = true;
  },
};
</script>

<style></style>
